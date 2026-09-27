from __future__ import annotations

import asyncio
import io
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from swarm_oneshot.cli import load_config
from swarm_oneshot.env_config import apply_env_overrides, load_project_env, missing_api_key_message
from swarm_oneshot.models import (
    Finding, Plan, ReviewResult, SwarmConfig, Synthesis, Task, TaskInstruction, Track, TrackGuidance, WorkerResult,
)
from swarm_oneshot.orchestrator import Swarm
from swarm_oneshot.progress import Progress
from swarm_oneshot.runner import AgentRun
from swarm_oneshot.tools import resolve_allowed_path
from swarm_oneshot.validation import PlanError, validate_plan


EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "e2e.yaml"


def config_data() -> dict:
    import yaml

    return yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))


EXAMPLE_MULTI = Path(__file__).resolve().parents[1] / "examples" / "e2e_multi.yaml"


class FakeRunner:
    def __init__(
        self,
        *,
        dependent: bool = False,
        fail_worker: str | None = None,
        coordinator: bool = False,
        coordinator_id: str = "coordenador",
        reject_guidance: bool = False,
        fail_attempts: dict[str, int] | None = None,
        raise_on: set[str] | None = None,
        leak_secret: str | None = None,
    ) -> None:
        self.dependent = dependent
        self.fail_worker = fail_worker
        self.coordinator = coordinator
        self.coordinator_id = coordinator_id
        self.reject_guidance = reject_guidance
        self.fail_attempts = fail_attempts or {}
        self.attempt_counts: dict[str, int] = {}
        self.raise_on = raise_on or set()
        self.leak_secret = leak_secret
        self.active_workers = 0
        self.max_active_workers = 0
        self.events: list[str] = []
        self.turns: dict[str, int] = {}

    async def run(self, *, agent_id, model, instructions, prompt, output_type, tools, max_turns):
        if agent_id in self.raise_on:
            raise RuntimeError(f"falha simulada em {agent_id}")
        data = json.loads(prompt)
        self.events.append(f"start:{agent_id}")
        self.turns[agent_id] = max_turns
        if output_type is Plan:
            if self.coordinator:
                tracks = [Track(id="a", orchestrator_id="principal"), Track(id="b", orchestrator_id=self.coordinator_id)]
            else:
                tracks = [Track(id="a", orchestrator_id="principal")]
            output = Plan(
                tracks=tracks,
                tasks=[
                    Task(id="T1", track_id="a", worker_id="release-a", goal="Analisar A", acceptance="Citar A"),
                    Task(id="T2", track_id="b" if self.coordinator else "a", worker_id="release-b", goal="Analisar B", acceptance="Citar B", depends_on=["T1"] if self.dependent else []),
                ],
            )
        elif output_type is WorkerResult:
            task = data["task"]
            self.active_workers += 1
            self.max_active_workers = max(self.max_active_workers, self.active_workers)
            if self.dependent and task["id"] == "T2":
                assert "T1" in data["dependencies"]
                assert "end:release-a" in self.events
            await asyncio.sleep(0.01)
            self.active_workers -= 1
            self.attempt_counts[agent_id] = self.attempt_counts.get(agent_id, 0) + 1
            attempts_failed = self.fail_attempts.get(agent_id, 0)
            is_failing = (agent_id == self.fail_worker) or (self.attempt_counts[agent_id] <= attempts_failed)
            output = WorkerResult(
                task_id=task["id"],
                status="failed" if is_failing else "completed",
                findings=[] if is_failing else [Finding(claim=task["goal"], evidence="nota de versão", impact="ação")],
                errors=["falha simulada"] if is_failing else [],
            )
        elif output_type is ReviewResult:
            output = ReviewResult(track_id=data["track"]["id"], accepted_task_ids=list(data["task_results"]), summary="Revisado")
        elif output_type is TrackGuidance:
            output = TrackGuidance(track_id=data["track"]["id"], approved=not self.reject_guidance, task_instructions=[TaskInstruction(task_id=task["id"], instruction="Use a evidência fornecida.") for task in data["tasks"]], issues=["Faltam citações antes da execução."] if self.reject_guidance else [])
        elif output_type is Synthesis:
            answer = f"Resumo com segredo: {self.leak_secret}" if self.leak_secret else "Resumo verificado"
            evidence = [f"Evidência com {self.leak_secret}"] if self.leak_secret else ["notas A e B"]
            output = Synthesis(answer=answer, evidence=evidence)
        else:
            raise AssertionError(output_type)
        self.events.append(f"end:{agent_id}")
        return AgentRun(output=output, model_calls=1)


