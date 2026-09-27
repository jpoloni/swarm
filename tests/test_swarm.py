from __future__ import annotations

import asyncio
import io
import json
from pathlib import Path

import pytest
from pydantic import ValidationError

from swarm_oneshot.cli import load_config
from swarm_oneshot.env_config import apply_env_overrides
from swarm_oneshot.models import (
    Finding, Plan, ReviewResult, SwarmConfig, Synthesis, Task, TaskInstruction, Track, TrackGuidance, WorkerResult,
)
from swarm_oneshot.orchestrator import Swarm
from swarm_oneshot.progress import Progress
from swarm_oneshot.runner import AgentRun
from swarm_oneshot.validation import PlanError, validate_plan


EXAMPLE = Path(__file__).resolve().parents[1] / "examples" / "e2e.yaml"


def config_data() -> dict:
    import yaml

    return yaml.safe_load(EXAMPLE.read_text(encoding="utf-8"))


class FakeRunner:
    def __init__(self, *, dependent: bool = False, fail_worker: str | None = None, coordinator: bool = False) -> None:
        self.dependent = dependent
        self.fail_worker = fail_worker
        self.coordinator = coordinator
        self.active_workers = 0
        self.max_active_workers = 0
        self.events: list[str] = []

    async def run(self, *, agent_id, model, instructions, prompt, output_type, tools, max_turns):
        data = json.loads(prompt)
        self.events.append(f"start:{agent_id}")
        if output_type is Plan:
            if self.coordinator:
                tracks = [Track(id="a", orchestrator_id="principal"), Track(id="b", orchestrator_id="coordenador")]
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
            output = WorkerResult(
                task_id=task["id"],
                status="failed" if agent_id == self.fail_worker else "completed",
                findings=[] if agent_id == self.fail_worker else [Finding(claim=task["goal"], evidence="nota de versão", impact="ação")],
                errors=["falha simulada"] if agent_id == self.fail_worker else [],
            )
        elif output_type is ReviewResult:
            output = ReviewResult(track_id=data["track"]["id"], accepted_task_ids=list(data["task_results"]), summary="Revisado")
        elif output_type is TrackGuidance:
            output = TrackGuidance(track_id=data["track"]["id"], approved=True, task_instructions=[TaskInstruction(task_id=task["id"], instruction="Use a evidência fornecida.") for task in data["tasks"]])
        elif output_type is Synthesis:
            output = Synthesis(answer="Resumo verificado", evidence=["notas A e B"])
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


def test_worker_failure_produces_partial_when_allowed():
    data = config_data()
    data["execution"]["on_worker_failure"] = "partial"
    config = SwarmConfig.model_validate(data)
    result, _ = run_fake(config, FakeRunner(fail_worker="release-b"))
    assert result.status == "partial"
    assert result.completed_tasks == ["T1"]
    assert result.incomplete_tasks == ["T2"]
    assert "T2" in " ".join(result.limitations)


def test_missing_key_exits_before_api_call(monkeypatch):
    from swarm_oneshot import cli

    monkeypatch.delenv("OPENAI_API_KEY", raising=False)
    monkeypatch.setattr("sys.argv", ["swarm-oneshot", "run", "--config", str(EXAMPLE), "--output", "/tmp/no-output.json"])
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
