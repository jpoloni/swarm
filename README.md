# Swarm one-shot

Aplicação CLI para executar um objetivo específico com orquestradores e workers configuráveis no OpenAI Agents SDK. A [spec](SPEC.md), o [plano de implementação](IMPLEMENTATION_PLAN.md), o [plano E2E](TEST_PLAN_E2E.md), o [progresso](PROGRESS.md) e o [handoff](HANDOFF.md) documentam os contratos, critérios de aceite e estado.

## Instalação

```sh
python3 -m venv venv
venv/bin/python -m pip install -e '.[dev]'
```

## Validar sem chave

```sh
venv/bin/python -m swarm_oneshot validate
venv/bin/python -m swarm_oneshot validate --config examples/e2e.yaml --no-env-overrides
venv/bin/python -m pytest
```

O primeiro comando lê `.env` e usa `SWARM_CONFIG`. Ajuste `SWARM_ORCHESTRATOR_COUNT`, `SWARM_WORKER_COUNT`, `SWARM_PRIMARY_MODEL`, `SWARM_COORDINATOR_MODELS` e `SWARM_WORKER_MODELS` nesse arquivo. Um modelo único em cada lista vale para todos do grupo; para modelos individuais, separe os IDs por vírgula. Ao aumentar a contagem acima dos agentes definidos no YAML, a aplicação cria slots genéricos; para especialidades específicas, defina esses agentes no YAML.

## Executar com chave

Preencha `OPENAI_API_KEY` no `.env` local e execute:

```sh
venv/bin/python -m swarm_oneshot run
venv/bin/python scripts/e2e.py
```

O primeiro comando aplica os parâmetros do `.env` ao objetivo apontado por `SWARM_CONFIG`. O E2E usa a chave do `.env`, mas executa os dois cenários fixos sem overrides de agentes para manter os critérios de aceite reproduzíveis.

Para uma configuração própria:

```sh
venv/bin/python -m swarm_oneshot run --config minha-config.yaml --output artifacts/resultado.json
```

## Caso real: auditoria deste projeto

O arquivo [audit_repo.yaml](audit_repo.yaml) usa três workers para revisar configuração, orquestração e testes do próprio código, com um coordenador responsável pela frente de qualidade. As ferramentas só podem ler os arquivos declarados em `context.artifacts`; `.env` não está nessa lista. A resposta deve citar caminho e linha para cada achado.

```sh
venv/bin/python -m swarm_oneshot validate --config audit_repo.yaml --no-env-overrides
venv/bin/python -m swarm_oneshot run --config audit_repo.yaml --output artifacts/auditoria.json --no-env-overrides
```

O segundo comando usa a chave do `.env` e faz chamadas reais à API. O resultado fica em `artifacts/auditoria.json`.
Nesta auditoria, `worker_max_turns: 6` permite várias leituras de arquivos por worker; `max_model_calls: 32` limita o orçamento total. Um worker que exceder os turnos ou não concluir aparece em `incomplete_tasks` e pode produzir `status: partial` quando outras tarefas terminam.

A CLI imprime barras por fase em `stderr` e grava o contrato final em JSON. O exemplo usa `gpt-5.6-luna`; ajuste os modelos do `.env` e `SWARM_ALLOWED_MODELS` caso sua conta use outros IDs. `allowed_models` é um catálogo local opcional, não uma consulta de disponibilidade da API. Variáveis exportadas no shell têm prioridade sobre o `.env`.

## Estrutura

- `src/swarm_oneshot/models.py`: configuração e contratos Pydantic.
- `src/swarm_oneshot/validation.py`: validação determinística do plano.
- `src/swarm_oneshot/orchestrator.py`: agendamento, orçamento, revisão e síntese.
- `src/swarm_oneshot/runner.py`: integração com o Agents SDK.
- `src/swarm_oneshot/tools.py`: ferramentas de leitura restritas aos artefatos declarados.
- `scripts/e2e.py`: verificação real da API, condicionada à chave.

O fluxo não guarda memória entre execuções. O `run_id` agrupa traces e resultados, mas não retoma uma conversa anterior.
