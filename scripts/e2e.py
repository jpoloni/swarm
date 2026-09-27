"""Run a small real-API acceptance case once OPENAI_API_KEY is provided."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from swarm_oneshot.env_config import load_project_env, missing_api_key_message


ROOT = Path(__file__).resolve().parents[1]
CASES = [
    (ROOT / "examples" / "e2e.yaml", ROOT / "artifacts" / "e2e-result.json", "e2e-release-notes", {"principal", "release-a", "release-b"}),
    (ROOT / "examples" / "e2e_multi.yaml", ROOT / "artifacts" / "e2e-multi-result.json", "e2e-release-notes-multi", {"principal", "coordenador-b", "release-a", "release-b"}),
]


def main() -> int:
    env_path = ROOT / ".env"
    load_project_env(env_path)
    if not (os.environ.get("OPENAI_API_KEY") or "").strip():
        print(missing_api_key_message(env_path), file=sys.stderr)
        return 2
    for config, output, run_id, agents in CASES:
        process = subprocess.run(
            [sys.executable, "-m", "swarm_oneshot", "run", "--config", str(config), "--output", str(output), "--no-env-overrides"],
            cwd=ROOT,
            check=False,
        )
        if process.returncode:
            print(f"Execução falhou para {config.name} com código {process.returncode}", file=sys.stderr)
            return process.returncode
        if not output.is_file():
            print(f"Arquivo de saída esperado não foi gerado: {output}", file=sys.stderr)
            return 1
        content = output.read_text(encoding="utf-8")
        data = json.loads(content)
        assert data["run_id"] == run_id, data
        assert data["status"] == "completed", data
        assert len(data["completed_tasks"]) >= 2, data
        assert not data["incomplete_tasks"], data
        assert data["answer"].strip(), data
        assert data["evidence"], data
        assert data["usage"]["model_calls"] > 0, data
        assert set(data["agent_models"]) == agents, data
        assert os.environ["OPENAI_API_KEY"] not in content
        print(f"E2E aprovado: {config.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
