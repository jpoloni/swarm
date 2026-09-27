"""Application-owned one-shot orchestration over Agents SDK runs."""

from __future__ import annotations

import asyncio
import json
import time
from pathlib import Path
from typing import Any

from .models import (
    FinalResult, Plan, ReviewResult, SwarmConfig, Synthesis, Task, TrackGuidance,
    UsageReport, WorkerResult,
)
from .progress import Progress
from .runner import OpenAIAgentRunner
from .sanitize import sanitize_result
from .tools import build_tools
from .validation import PlanError, validate_plan


class BudgetError(RuntimeError):
    pass


class CallBudget:
    def __init__(self, limit: int) -> None:
        self.limit = limit
        self.used = 0
        self._lock = asyncio.Lock()

    async def reserve(self, turns: int, *, final: bool = False) -> int:
        async with self._lock:
            available = self.limit - self.used - (0 if final else 1)
            if available < 1:
                raise BudgetError("orçamento de chamadas esgotado")
            granted = min(turns, available)
            self.used += granted
            return granted

    async def refund(self, reserved: int, actual: int) -> None:
        async with self._lock:
            self.used -= max(reserved - max(actual, 0), 0)


def payload(value: Any) -> str:
    if hasattr(value, "model_dump"):
        value = value.model_dump()
    return json.dumps(value, ensure_ascii=False)