def run_fake(config: SwarmConfig, fake: FakeRunner):
    output = io.StringIO()
    result = asyncio.run(Swarm(config, base_dir=EXAMPLE.parent, runner=fake, progress=Progress(stream=output)).run())
    return result, output.getvalue()


def test_config_rejects_duplicate_agent_ids():
    data = config_data()
    data["workers"]["agents"][1]["id"] = "principal"
    with pytest.raises(ValidationError, match="únicos"):
        SwarmConfig.model_validate(data)


def test_two_workers_run_in_parallel_and_progress_completes():
    config = load_config(EXAMPLE)
    fake = FakeRunner()
    result, progress = run_fake(config, fake)
    assert result.status == "completed"
    assert result.completed_tasks == ["T1", "T2"]
    assert fake.max_active_workers == 2
    assert "workers        [████████████████████] 2/2" in progress
    assert "síntese" in progress
    assert result.agent_models == {"principal": "gpt-5.6-luna", "release-a": "gpt-5.6-luna", "release-b": "gpt-5.6-luna"}


def test_dependency_waits_for_predecessor():
    config = load_config(EXAMPLE)
    fake = FakeRunner(dependent=True)
    result, _ = run_fake(config, fake)
    assert result.status == "completed"
    assert fake.max_active_workers == 1


def test_coordinator_reviews_its_track():
    data = config_data()
    data["orchestrators"]["count"] = 2
    data["orchestrators"]["agents"].append({"id": "coordenador", "role": "coordinator", "model": "gpt-5.6-luna", "instructions": "Revise a frente."})
    config = SwarmConfig.model_validate(data)
    result, progress = run_fake(config, FakeRunner(coordinator=True))
    assert result.status == "completed"
    assert result.agent_models["coordenador"] == "gpt-5.6-luna"
    assert "coordenação" in progress
    assert "revisão        [████████████████████] 1/1" in progress


def test_preflight_rejection_does_not_stop_worker_execution():
    data = config_data()
    data["orchestrators"]["count"] = 2
    data["orchestrators"]["agents"].append({"id": "coordenador", "role": "coordinator", "model": "gpt-5.6-luna", "instructions": "Revise a frente."})
    config = SwarmConfig.model_validate(data)
    fake = FakeRunner(coordinator=True, reject_guidance=True)
    result, _ = run_fake(config, fake)
    assert result.status == "completed"
    assert result.completed_tasks == ["T1", "T2"]
    assert "start:release-b" in fake.events
    assert any("Orientação da frente b não aprovada" in item for item in result.limitations)


def test_worker_failure_produces_partial_when_allowed():
    data = config_data()
    data["execution"]["on_worker_failure"] = "partial"
    config = SwarmConfig.model_validate(data)
    result, _ = run_fake(config, FakeRunner(fail_worker="release-b"))
    assert result.status == "partial"
    assert result.completed_tasks == ["T1"]
    assert result.incomplete_tasks == ["T2"]
    assert "T2" in " ".join(result.limitations)


def test_tool_worker_uses_configured_turn_limit():
    data = config_data()
    data["context"]["artifacts"] = ["e2e.yaml"]
    data["workers"]["agents"][0]["tools"] = ["repository_read"]
    data["execution"]["worker_max_turns"] = 6
    data["execution"]["max_model_calls"] = 12
    config = SwarmConfig.model_validate(data)
    fake = FakeRunner()
    result, _ = run_fake(config, fake)
    assert result.status == "completed"
    assert fake.turns["release-a"] == 6
    assert fake.turns["release-b"] == 1


def test_missing_key_exits_before_api_call(tmp_path, monkeypatch):
    from swarm_oneshot import cli

    class DenySwarm:
        def __init__(self, *args, **kwargs):
            raise AssertionError("A execução não deve começar sem chave")

    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr(cli, "Swarm", DenySwarm)
    monkeypatch.setattr("sys.argv", ["swarm-oneshot", "run", "--config", str(EXAMPLE), "--output", str(tmp_path / "no-output.json"), "--no-env-overrides"])
    assert cli.main() == 2


