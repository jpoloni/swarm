"""Deterministic checks for plans proposed by the primary agent."""

from __future__ import annotations

from .models import Plan, SwarmConfig


class PlanError(ValueError):
    pass


def validate_plan(config: SwarmConfig, plan: Plan) -> None:
    if not plan.tracks or not plan.tasks:
        raise PlanError("plano sem frentes ou tarefas")
    track_ids = [track.id for track in plan.tracks]
    task_ids = [task.id for task in plan.tasks]
    if len(track_ids) != len(set(track_ids)) or len(task_ids) != len(set(task_ids)):
        raise PlanError("IDs de frentes e tarefas devem ser únicos")

    orchestrators = {agent.id for agent in config.orchestrators.agents}
    workers = {agent.id for agent in config.workers.agents}
    if any(track.orchestrator_id not in orchestrators for track in plan.tracks):
        raise PlanError("frente atribuída a orquestrador desconhecido")
    assigned_orchestrators = {track.orchestrator_id for track in plan.tracks}
    if not {a.id for a in config.orchestrators.agents if a.role == "coordinator"}.issubset(assigned_orchestrators):
        raise PlanError("orquestrador auxiliar sem frente")
    if any(task.track_id not in track_ids or task.worker_id not in workers for task in plan.tasks):
        raise PlanError("tarefa com frente ou worker desconhecido")
    if {task.worker_id for task in plan.tasks} != workers:
        raise PlanError("cada worker configurado precisa receber ao menos uma tarefa útil")
    if any(not task.goal.strip() or not task.acceptance.strip() for task in plan.tasks):
        raise PlanError("tarefa sem objetivo ou critério de aceite")
    if any(track.id not in {task.track_id for task in plan.tasks} for track in plan.tracks):
        raise PlanError("frente sem tarefa")
    dependencies = {task.id: task.depends_on for task in plan.tasks}
    for task_id, predecessors in dependencies.items():
        if len(predecessors) != len(set(predecessors)):
            raise PlanError(f"dependência repetida em {task_id}")
        if any(predecessor not in dependencies or predecessor == task_id for predecessor in predecessors):
            raise PlanError(f"dependência inválida em {task_id}")
    visiting: set[str] = set()
    visited: set[str] = set()

    def visit(task_id: str) -> None:
        if task_id in visiting:
            raise PlanError("ciclo de dependências no plano")
        if task_id in visited:
            return
        visiting.add(task_id)
        for predecessor in dependencies[task_id]:
            visit(predecessor)
        visiting.remove(task_id)
        visited.add(task_id)

    for task_id in dependencies:
        visit(task_id)