class Swarm:
    def __init__(
        self,
        config: SwarmConfig,
        *,
        base_dir: Path,
        runner: Any | None = None,
        progress: Progress | None = None,
    ) -> None:
        self.config = config
        self.base_dir = base_dir
        self.runner = runner or OpenAIAgentRunner()
        self.progress = progress or Progress()
        self.budget = CallBudget(config.execution.max_model_calls)
        self.plan: Plan | None = None
        self.completed: dict[str, WorkerResult] = {}
        self.failed: dict[str, str] = {}
        self.reviews: dict[str, ReviewResult] = {}
        self.guidance: dict[str, TrackGuidance] = {}
        self.agent_models: dict[str, str] = {}
        self.limitations: list[str] = []
        self.started = 0.0

    async def run(self) -> FinalResult:
        self.started = time.monotonic()
        self.progress.set("planejamento", 0, 1)
        self.progress.set("coordenação", 0, max(self.config.orchestrators.count - 1, 1))
        self.progress.set("workers", 0, self.config.workers.count)
        self.progress.set("revisão", 0, max(self.config.orchestrators.count - 1, 1))
        self.progress.set("síntese", 0, 1)
        try:
            async with asyncio.timeout(self.config.execution.timeout_seconds):
                if isinstance(self.runner, OpenAIAgentRunner):
                    from agents import trace

                    with trace("swarm-one-shot", group_id=self.config.run_id):
                        return await self._run_inner()
                return await self._run_inner()
        except TimeoutError:
            self.limitations.append("Tempo global esgotado.")
            return self._fallback("failed")
        except (BudgetError, PlanError, ValueError) as exc:
            self.limitations.append(str(exc))
            return self._fallback("rejected" if self.plan is None else "failed")
        except Exception as exc:
            self.limitations.append(f"Falha de execução: {type(exc).__name__}: {exc}")
            return self._fallback("failed")

    async def _run_inner(self) -> FinalResult:
        primary = self.config.primary
        prompt = payload({
            "objective": self.config.objective,
            "context": self.config.context.model_dump(),
            "orchestrators": [{"id": a.id, "role": a.role, "instructions": a.instructions} for a in self.config.orchestrators.agents],
            "workers": [{"id": a.id, "specialty": a.specialty, "tools": a.tools} for a in self.config.workers.agents],
            "rules": "Crie pelo menos uma tarefa útil por worker. Atribua ao menos uma frente a cada coordenador. Use apenas IDs fornecidos. Defina dependências somente quando necessárias.",
        })
        plan = await self._call(
            primary.id, primary.model,
            primary.instructions + " Produza um plano estruturado. Não execute tarefas dos workers.",
            prompt, Plan, [], 1,
        )
        validate_plan(self.config, plan)
        self.plan = plan
        self.progress.set("planejamento", 1, 1)
        self.progress.set("workers", 0, len(plan.tasks))
        await self._prepare_tracks(plan)
        await self._execute_tasks(plan)
        await self._review_tracks(plan)
        return await self._synthesize()

    async def _call(
        self, agent_id: str, model: str, instructions: str,
        prompt: str, output_type: type, tools: list[Any], turns: int,
        *, final: bool = False,
    ) -> Any:
        reserved = await self.budget.reserve(turns, final=final)
        self.agent_models[agent_id] = model
        calls_made = 0
        try:
            result = await self.runner.run(
                agent_id=agent_id, model=model, instructions=instructions,
                prompt=prompt, output_type=output_type, tools=tools,
                max_turns=reserved,
            )
            calls_made = getattr(result, "model_calls", 1)
            return result.output
        finally:
            await self.budget.refund(reserved, calls_made)

    async def _prepare_tracks(self, plan: Plan) -> None:
        coordinators = {a.id: a for a in self.config.orchestrators.agents if a.role == "coordinator"}
        assigned = [track for track in plan.tracks if track.orchestrator_id in coordinators]
        if not assigned:
            self.progress.set("coordenação", 1, 1)
            return
        for number, track in enumerate(assigned, 1):
            coordinator = coordinators[track.orchestrator_id]
            tasks = [task for task in plan.tasks if task.track_id == track.id]
            guidance: TrackGuidance = await self._call(
                coordinator.id, coordinator.model,
                coordinator.instructions + " Oriente os workers desta frente antes da execução. Nesta etapa, avalie apenas escopo e viabilidade das tarefas: ainda não há achados para citar ou revisar. Se as tarefas forem viáveis, aprove a frente e peça aos workers as evidências necessárias. Não rejeite a frente por ausência de evidências que serão produzidas pelos workers.",
                payload({"objective": self.config.objective, "context": self.config.context.model_dump(), "track": track.model_dump(), "tasks": [task.model_dump() for task in tasks], "stage": "preparação antes da execução dos workers"}),
                TrackGuidance, [], 1,
            )
            task_ids = {task.id for task in tasks}
            instruction_ids = [item.task_id for item in guidance.task_instructions]
            if guidance.track_id != track.id or not set(instruction_ids).issubset(task_ids) or len(instruction_ids) != len(set(instruction_ids)):
                raise PlanError(f"orientação inválida para a frente {track.id}")
            if not guidance.approved:
                self.limitations.append(f"Orientação da frente {track.id} não aprovada: {'; '.join(guidance.issues) or 'sem justificativa'}")
            else:
                self.guidance[track.id] = guidance
            self.progress.set("coordenação", number, len(assigned))

    async def _execute_tasks(self, plan: Plan) -> None:
        pending = {task.id: task for task in plan.tasks}
        worker_specs = {worker.id: worker for worker in self.config.workers.agents}
        locks = {worker_id: asyncio.Lock() for worker_id in worker_specs}
        semaphore = asyncio.Semaphore(self.config.execution.max_parallel_workers)
        finished = 0

        async def execute(task: Task) -> tuple[str, WorkerResult | None, str | None]:
            worker = worker_specs[task.worker_id]
            async with semaphore, locks[worker.id]:
                prior = {dep: self.completed[dep].model_dump() for dep in task.depends_on}
                prompt = payload({
                    "objective": self.config.objective,
                    "context": self.config.context.model_dump(),
                    "task": task.model_dump(),
                    "coordinator_guidance": next((item.instruction for item in self.guidance[task.track_id].task_instructions if item.task_id == task.id), "") if task.track_id in self.guidance else "",
                    "dependencies": prior,
                    "rule": "Entregue apenas fatos sustentados pelos dados disponíveis. Use o task_id recebido. Se não puder concluir, status=failed e descreva a lacuna.",
                })
                tools = build_tools(worker.tools, self.base_dir, self.config.context.artifacts) if worker.tools else []
                turns = self.config.execution.worker_max_turns if tools else 1
                last_error = "falha desconhecida"
                for attempt in range(self.config.execution.max_retries_per_task + 1):
                    try:
                        async with asyncio.timeout(self.config.execution.worker_timeout_seconds):
                            result: WorkerResult = await self._call(
                                worker.id, worker.model, worker.specialty,
                                prompt, WorkerResult, tools, turns,
                            )
                        if result.task_id != task.id:
                            raise ValueError("worker devolveu task_id incorreto")
                        if result.status != "completed":
                            raise ValueError("; ".join(result.errors) or "worker não concluiu")
                        if self.config.output.require_evidence and (
                            not result.findings or any(not finding.evidence.strip() for finding in result.findings)
                        ):
                            raise ValueError("resultado sem evidências")
                        return task.id, result, None
                    except Exception as exc:
                        last_error = f"tentativa {attempt + 1}: {type(exc).__name__}: {exc}"
                        if isinstance(exc, BudgetError):
                            break
                return task.id, None, last_error

        while pending:
            blocked = [task_id for task_id, task in pending.items() if any(dep in self.failed for dep in task.depends_on)]
            for task_id in blocked:
                self.failed[task_id] = "dependência não concluída"
                del pending[task_id]
                finished += 1
                self.progress.set("workers", finished, len(plan.tasks))
            ready = [task for task in pending.values() if all(dep in self.completed for dep in task.depends_on)]
            if not ready:
                if pending:
                    raise PlanError("plano sem tarefas executáveis")
                break
            results = await asyncio.gather(*(execute(task) for task in ready))
            for task_id, output, error in results:
                del pending[task_id]
                if output is None:
                    self.failed[task_id] = error or "falha desconhecida"
                else:
                    self.completed[task_id] = output
                finished += 1
                self.progress.set("workers", finished, len(plan.tasks))

    async def _review_tracks(self, plan: Plan) -> None:
        coordinators = {a.id: a for a in self.config.orchestrators.agents if a.role == "coordinator"}
        assigned = [track for track in plan.tracks if track.orchestrator_id in coordinators]
        if not assigned:
            self.progress.set("revisão", 1, 1)
            return
        done = 0
        for track in assigned:
            coordinator = coordinators[track.orchestrator_id]
            task_ids = [task.id for task in plan.tasks if task.track_id == track.id]
            prompt = payload({
                "objective": self.config.objective,
                "track": track.model_dump(),
                "task_results": {task_id: self.completed[task_id].model_dump() for task_id in task_ids if task_id in self.completed},
                "failed_tasks": {task_id: self.failed[task_id] for task_id in task_ids if task_id in self.failed},
                "rule": "Aceite apenas tarefas concluídas e sustentadas por evidência. Devolva track_id e IDs exatos.",
            })
            try:
                review: ReviewResult = await self._call(
                    coordinator.id, coordinator.model, coordinator.instructions,
                    prompt, ReviewResult, [], 1,
                )
                if review.track_id != track.id or not set(review.accepted_task_ids).issubset(set(task_ids)):
                    raise ValueError("revisão com IDs inválidos")
                self.reviews[track.id] = review
                for task_id in task_ids:
                    if task_id in self.completed and task_id not in review.accepted_task_ids:
                        del self.completed[task_id]
                        self.failed[task_id] = "não aceito na revisão"
                self.limitations.extend(review.issues)
            except Exception as exc:
                self.limitations.append(f"Revisão {track.id}: {type(exc).__name__}: {exc}")
                for task_id in task_ids:
                    if task_id in self.completed:
                        del self.completed[task_id]
                        self.failed[task_id] = "revisão não concluída"
            done += 1
            self.progress.set("revisão", done, len(assigned))

    async def _synthesize(self) -> FinalResult:
        assert self.plan is not None
        primary = self.config.primary
        status = self._status()
        prompt = payload({
            "objective": self.config.objective,
            "language": self.config.output.language,
            "status": status,
            "completed": {task_id: result.model_dump() for task_id, result in self.completed.items()},
            "incomplete": self.failed,
            "reviews": {track_id: review.model_dump() for track_id, review in self.reviews.items()},
            "rule": "Sintetize somente resultados verificados. Descreva explicitamente as lacunas. Responda em markdown.",
        })
        try:
            synthesis: Synthesis = await self._call(
                primary.id, primary.model, primary.instructions,
                prompt, Synthesis, [], 1, final=True,
            )
            self.progress.set("síntese", 1, 1)
            return self._result(status, synthesis.answer, synthesis.evidence, synthesis.limitations)
        except Exception as exc:
            self.limitations.append(f"Síntese: {type(exc).__name__}: {exc}")
            return self._fallback("failed")

    def _status(self) -> str:
        if not self.failed:
            return "completed"
        if self.config.execution.on_worker_failure == "partial" and self.completed:
            return "partial"
        return "failed"

    def _fallback(self, status: str) -> FinalResult:
        if self.plan:
            for task in self.plan.tasks:
                if task.id not in self.completed and task.id not in self.failed:
                    self.failed[task.id] = "execução interrompida"
        answer = "Execução encerrada sem síntese completa."
        if self.completed:
            answer += " Resultados verificados: " + "; ".join(
                finding.claim for result in self.completed.values() for finding in result.findings
            )
        return self._result(status, answer, [], [])

    def _result(self, status: str, answer: str, evidence: list[str], limitations: list[str]) -> FinalResult:
        result = FinalResult(
            run_id=self.config.run_id,
            status=status,
            answer=answer,
            completed_tasks=sorted(self.completed),
            incomplete_tasks=sorted(self.failed),
            evidence=evidence,
            limitations=self.limitations + limitations + [f"{task_id}: {error}" for task_id, error in sorted(self.failed.items())],
            usage=UsageReport(model_calls=self.budget.used, elapsed_seconds=round(time.monotonic() - self.started, 3)),
            agent_models=self.agent_models,
            trace_ref=self.config.run_id if isinstance(self.runner, OpenAIAgentRunner) else None,
        )
        return sanitize_result(result)