def test_plan_cycle_is_rejected():
    config = load_config(EXAMPLE)
    plan = Plan(
        tracks=[Track(id="a", orchestrator_id="principal")],
        tasks=[
            Task(id="T1", track_id="a", worker_id="release-a", goal="A", acceptance="A", depends_on=["T2"]),
            Task(id="T2", track_id="a", worker_id="release-b", goal="B", acceptance="B", depends_on=["T1"]),
        ],
    )
    with pytest.raises(PlanError, match="ciclo"):
        validate_plan(config, plan)


def test_budget_keeps_turn_for_final_answer():
    data = config_data()
    data["execution"]["max_model_calls"] = 3
    config = SwarmConfig.model_validate(data)
    result, _ = run_fake(config, FakeRunner())
    assert result.status == "failed"
    assert result.usage.model_calls <= 3
    assert len(result.incomplete_tasks) == 1


def test_all_model_outputs_have_sdk_strict_schemas():
    from agents import AgentOutputSchema

    for output_type in (Plan, WorkerResult, TrackGuidance, ReviewResult, Synthesis):
        assert AgentOutputSchema(output_type).json_schema()


def test_env_resizes_agents_and_assigns_individual_models(monkeypatch):
    monkeypatch.setenv("SWARM_ORCHESTRATOR_COUNT", "3")
    monkeypatch.setenv("SWARM_WORKER_COUNT", "3")
    monkeypatch.setenv("SWARM_PRIMARY_MODEL", "model-primary")
    monkeypatch.setenv("SWARM_COORDINATOR_MODELS", "model-c1,model-c2")
    monkeypatch.setenv("SWARM_WORKER_MODELS", "model-w1,model-w2,model-w3")
    monkeypatch.setenv("SWARM_ALLOWED_MODELS", "model-primary,model-c1,model-c2,model-w1,model-w2,model-w3")
    monkeypatch.setenv("SWARM_MAX_PARALLEL_WORKERS", "3")
    config = SwarmConfig.model_validate(apply_env_overrides(config_data()))
    assert config.orchestrators.count == 3
    assert config.workers.count == 3
    assert [a.model for a in config.orchestrators.agents] == ["model-primary", "model-c1", "model-c2"]
    assert [a.model for a in config.workers.agents] == ["model-w1", "model-w2", "model-w3"]
    assert len({a.id for a in config.orchestrators.agents + config.workers.agents}) == 6


def test_env_rejects_mismatched_model_list(monkeypatch):
    monkeypatch.setenv("SWARM_WORKER_COUNT", "3")
    monkeypatch.setenv("SWARM_WORKER_MODELS", "model-a,model-b")
    with pytest.raises(ValueError, match="requer 1 ou 3 modelos"):
        apply_env_overrides(config_data())


def test_env_overrides_worker_turn_limit(monkeypatch):
    monkeypatch.setenv("SWARM_WORKER_MAX_TURNS", "5")
    config = SwarmConfig.model_validate(apply_env_overrides(config_data()))
    assert config.execution.worker_max_turns == 5


def test_repository_read_is_limited_to_declared_artifacts(tmp_path):
    allowed = tmp_path / "code.py"
    allowed.write_text("print('ok')\n", encoding="utf-8")
    secret = tmp_path / ".env"
    secret.write_text("OPENAI_API_KEY=secret\n", encoding="utf-8")
    assert resolve_allowed_path(tmp_path, ["code.py"], "code.py") == allowed
    with pytest.raises(ValueError, match="não declarado"):
        resolve_allowed_path(tmp_path, ["code.py"], ".env")
    with pytest.raises(ValueError, match="fora"):
        resolve_allowed_path(tmp_path, ["code.py"], "../outside")


def test_env_file_supplies_key_when_shell_value_is_empty(tmp_path, monkeypatch):
    env_path = tmp_path / ".env"
    env_path.write_text("OPENAI_API_KEY=test-key\n", encoding="utf-8")
    monkeypatch.setenv("OPENAI_API_KEY", "")
    load_project_env(env_path)
    assert __import__("os").environ["OPENAI_API_KEY"] == "test-key"


def test_missing_key_message_identifies_blank_env_file(tmp_path):
    env_path = tmp_path / ".env"
    env_path.write_text("OPENAI_API_KEY=\n", encoding="utf-8")
    assert "está vazia" in missing_api_key_message(env_path)


