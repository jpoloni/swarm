"""Read-only tools available to configured workers."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def build_tools(names: list[str], base_dir: Path, artifacts: list[str]) -> list[Any]:
    # Import here so validation and dry-run work without loading the SDK.
    from agents import function_tool

    tools: list[Any] = []
    root = base_dir.resolve()

    def safe_path(value: str) -> Path:
        path = (root / value).resolve()
        if not path.is_relative_to(root):
            raise ValueError("caminho fora do diretório da configuração")
        if not path.is_file():
            raise ValueError("arquivo não encontrado")
        if path.stat().st_size > 200_000:
            raise ValueError("arquivo excede 200 KB")
        return path

    if "document_search" in names:
        @function_tool
        def document_search(query: str) -> str:
            """Search text artifacts declared in the run configuration."""
            needle = query.casefold().strip()
            if not needle:
                return "Consulta vazia."
            hits: list[str] = []
            for artifact in artifacts:
                path = safe_path(artifact)
                for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    if needle in line.casefold():
                        hits.append(f"{artifact}:{number}: {line[:400]}")
                    if len(hits) >= 12:
                        break
                if len(hits) >= 12:
                    break
            return "\n".join(hits) if hits else "Nenhum resultado."

        tools.append(document_search)

    if "repository_read" in names:
        @function_tool
        def repository_read(path: str) -> str:
            """Read a UTF-8 file inside the configuration directory."""
            return safe_path(path).read_text(encoding="utf-8")[:12_000]

        tools.append(repository_read)

    return tools
