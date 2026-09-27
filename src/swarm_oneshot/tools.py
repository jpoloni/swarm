"""Read-only tools available to configured workers."""

from __future__ import annotations

from pathlib import Path
from typing import Any


def resolve_allowed_path(base_dir: Path, artifacts: list[str], value: str) -> Path:
    """Resolve one explicitly declared artifact inside the configuration directory."""
    root = base_dir.resolve()
    path = (root / value).resolve()
    declared = {(root / artifact).resolve() for artifact in artifacts}
    if not path.is_relative_to(root):
        raise ValueError("caminho fora do diretório da configuração")
    if path not in declared:
        raise ValueError("arquivo não declarado em context.artifacts")
    if not path.is_file():
        raise ValueError("arquivo não encontrado")
    if path.stat().st_size > 200_000:
        raise ValueError("arquivo excede 200 KB")
    return path


def build_tools(names: list[str], base_dir: Path, artifacts: list[str]) -> list[Any]:
    # Import here so validation and dry-run work without loading the SDK.
    from agents import function_tool

    tools: list[Any] = []
    if "document_search" in names:
        import re

        @function_tool
        def document_search(query: str) -> str:
            """Search text artifacts declared in the run configuration with exact and keyword matching."""
            needle = query.casefold().strip()
            if not needle:
                return "Consulta vazia."

            # 1. Busca exata por substring
            exact_hits: list[str] = []
            for artifact in artifacts:
                path = resolve_allowed_path(base_dir, artifacts, artifact)
                for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    if needle in line.casefold():
                        exact_hits.append(f"{artifact}:{number}: {line[:400]}")
                        if len(exact_hits) >= 12:
                            break
                if len(exact_hits) >= 12:
                    break

            if exact_hits:
                return "\n".join(exact_hits)

            # 2. Busca tolerante por palavras-chave (tokens com 3+ caracteres)
            tokens = [t for t in re.findall(r"\w+", needle) if len(t) >= 3]
            if not tokens:
                return "Nenhum resultado."

            scored_hits: list[tuple[int, int, str]] = []
            global_idx = 0
            for artifact in artifacts:
                path = resolve_allowed_path(base_dir, artifacts, artifact)
                for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
                    global_idx += 1
                    line_lower = line.casefold()
                    matched = sum(1 for t in tokens if t in line_lower)
                    if matched > 0:
                        scored_hits.append((matched, -global_idx, f"{artifact}:{number}: {line[:400]}"))

            if not scored_hits:
                return "Nenhum resultado."

            # Ordena por maior contagem de termos casados
            scored_hits.sort(key=lambda item: item[0], reverse=True)
            top_score = scored_hits[0][0]
            # Retorna até 12 resultados relevantes
            selected = [hit[2] for hit in scored_hits[:12] if hit[0] >= min(top_score, 1)]
            return "\n".join(selected) if selected else "Nenhum resultado."

        tools.append(document_search)

    if "repository_read" in names:
        @function_tool
        def repository_read(path: str) -> str:
            """Read a declared UTF-8 artifact with path and line numbers."""
            source = resolve_allowed_path(base_dir, artifacts, path)
            numbered = (f"{path}:{number}: {line}" for number, line in enumerate(source.read_text(encoding="utf-8").splitlines(), 1))
            return "\n".join(numbered)[:12_000]

        tools.append(repository_read)

    if "code_structure_inspect" in names:
        import ast

        @function_tool
        def code_structure_inspect(path: str) -> str:
            """Inspect Python code structure (classes, functions, imports) in a declared artifact."""
            source_path = resolve_allowed_path(base_dir, artifacts, path)
            if not source_path.name.endswith(".py"):
                return f"{path}: apenas arquivos .py são suportados por esta ferramenta."
            text = source_path.read_text(encoding="utf-8")
            try:
                tree = ast.parse(text, filename=path)
            except SyntaxError as err:
                return f"{path}: erro de sintaxe na linha {err.lineno}: {err.msg}"

            lines: list[str] = [f"Estrutura de {path}:"]
            for node in tree.body:
                if isinstance(node, ast.ClassDef):
                    methods = [n.name for n in node.body if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]
                    lines.append(f"  linha {node.lineno}: class {node.name} (métodos: {', '.join(methods) or 'nenhum'})")
                elif isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    prefix = "async def" if isinstance(node, ast.AsyncFunctionDef) else "def"
                    args = [a.arg for a in node.args.args]
                    lines.append(f"  linha {node.lineno}: {prefix} {node.name}({', '.join(args)})")
                elif isinstance(node, ast.Import):
                    names_str = ", ".join(alias.name for alias in node.names)
                    lines.append(f"  linha {node.lineno}: import {names_str}")
                elif isinstance(node, ast.ImportFrom):
                    names_str = ", ".join(alias.name for alias in node.names)
                    lines.append(f"  linha {node.lineno}: from {node.module or ''} import {names_str}")
            return "\n".join(lines) if len(lines) > 1 else f"{path}: nenhum símbolo de alto nível encontrado."

        tools.append(code_structure_inspect)

    return tools
