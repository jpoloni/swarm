"""Command line entry point for validation and one-shot runs."""

from __future__ import annotations

import argparse
import asyncio
import json
import os
import sys
from pathlib import Path

import yaml
from dotenv import load_dotenv
from pydantic import ValidationError

from .env_config import apply_env_overrides
from .models import SwarmConfig
from .orchestrator import Swarm
from .progress import Progress


def load_config(path: Path, *, apply_env: bool = False) -> SwarmConfig:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError("configuração YAML deve ser um objeto")
    if apply_env:
        data = apply_env_overrides(data)
    config = SwarmConfig.model_validate(data)
    root = path.parent.resolve()
    for artifact in config.context.artifacts:
        resolved = (root / artifact).resolve()
        if not resolved.is_relative_to(root) or not resolved.is_file():
            raise ValueError(f"artefato inválido: {artifact}")
    return config


def main() -> int:
    load_dotenv(Path.cwd() / ".env", override=False)
    parser = argparse.ArgumentParser(prog="swarm-oneshot")
    sub = parser.add_subparsers(dest="command", required=True)
    validate = sub.add_parser("validate", help="validar configuração sem chamar a API")
    validate.add_argument("--config", type=Path)
    validate.add_argument("--no-env-overrides", action="store_true")
    run = sub.add_parser("run", help="executar swarm one-shot")
    run.add_argument("--config", type=Path)
    run.add_argument("--output", type=Path)
    run.add_argument("--no-env-overrides", action="store_true")
    args = parser.parse_args()
    try:
        config_path = args.config or (Path(value) if (value := os.environ.get("SWARM_CONFIG")) else None)
        if config_path is None:
            raise ValueError("informe --config ou SWARM_CONFIG no .env")
        config = load_config(config_path, apply_env=not args.no_env_overrides)
        output_path = None
        if args.command == "run":
            output_path = args.output or (Path(value) if (value := os.environ.get("SWARM_OUTPUT")) else None)
            if output_path is None:
                raise ValueError("informe --output ou SWARM_OUTPUT no .env")
        width_raw = os.environ.get("SWARM_PROGRESS_WIDTH", "20")
        width = int(width_raw)
        if not 1 <= width <= 80:
            raise ValueError("SWARM_PROGRESS_WIDTH deve estar entre 1 e 80")
    except (OSError, ValueError, ValidationError, yaml.YAMLError) as exc:
        print(f"Configuração inválida: {exc}", file=sys.stderr)
        return 2
    if args.command == "validate":
        print(f"Configuração válida: {config.run_id} · {config.orchestrators.count} orquestrador(es) · {config.workers.count} worker(s)")
        return 0
    if not os.environ.get("OPENAI_API_KEY"):
        print("OPENAI_API_KEY ausente. Defina a variável para executar o teste com a API.", file=sys.stderr)
        return 2
    result = asyncio.run(Swarm(config, base_dir=config_path.parent, progress=Progress(width=width)).run())
    assert output_path is not None
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(result.model_dump(), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Resultado: {output_path} · status={result.status} · chamadas={result.usage.model_calls}")
    return 0 if result.status == "completed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
