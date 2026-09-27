"""Run a small real-API acceptance case once OPENAI_API_KEY is provided."""

from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

from dotenv import load_dotenv


ROOT = Path(__file__).resolve().parents[1]
CASES = [
    (ROOT / "examples" / "e2e.yaml", ROOT / "artifacts" / "e2e-result.json", "e2e-release-notes", {"principal", "release-a", "release-b"}),
    (ROOT / "examples" / "e2e_multi.yaml", ROOT / "artifacts" / "e2e-multi-result.json", "e2e-release-notes-multi", {"principal", "coordenador-b", "release-a", "release-b"}),
]


def main() -> int:
    load_dotenv(ROOT / ".env", override=False)
    if not os.environ.get("OPENAI_API_KEY"):
        print("Aguardando OPENAI_API_KEY. Nenhuma chamada à API foi feita.", file=sys.stderr)
        return 2
    for config, output, run_id, agents in CASES:
        process = subprocess.run(
            [sys.executable, "-m", "swarm_oneshot", "run", "--config", str(config), "--output", str(output), "--no-env-overrides"],
            cwd=ROOT,
            check=False,
        )
        if process.returncode:
            return process.returncode
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
