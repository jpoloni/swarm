"""Sanitization utilities to ensure sensitive credentials never leak into output artifacts."""

from __future__ import annotations

import os
import re
from typing import Any

from .models import FinalResult

OPENAI_KEY_PATTERN = re.compile(r"sk-(?:proj-)?[A-Za-z0-9_-]{20,}")


def sanitize_text(text: str, additional_secrets: list[str] | None = None) -> str:
    """Scrub sensitive credentials (e.g. OpenAI API keys) from text."""
    if not text:
        return text
    env_key = (os.environ.get("OPENAI_API_KEY") or "").strip()
    if env_key and len(env_key) >= 6:
        text = text.replace(env_key, "[REDACTED_KEY]")
    if additional_secrets:
        for secret in additional_secrets:
            clean = secret.strip()
            if clean and len(clean) >= 6:
                text = text.replace(clean, "[REDACTED_SECRET]")
    text = OPENAI_KEY_PATTERN.sub("[REDACTED_KEY]", text)
    return text


def sanitize_result(result: FinalResult, additional_secrets: list[str] | None = None) -> FinalResult:
    """Return a sanitized copy of FinalResult with all sensitive strings redacted."""
    secrets = list(additional_secrets or [])
    return FinalResult(
        run_id=result.run_id,
        status=result.status,
        answer=sanitize_text(result.answer, secrets),
        completed_tasks=result.completed_tasks,
        incomplete_tasks=result.incomplete_tasks,
        evidence=[sanitize_text(e, secrets) for e in result.evidence],
        limitations=[sanitize_text(l, secrets) for l in result.limitations],
        usage=result.usage,
        agent_models=result.agent_models,
        trace_ref=sanitize_text(result.trace_ref, secrets) if result.trace_ref else None,
    )
