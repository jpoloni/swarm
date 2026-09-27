"""Apply optional environment overrides to a YAML swarm configuration."""

from __future__ import annotations

import os
from copy import deepcopy
from pathlib import Path
from typing import Any

from dotenv import dotenv_values, load_dotenv


def load_project_env(path: Path) -> None:
    """Load .env while preserving nonempty shell values over file values."""
    load_dotenv(path, override=False)
    if not (os.environ.get("OPENAI_API_KEY") or "").strip() and path.is_file():
        key = (dotenv_values(path).get("OPENAI_API_KEY") or "").strip()
        if key:
            os.environ["OPENAI_API_KEY"] = key


def missing_api_key_message(path: Path) -> str:
    if path.is_file():
        values = dotenv_values(path)
        if "OPENAI_API_KEY" in values:
            return f"OPENAI_API_KEY está vazia em {path}. Preencha a linha OPENAI_API_KEY=... e execute novamente."
        return f"OPENAI_API_KEY não foi definida em {path} nem no ambiente."
    return f"Arquivo {path} não encontrado e OPENAI_API_KEY ausente no ambiente."


def _value(name: str) -> str | None:
    value = os.environ.get(name, "").strip()
    return value or None


def _models(name: str, count: int) -> list[str] | None:
    raw = _value(name)
    if raw is None:
        return None
    values = [part.strip() for part in raw.split(",")]
    if not all(values):
        raise ValueError(f"{name} contém modelo vazio")
    if len(values) == 1:
        return values * count
    if len(values) != count:
        raise ValueError(f"{name} requer 1 ou {count} modelos")
    return values


def _count(name: str, current: int) -> int:
    raw = _value(name)
    if raw is None:
        return current
    try:
        count = int(raw)
    except ValueError as exc:
        raise ValueError(f"{name} deve ser inteiro") from exc
    if count < 1:
        raise ValueError(f"{name} deve ser maior que zero")
    return count


def _next_id(prefix: str, used: set[str]) -> str:
    number = 1
    while f"{prefix}-{number}" in used:
        number += 1
    value = f"{prefix}-{number}"
    used.add(value)
    return value


def apply_env_overrides(source: dict[str, Any]) -> dict[str, Any]:
    """Resize agent slots and override models/limits with SWARM_* values."""
    data = deepcopy(source)
    orch = data["orchestrators"]
    workers = data["workers"]
    primary = next((agent for agent in orch["agents"] if agent["role"] == "primary"), None)
    if primary is None:
        raise ValueError("YAML sem orquestrador primary")
    existing_coordinators = [agent for agent in orch["agents"] if agent["role"] == "coordinator"]
    existing_workers = workers["agents"]
    orch_count = _count("SWARM_ORCHESTRATOR_COUNT", orch["count"])
    worker_count = _count("SWARM_WORKER_COUNT", workers["count"])
    used_ids = {agent["id"] for agent in orch["agents"] + existing_workers}

    selected_coordinators = deepcopy(existing_coordinators[:orch_count - 1])
    while len(selected_coordinators) < orch_count - 1:
        selected_coordinators.append({
            "id": _next_id("coordenador", used_ids),
            "role": "coordinator",
            "model": primary["model"],
            "instructions": "Coordene uma frente independente e revise as evidências.",
        })
    selected_workers = deepcopy(existing_workers[:worker_count])
    while len(selected_workers) < worker_count:
        selected_workers.append({
            "id": _next_id("worker", used_ids),
            "specialty": "Investigue uma parte independente do objetivo com evidências.",
            "model": primary["model"],
            "tools": [],
        })

    primary = deepcopy(primary)
    if model := _value("SWARM_PRIMARY_MODEL"):
        primary["model"] = model
    for agents, env_name in ((selected_coordinators, "SWARM_COORDINATOR_MODELS"), (selected_workers, "SWARM_WORKER_MODELS")):
        values = _models(env_name, len(agents))
        if values:
            for agent, model in zip(agents, values):
                agent["model"] = model
    orch["count"] = orch_count
    orch["agents"] = [primary] + selected_coordinators
    workers["count"] = worker_count
    workers["agents"] = selected_workers

    for env_name, field in (("SWARM_RUN_ID", "run_id"), ("SWARM_OBJECTIVE", "objective")):
        if value := _value(env_name):
            data[field] = value
    for env_name, field in (
        ("SWARM_MAX_PARALLEL_WORKERS", "max_parallel_workers"),
        ("SWARM_MAX_MODEL_CALLS", "max_model_calls"),
        ("SWARM_WORKER_MAX_TURNS", "worker_max_turns"),
        ("SWARM_TIMEOUT_SECONDS", "timeout_seconds"),
        ("SWARM_WORKER_TIMEOUT_SECONDS", "worker_timeout_seconds"),
        ("SWARM_MAX_RETRIES_PER_TASK", "max_retries_per_task"),
        ("SWARM_ON_WORKER_FAILURE", "on_worker_failure"),
    ):
        if value := _value(env_name):
            data["execution"][field] = value
    if raw := _value("SWARM_ALLOWED_MODELS"):
        values = [part.strip() for part in raw.split(",")]
        if not all(values):
            raise ValueError("SWARM_ALLOWED_MODELS contém modelo vazio")
        data["execution"]["allowed_models"] = values
    return data
