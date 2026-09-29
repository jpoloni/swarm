# Handoff — Swarm one-shot

Data: 2026-09-29 (Encerramento da Sessão)
Estado: robusto, 100% testado (unitários, integração e E2E reais), repositório público sincronizado no GitHub

## Repositório Remoto e Segurança
- **Repositório GitHub (Público)**: [https://github.com/jpoloni/swarm](https://github.com/jpoloni/swarm)
- **Remote**: `origin` (`git@github.com:jpoloni/swarm.git`)
- **Branch**: `main` (up to date)
- **Auditoria de Segredos**: 100% limpo — `.env` e `artifacts/` ignorados pelo `.gitignore`, zero chaves reais no histórico e zero alertas no GitHub Secret Scanning (`gh api repos/jpoloni/swarm/secret-scanning/alerts` -> `[]`).

## Configuração ativa de modelos (.env)

- **Primary**: `gpt-5.6-sol` (responsável pelo plano inicial e síntese final);
- **Coordenadores**: `gpt-5.6-sol` (orientação pré-voo e revisão das frentes);
- **Workers (Oficial)**: `gpt-5.6-terra` (execução das tarefas analíticas e leitura de artefatos);
- **Allowed models**: `gpt-5.6-sol,gpt-5.6-luna,gpt-5.6-terra`.

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

1. **Hospitais Cordilheira S.A. — Pacote PEEA 2027 + Medidas Q4/2026** (`examples/hospitais_cordilheira/`):
   - **Workers GPT 5.6 Terra (Oficial)**: `status: completed`, 13 chamadas, 100% cego. **Nota Oficial: 98,0 / 100,0** (zero reprovação sumária nos Gates C1, C2 e C3). Elaborou parecer técnico independente para o Conselho de Administração cumprindo rigorosamente os 8 itens mandatórios do DOC-00 (catálogo de afirmações [Cxx], decisões ancoradas, afirmações sem consequência, tabela de alocação por fonte/destino, cronograma físico trimestral em sala-dias, registro de riscos com dono/gatilho, contestação individual de premissas P1 a P8 com 12,5/12,5 pts e apêndice de cálculos com fórmulas no formato `conta = resultado`). Deliberou pela aprovação imediata da requalificação de gases em out/2026 com NR-13 para evitar multa de R$ 180k/dia da ACP 0042.2025; aprovação do reforço Radlin no Q4/2026 via alçada de emergência (Art. 9º PO-12) para salvar a habilitação de alta complexidade da radioterapia e R$ 11,8 MM de margem; rejeição de F1 pelo método convencional e adoção do método alternativo E-77 para manter 10 salas operacionais e honrar Cláusula 7.2 do contrato Omega; rejeição de F4 pela ausência de CMMS; prorrogação de 12 meses da Geomed até 30/12/2026; e repactuação de banda de gases até 01/12/2026. Artefatos: `artifacts/hospitais_cordilheira_blind_terra_result.json` e `artifacts/hospitais_cordilheira_parecer.md`.

2. **PetroHorizonte TIC — Governança de Orçamento (REO-2025-0142)** (`examples/tic_orcamento/`):
   - **Workers GPT 5.6 Terra (Oficial)**: `status: completed`, 10 chamadas, 37.0s. Execução 100% cega: auditoria de MUST-01 a MUST-07, veredito de 3 Cumpridos, 3 GAPs e 1 Pendente, identificou violação de change freeze no aditivo NébulaOps, ausência de rebaseline para overrun de 11% da linha cloud e corrigiu a classificação preliminar indevida de N/A para o despacho de contingência. Artefato: `artifacts/tic_orcamento_blind_terra_result.json`.

3. **PetroHorizonte TIC — IA Responsável (RIO-2025-IA-0087)** (`examples/tic_ia_responsavel/`):
   - **Workers GPT 5.6 Terra (Oficial)**: `status: completed`, 10 chamadas, 41.5s. Execução 100% cega: corpus higienizado sem gabarito, auditoria exata de MUST-01 a MUST-07, veredito fundamentado de não conformidade para encerramento (gaps em HITL MUST-02, rollback fora do prazo de 6h MUST-04, linhagem parcial/tardia MUST-05 e due diligence vencida MUST-07), com plano mandatório de remediação. Artefato: `artifacts/tic_ia_responsavel_blind_terra_result.json`.

4. **Rede Leste Transmissão S.A. — Rede Sentinela (Comitê Extraordinário de Carteira 2027)** (`examples/rede_sentinela/`):
   - **Workers GPT 5.6 Terra (Oficial)**: `status: completed`, 10 chamadas, 72.8s. Execução 100% cega: atendeu integralmente MUST-01 a MUST-10, acertou 9/9 deliberações de frentes (F1, F2, F6, F7, F9 aprovadas; F4, F8 diferidas; F3 e F5 rejeitadas), 8/8 premissas P1 a P8 (P1-P5 refutadas, P6-P8 sustentadas), reconstituição da equação paramétrica do GridStore (24,24 anos de payback real vs 3,69 prometidos, take-or-pay de R$ 144 MM e multa de R$ 85,8 MM), identificação do retorno de R$ 36 MM de Linha Norte II ao CAPEX (totalizando R$ 456 MM) e reconciliação dos 22 bay-dias autorizados pelo ONS. Artefato: `artifacts/sentinela_blind_terra_result.json`.

5. **Porto Limiar — TPL (Comitê de Carteira 2027)** (`examples/porto_limiar/`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 10 chamadas, 61.1s. Reconstituiu a fórmula paramétrica do payback de F5 (TurnGate) provando 24,5 anos reais (vs 3,4 anos prometidos), reconciliação do fluxo de CAPEX (R$ 178 MM com baixa de Armazém Norte) e OPEX compulsório de F2/F9. Artefato: `artifacts/porto_limiar_blind_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 14 chamadas, 51.9s. 100% cego, 9/9 deliberações de frentes coincidentes com o gabarito. Artefato: `artifacts/porto_limiar_blind_result.json`.

6. **Governança Portuária — Terminais Cordilheira S.A.** (`examples/terminais_cordilheira/`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 13 chamadas, 88.7s. Nota estimada **~87,5/100**. Encontrou o cancelamento do PEC-114 (+R$ 9,6 MM de CAPEX, totalizando R$ 13,8 MM), a exigência de SFCE da norma NE-31 (R$ 3,1 MM CAPEX + R$ 0,58 MM/ano) e a fórmula exata da recuperação de caução (`1,95 × 2,10 × (1 - 0,22) ≈ 3,2 MM`). Artefato: `artifacts/terminais_cordilheira_blind_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 13 chamadas, 58.9s. Nota estimada **78,5/100**, superando com folga todos os gates sumários (C1, C2 e C3) e gabaritando as premissas P1–P8. Artefato: `artifacts/terminais_cordilheira_blind_result.json`.

7. **Governança de TIC — Aurora Energia** (`examples/aurora/`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 10 chamadas, 45.9s. Execução 100% cega: sem nenhuma dica no YAML, atendeu rigorosamente MUST-01 a MUST-10, isolou o déficit de R$ 4,0 MM em F6, diagnosticou o viés do piloto no Aurora-12, a sobreposição do SaaS paralelo de R$ 3,2 MM e determinou os donos e gatilhos de escalonamento. Artefato: `artifacts/aurora_blind_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 11 chamadas, 42.1s. 100% de aderência ao gabarito oficial. Artefato: `artifacts/aurora_decisao_comite_otimizada.json`.

8. **Due Diligence Contratual B2B SaaS** (`examples/contract_audit.yaml`):
   - **Workers GPT 5.6 Terra**: `status: completed`, 13 chamadas, 40.0s. Execução 100% cega: sem qualquer menção prévia a números de cláusulas, mapeou e fundamentou autonomamente todas as cláusulas (2.1-2.4, 3.1-3.3, 4.1-4.3, 5.2-5.4 e 7.1), calculou o lock-in de R$ 900.000,00 e converteu a assimetria de SLA de 95% em 36h/mês de indisponibilidade. Artefato: `artifacts/contract_audit_blind_terra_result.json`.
   - **Workers GPT 5.6 Luna**: `status: completed`, 11 chamadas, 37.5s. Matriz de riscos e contra-redações. Artefato: `artifacts/due_diligence_contrato.json`.

9. **Auditoria real do repositório** (`audit_repo.yaml`):
   - `status: completed`, 3 tarefas concluídas, 13 chamadas de modelo;
   - Artefato: `artifacts/auditoria.json`;
   - Trace: `auditoria-swarm-local`.

10. **Cenário E2E simples** (`examples/e2e.yaml`):
   - `status: completed`, 2 tarefas concluídas, 4 chamadas de modelo;
   - Artefato: `artifacts/e2e-result.json`.

10. **Cenário E2E multi-agente** (`examples/e2e_multi.yaml`):
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
