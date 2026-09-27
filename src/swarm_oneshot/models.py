"""Configuration and structured contracts for a single swarm execution."""

from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class StrictModel(BaseModel):
    model_config = ConfigDict(extra="forbid")


class ContextSpec(StrictModel):
    text: str = ""
    artifacts: list[str] = Field(default_factory=list)


class OrchestratorSpec(StrictModel):
    id: str = Field(min_length=1)
    role: Literal["primary", "coordinator"]
    model: str = Field(min_length=1)
    instructions: str = Field(min_length=1)


class WorkerSpec(StrictModel):
    id: str = Field(min_length=1)
    specialty: str = Field(min_length=1)
    model: str = Field(min_length=1)
    tools: list[Literal["document_search", "repository_read", "code_structure_inspect"]] = Field(default_factory=list)


class OrchestratorTeam(StrictModel):
    count: int = Field(ge=1)
    agents: list[OrchestratorSpec]


class WorkerTeam(StrictModel):
    count: int = Field(ge=1)
    agents: list[WorkerSpec]


class ExecutionSpec(StrictModel):
    max_parallel_workers: int = Field(ge=1)
    max_model_calls: int = Field(ge=3)
    worker_max_turns: int = Field(default=3, ge=1)
    timeout_seconds: float = Field(gt=0)
    worker_timeout_seconds: float = Field(gt=0)
    max_retries_per_task: int = Field(ge=0, le=3)
    on_worker_failure: Literal["partial", "fail"]
    allowed_models: list[str] | None = None


class OutputSpec(StrictModel):
    language: str = "pt-BR"
    format: Literal["markdown"] = "markdown"
    require_evidence: bool = True


class SwarmConfig(StrictModel):
    schema_version: Literal["1"]
    run_id: str = Field(min_length=1)
    objective: str = Field(min_length=1)
    context: ContextSpec = Field(default_factory=ContextSpec)
    orchestrators: OrchestratorTeam
    workers: WorkerTeam
    execution: ExecutionSpec
    output: OutputSpec = Field(default_factory=OutputSpec)

    @model_validator(mode="after")
    def validate_teams(self) -> SwarmConfig:
        if self.orchestrators.count != len(self.orchestrators.agents):
            raise ValueError("orchestrators.count não corresponde à lista de agentes")
        if self.workers.count != len(self.workers.agents):
            raise ValueError("workers.count não corresponde à lista de agentes")
        if sum(a.role == "primary" for a in self.orchestrators.agents) != 1:
            raise ValueError("deve existir exatamente um orquestrador primary")
        ids = [a.id for a in self.orchestrators.agents] + [a.id for a in self.workers.agents]
        if len(ids) != len(set(ids)):
            raise ValueError("IDs de agentes devem ser únicos")
        if self.execution.max_parallel_workers > self.workers.count:
            raise ValueError("max_parallel_workers excede workers.count")
        if self.execution.worker_timeout_seconds > self.execution.timeout_seconds:
            raise ValueError("worker_timeout_seconds excede timeout_seconds")
        allowed = self.execution.allowed_models
        if allowed is not None:
            if not allowed:
                raise ValueError("allowed_models não pode ser vazio")
            unavailable = {a.model for a in self.orchestrators.agents + self.workers.agents} - set(allowed)
            if unavailable:
                raise ValueError(f"modelos fora do catálogo: {sorted(unavailable)}")
        return self

    @property
    def primary(self) -> OrchestratorSpec:
        return next(a for a in self.orchestrators.agents if a.role == "primary")


class Track(StrictModel):
    id: str
    orchestrator_id: str


class Task(StrictModel):
    id: str
    track_id: str
    worker_id: str
    goal: str
    inputs: list[str] = Field(default_factory=list)
    depends_on: list[str] = Field(default_factory=list)
    acceptance: str


class Plan(StrictModel):
    tracks: list[Track]
    tasks: list[Task]


class Finding(StrictModel):
    claim: str
    evidence: str
    impact: str


class WorkerResult(StrictModel):
    task_id: str
    status: Literal["completed", "failed"]
    findings: list[Finding] = Field(default_factory=list)
    artifacts: list[str] = Field(default_factory=list)
    open_questions: list[str] = Field(default_factory=list)
    errors: list[str] = Field(default_factory=list)


class TaskInstruction(StrictModel):
    task_id: str
    instruction: str


class TrackGuidance(StrictModel):
    track_id: str
    approved: bool
    task_instructions: list[TaskInstruction] = Field(default_factory=list)
    issues: list[str] = Field(default_factory=list)


class ReviewResult(StrictModel):
    track_id: str
    accepted_task_ids: list[str]
    issues: list[str] = Field(default_factory=list)
    summary: str


class Synthesis(StrictModel):
    answer: str
    evidence: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)


class UsageReport(StrictModel):
    model_calls: int = 0
    elapsed_seconds: float = 0


class FinalResult(StrictModel):
    run_id: str
    status: Literal["completed", "partial", "failed", "rejected"]
    answer: str
    completed_tasks: list[str] = Field(default_factory=list)
    incomplete_tasks: list[str] = Field(default_factory=list)
    evidence: list[str] = Field(default_factory=list)
    limitations: list[str] = Field(default_factory=list)
    usage: UsageReport = Field(default_factory=UsageReport)
    agent_models: dict[str, str] = Field(default_factory=dict)
    trace_ref: str | None = None