def test_multi_agent_e2e_multi_scenario():
    config = load_config(EXAMPLE_MULTI, apply_env=False)
    fake = FakeRunner(coordinator=True, coordinator_id="coordenador-b")
    result, progress = run_fake(config, fake)
    assert result.status == "completed"
    assert result.completed_tasks == ["T1", "T2"]
    assert result.agent_models == {
        "principal": "gpt-5.6-luna",
        "coordenador-b": "gpt-5.6-luna",
        "release-a": "gpt-5.6-luna",
        "release-b": "gpt-5.6-luna",
    }
    assert "revisão" in progress
    assert "start:coordenador-b" in fake.events


def test_budget_refund_on_worker_retry():
    data = config_data()
    data["execution"]["max_model_calls"] = 6
    data["execution"]["max_retries_per_task"] = 1
    data["execution"]["worker_max_turns"] = 4
    config = SwarmConfig.model_validate(data)
    fake = FakeRunner(fail_attempts={"release-b": 1})
    result, _ = run_fake(config, fake)
    assert result.status == "completed"
    assert result.completed_tasks == ["T1", "T2"]
    assert result.usage.model_calls == 5


def test_budget_refund_on_runner_exception():
    data = config_data()
    data["execution"]["max_model_calls"] = 6
    data["execution"]["on_worker_failure"] = "partial"
    config = SwarmConfig.model_validate(data)
    fake = FakeRunner(raise_on={"release-b"})
    result, _ = run_fake(config, fake)
    assert result.status == "partial"
    assert "T1" in result.completed_tasks
    assert "T2" in result.incomplete_tasks
    assert result.usage.model_calls == 3


def test_secrets_never_appear_in_artifact(monkeypatch):
    secret_key = "sk-proj-supersecretkey1234567890abcdef"
    monkeypatch.setenv("OPENAI_API_KEY", secret_key)
    config = load_config(EXAMPLE, apply_env=False)
    fake = FakeRunner(leak_secret=secret_key)
    result, _ = run_fake(config, fake)
    assert secret_key not in result.answer
    assert "[REDACTED_KEY]" in result.answer
    for ev in result.evidence:
        assert secret_key not in ev
        assert "[REDACTED_KEY]" in ev


def test_cli_full_flow_produces_valid_json_file(tmp_path, monkeypatch):
    from swarm_oneshot import cli

    out_file = tmp_path / "artifacts" / "cli-result.json"
    fake = FakeRunner()

    class PatchedSwarm(Swarm):
        def __init__(self, config, *, base_dir, progress=None):
            super().__init__(config, base_dir=base_dir, runner=fake, progress=progress)

    monkeypatch.setenv("OPENAI_API_KEY", "test-key-mock")
    monkeypatch.setattr(cli, "Swarm", PatchedSwarm)
    monkeypatch.setattr(
        "sys.argv",
        ["swarm-oneshot", "run", "--config", str(EXAMPLE), "--output", str(out_file), "--no-env-overrides"],
    )
    code = cli.main()
    assert code == 0
    assert out_file.is_file()
    payload = json.loads(out_file.read_text(encoding="utf-8"))
    assert payload["run_id"] == "e2e-release-notes"
    assert payload["status"] == "completed"
    assert payload["completed_tasks"] == ["T1", "T2"]
    assert payload["usage"]["model_calls"] > 0
    assert payload["agent_models"]["principal"] == "gpt-5.6-luna"


def test_cli_validate_command_succeeds(monkeypatch, capsys):
    from swarm_oneshot import cli

    monkeypatch.setattr(
        "sys.argv",
        ["swarm-oneshot", "validate", "--config", str(EXAMPLE), "--no-env-overrides"],
    )
    code = cli.main()
    assert code == 0
    captured = capsys.readouterr()
    assert "Configuração válida" in captured.out


def test_cli_fails_on_missing_config_or_output(tmp_path, monkeypatch):
    from swarm_oneshot import cli

    monkeypatch.chdir(tmp_path)
    monkeypatch.delenv("SWARM_CONFIG", raising=False)
    monkeypatch.delenv("SWARM_OUTPUT", raising=False)
    monkeypatch.setattr("sys.argv", ["swarm-oneshot", "validate"])
    assert cli.main() == 2

    monkeypatch.setattr("sys.argv", ["swarm-oneshot", "run", "--config", str(EXAMPLE)])
    assert cli.main() == 2


def test_subprocess_cli_handles_errors():
    import subprocess
    import sys

    proc = subprocess.run(
        [sys.executable, "-m", "swarm_oneshot", "run", "--config", "nonexistent.yaml", "--output", "out.json"],
        capture_output=True,
        text=True,
    )
    assert proc.returncode == 2
    assert "Configuração inválida" in proc.stderr
