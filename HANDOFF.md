# Handoff — Swarm one-shot

Data: 2026-09-26 (Sessão atualizada às 22:30)
Estado: robusto, 100% testado (unitários, integração e E2E reais)

## Configuração ativa de modelos (.env)

- **Primary**: `gpt-5.6-sol` (responsável pelo plano inicial e síntese final);
- **Coordenadores**: `gpt-5.6-sol` (orientação pré-voo e revisão das frentes);
- **Workers**: `gpt-5.6-luna` (execução das tarefas e leitura de artefatos);
- **Allowed models**: `gpt-5.6-sol,gpt-5.6-luna`.

## Entrega atual

O projeto implementa uma execução one-shot de agentes no OpenAI Agents SDK, com:

- agente principal que cria o plano e sintetiza a resposta;
- coordenadores por frente de trabalho (com orientação pré-voo e revisão de critérios);
- workers parametrizados por YAML e `.env`;
- dependências entre tarefas, concorrência limitada e retries;
- barras de progresso por fase;
- contratos estritos com Pydantic;
- leitura de arquivos estritamente restrita aos artefatos declarados;
- sanitização ativa de segredos (`sk-...`, chaves do `.env`) em todos os artefatos de saída;
- gestão resiliente de orçamento de chamadas (`try/finally` e reembolso adequado de turnos em retries/falhas);
- artefato JSON final e trace agrupado por `run_id`.

## Evidências de execução real (OpenAI API)

Todos os cenários reais foram executados e validados:

1. **Auditoria real do repositório** (`audit_repo.yaml`):
   - `status: completed`, 3 tarefas concluídas, 13 chamadas de modelo;
   - Artefato: `artifacts/auditoria.json`;
   - Trace: `auditoria-swarm-local`.

2. **Cenário E2E simples** (`examples/e2e.yaml`):
   - `status: completed`, 2 tarefas concluídas, 4 chamadas de modelo;
   - Artefato: `artifacts/e2e-result.json`.

3. **Cenário E2E multi-agente** (`examples/e2e_multi.yaml`):
   - `status: completed`, 2 tarefas concluídas, 6 chamadas de modelo (com coordenador);
   - Artefato: `artifacts/e2e-multi-result.json`.

## Verificações locais

Executadas com 100% de sucesso:

```sh
venv/bin/python -m pytest -v        # 25 passed
venv/bin/python -m swarm_oneshot validate
venv/bin/python -m swarm_oneshot validate --config examples/e2e.yaml --no-env-overrides
venv/bin/python -m swarm_oneshot validate --config examples/e2e_multi.yaml --no-env-overrides
venv/bin/python -m swarm_oneshot validate --config audit_repo.yaml --no-env-overrides
venv/bin/python scripts/e2e.py      # Ambos os cenários aprovados
git diff --check
```

## Como retomar

1. Confirmar `OPENAI_API_KEY` no `.env` local.
2. Validar uma configuração:

   ```sh
   venv/bin/python -m swarm_oneshot validate --config audit_repo.yaml --no-env-overrides
   ```

3. Executar o swarm:

   ```sh
   venv/bin/python -m swarm_oneshot run \
     --config audit_repo.yaml \
     --output artifacts/auditoria.json \
     --no-env-overrides
   ```

4. Executar a suíte completa de testes:

   ```sh
   venv/bin/python -m pytest -q
   ```

5. Executar os cenários E2E reais:

   ```sh
   venv/bin/python scripts/e2e.py
   ```

## Arquivos principais

- `SPEC.md`: arquitetura e contratos.
- `IMPLEMENTATION_PLAN.md`: plano de implementação.
- `TEST_PLAN_E2E.md`: critérios E2E.
- `src/swarm_oneshot/orchestrator.py`: ciclo de planejamento, execução, revisão, síntese e gestão de orçamento.
- `src/swarm_oneshot/sanitize.py`: sanitização e proteção contra vazamento de segredos em artefatos.
- `src/swarm_oneshot/cli.py`: ponto de entrada da CLI, tratamento de erros e escrita segura.
- `src/swarm_oneshot/env_config.py`: carregamento do `.env` e overrides.
- `src/swarm_oneshot/runner.py`: adaptador do Agents SDK.
- `tests/test_swarm.py`: 25 testes cobrindo orquestração, multi-agente, orçamento, segredos, CLI e subprocesso.

## Melhorias implementadas nesta sessão

Todas as 5 melhorias apontadas na auditoria anterior foram concluídas:

1. **Cenário multi-agente `e2e_multi.yaml`**: testado offline no `pytest` e executado com sucesso na API real da OpenAI.
2. **Fluxo completo CLI → JSON**: testes de ponta a ponta validando exit codes, criação de diretórios e integridade do JSON gerado.
3. **Proteção de segredos**: módulo `sanitize.py` integrado à geração do `FinalResult`, redigindo chaves e tokens de padrão `sk-...`.
4. **Tratamento de falhas de subprocesso e I/O**: `cli.py` e `scripts/e2e.py` verificam existência do arquivo de saída e reportam erros de subprocesso.
5. **Reembolso do orçamento de chamadas**: `_call` com `try/finally` garantindo que `refund` sempre seja executado em falhas, cancelamentos e retries de workers.
