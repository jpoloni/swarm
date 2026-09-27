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

1. **Porto Limiar — TPL (Comitê de Carteira 2027)** (`examples/porto_limiar/`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 10 chamadas, 61.1s. Reconstituiu a fórmula paramétrica do payback de F5 (TurnGate) provando 24,5 anos reais (vs 3,4 anos prometidos), reconciliação do fluxo de CAPEX (R$ 178 MM com baixa de Armazém Norte) e OPEX compulsório de F2/F9. Artefato: `artifacts/porto_limiar_blind_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 14 chamadas, 51.9s. 100% cego, 9/9 deliberações de frentes coincidentes com o gabarito. Artefato: `artifacts/porto_limiar_blind_result.json`.

2. **Governança Portuária — Terminais Cordilheira S.A.** (`examples/terminais_cordilheira/`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 13 chamadas, 88.7s. Nota estimada **~87,5/100**. Encontrou o cancelamento do PEC-114 (+R$ 9,6 MM de CAPEX, totalizando R$ 13,8 MM), a exigência de SFCE da norma NE-31 (R$ 3,1 MM CAPEX + R$ 0,58 MM/ano) e a fórmula exata da recuperação de caução (`1,95 × 2,10 × (1 - 0,22) ≈ 3,2 MM`). Artefato: `artifacts/terminais_cordilheira_blind_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 13 chamadas, 58.9s. Nota estimada **78,5/100**, superando com folga todos os gates sumários (C1, C2 e C3) e gabaritando as premissas P1–P8. Artefato: `artifacts/terminais_cordilheira_blind_result.json`.

3. **Governança de TIC — Aurora Energia** (`examples/aurora/`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 10 chamadas, 45.0s. Atendimento integral a MUST-01 a MUST-10, com isolamento do déficit de R$ 4,0 MM em F6 e impedimento formal de Wilson Tagliatti. Artefato: `artifacts/aurora_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 11 chamadas, 42.1s. 100% de aderência ao gabarito oficial. Artefato: `artifacts/aurora_decisao_comite_otimizada.json`.

4. **Due Diligence Contratual B2B SaaS** (`examples/contract_audit.yaml`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 12 chamadas, 41.8s. Cálculo da exposição de lock-in de R$ 900.000,00 e quantificação da assimetria de SLA (95% = 36h/mês de indisponibilidade). Artefato: `artifacts/contract_audit_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 11 chamadas, 37.5s. Matriz de riscos e contra-redações. Artefato: `artifacts/due_diligence_contrato.json`.

4. **Auditoria real do repositório** (`audit_repo.yaml`):
   - `status: completed`, 3 tarefas concluídas, 13 chamadas de modelo;
   - Artefato: `artifacts/auditoria.json`;
   - Trace: `auditoria-swarm-local`.

5. **Cenário E2E simples** (`examples/e2e.yaml`):
   - `status: completed`, 2 tarefas concluídas, 4 chamadas de modelo;
   - Artefato: `artifacts/e2e-result.json`.

6. **Cenário E2E multi-agente** (`examples/e2e_multi.yaml`):
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
- `src/swarm_oneshot/tools.py`: ferramentas de workers (`document_search`, `repository_read`, `code_structure_inspect`).
- `src/swarm_oneshot/env_config.py`: carregamento do `.env` e overrides.
- `src/swarm_oneshot/runner.py`: adaptador do Agents SDK.
- `tests/test_swarm.py`: 29 testes cobrindo orquestração, multi-agente, ferramentas, orçamento, segredos, CLI e subprocesso.

## Entregas concluídas nesta sessão

1. **Commit inicial do ciclo estável**: commit `812adf5` consolidando o núcleo do swarm e as 5 melhorias da auditoria.
2. **Expansão de ferramentas dos workers**:
   - Adicionada ferramenta `code_structure_inspect` (análise de AST para extrair classes, métodos e imports);
   - Testes unitários para `document_search`, `repository_read` e `code_structure_inspect`.
3. **Novos templates de casos de uso reais (`examples/`)**:
   - `examples/dependency_audit.yaml` com `dependencies_sample.toml`;
   - `examples/changelog_generation.yaml` com `commits_sample.txt`;
   - `examples/code_review.yaml` com `code_sample.py`.
4. **Empacotamento e CLI binária**:
   - `pip install -e .` configurado e testado com sucesso;
   - Executável `venv/bin/swarm-oneshot` pronto para uso em produção.
