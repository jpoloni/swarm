"""Narrow adapter around OpenAI Agents SDK for production and fake tests."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass
class AgentRun:
    output: Any
    model_calls: int


class OpenAIAgentRunner:
    async def run(
        self,
        *,
        agent_id: str,
        model: str,
        instructions: str,
        prompt: str,
        output_type: type,
        tools: list[Any],
        max_turns: int,
    ) -> AgentRun:
        from agents import Agent, RunConfig, Runner

        agent = Agent(
            name=agent_id,
            model=model,
            instructions=instructions,
            tools=tools,
            output_type=output_type,
        )
        result = await Runner.run(
            agent,
            prompt,
            max_turns=max_turns,
            run_config=RunConfig(trace_include_sensitive_data=False),
        )
        output = result.final_output
        if not isinstance(output, output_type):
            output = output_type.model_validate(output)
        return AgentRun(output=output, model_calls=result.context_wrapper.usage.requests)
