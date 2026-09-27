# Glossário operacional — corpus IA Responsável (PetroHorizonte)

Documento de apoio ao corpus fechado de calibração. Termos alinhados à POL-TIC-IA-2025-04 e ao RIO-2025-IA-0087.

| Termo | Significado operacional neste corpus |
|---|---|
| **Alto impacto** | Recomendação cuja execução pode implicar parada de trem, mobilização emergencial ou intervenção não programada acima do limiar LIM-IA-OPS-01; dispara MUST-02 (HITL). |
| **Baseline** | Conjunto de métricas e distribuição de features aprovadas na model card no momento da promoção. |
| **CMMS** | Sistema de gestão de manutenção; no incidente, destino das ordens INT-EMERG-331/332. |
| **Confirmação** | Momento em que o evento de modelo é registrado como confirmado no RIO; dispara prazos de MUST-04 e MUST-05. |
| **Drift** | Desvio de features ou de performance em relação à baseline; monitor `drift-predcomp-prod` no caso PH-PREDCOMP. |
| **Due diligence (vendor)** | Avaliação periódica (≤12 meses) de componente/modelo de fornecedor; MUST-07. |
| **Feature** | Variável de entrada do modelo (ex.: `psi_descarga_norm`, `rms_vib_eixo_b`). |
| **HITL** | Human-in-the-loop — aprovação humana registrada antes de executar ação de alto impacto (MUST-02). |
| **Inventário de modelos** | Repositório `inv-modelos-ia` com owner, versão, impacto e link da model card (MUST-01). |
| **Linhagem de features** | Rastreio de origem, janela e transformações dos dados de treino/retreino (MUST-05). |
| **Model card** | Ficha técnica versionada do modelo (objetivo, métricas, limitações, owner, data de promoção). |
| **Owner do modelo** | Responsável nomeado pela conformidade contínua; no RIO-2025-IA-0087: R. Campos / PH-44821. |
| **PH-PREDCOMP** | Série do modelo preditivo de manutenção de trens de compressão da PetroHorizonte S.A. |
| **Rollback** | Retorno à última versão estável ou desabilitação de recomendações automatizadas após drift (MUST-04). |
| **RIO** | Registro de Incidentes Operacionais — dossiê formal do evento de modelo. |
| **TC-PH7-A** | Tag interna fictícia do trem de compressão na Unidade Marítima Horizonte-7. |
