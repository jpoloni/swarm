# Registro de Incidente Operacional (RIO) — Modelo de IA em Produção
## RIO-2025-IA-0087 | Severidade: Alta | Status: Contido — em encerramento de governança

**Organização:** PetroHorizonte S.A. — Diretoria de TIC e Digital  
**Modelo afetado:** PH-PREDCOMP-v2.4 (preditiva de manutenção — trens de compressão)  
**Ativo / tag operacional:** Trem TC-PH7-A, Unidade Marítima Horizonte-7 (código interno; não corresponde a campo real)  
**Data/hora da detecção (monitor de drift):** 18/06/2025, 10:30 (America/Sao_Paulo)  
**Data/hora da confirmação (RIO):** 18/06/2025, 11:15  
**Área detentora:** MLOps Operacional — TIC/Digital  
**Owner do modelo (inventário):** R. Campos, matrícula PH-44821  
**Responsável pelo registro:** L. Ferreira (plantão MLOps)

---

## 1. Resumo executivo

Em 18/06/2025, após campanha de recalibração de sensores de pressão e vibração no Trem TC-PH7-A, o monitor de drift do modelo **PH-PREDCOMP-v2.4** emitiu alerta de severidade **Alta** (desvio de distribuição nas features `psi_descarga_norm` e `rms_vib_eixo_b` em relação à baseline da model card MC-PREDCOMP-2.4).

Entre 09:05 e 12:40 do mesmo dia, o modelo emitiu **14 recomendações** classificadas como alto impacto (classe `Critica — intervenção não programada`), das quais **2** foram convertidas em ordens de intervenção emergencial no CMMS interno sem registro de aprovação HITL recuperável neste RIO.

A emissão automatizada foi desabilitada às 17:50 do dia **19/06/2025** (rollback para PH-PREDCOMP-v2.3 concluído nesse horário). Não houve lesão pessoal nem vazamento ambiental; houve custo de mobilização e perda parcial de disponibilidade do trem no intervalo das intervenções.

## 2. Linha do tempo

| Horário (BRT) | Evento |
|---|---|
| 17/06/2025 22:00 | Conclusão da campanha de recalibração de sensores no TC-PH7-A (OS-MANUT-7741) |
| 18/06/2025 09:05 | Primeira recomendação `Critica` emitida por PH-PREDCOMP-v2.4 para TC-PH7-A |
| 18/06/2025 09:40 | Ordem CMMS INT-EMERG-331 criada a partir do painel preditivo (sem campo HITL preenchido) |
| 18/06/2025 10:12 | Segunda ordem CMMS INT-EMERG-332 criada nas mesmas condições |
| 18/06/2025 10:30 | Alerta de drift severidade Alta no monitor `drift-predcomp-prod` |
| 18/06/2025 11:15 | Confirmação registrada neste RIO; owner R. Campos acionado |
| 18/06/2025 14:00 | Reunião tática TIC + Confiabilidade; decisão verbal de “acompanhar até fim do turno” |
| 19/06/2025 09:20 | Parecer de Segurança Operacional solicitando desabilitar recomendações automatizadas |
| 19/06/2025 17:50 | Rollback concluído: produção aponta para PH-PREDCOMP-v2.3; auto-recomendação v2.4 desabilitada |
| 20/06/2025 11:00 | Extração de logs de recomendação do intervalo 18–19/06 anexada (LOG-PREDCOMP-0618) |

## 3. Inventário e model card

- **Inventário `inv-modelos-ia`:** entrada `PH-PREDCOMP` versão `2.4`, finalidade “preditiva de falha em trens de compressão — Polo Atlântico Sul (interno)”, impacto **Alto**, owner **R. Campos / PH-44821**, promoção em **02/05/2025**, link MC-PREDCOMP-2.4.
- **Model card MC-PREDCOMP-2.4:** arquivada em `model-cards/predcomp/2.4.md` com métricas de baseline (recall classe Critica ≥ 0,82 no holdout interno) e limitações explícitas quanto a mudança de calibração de sensores.

Citação estável: “owner R. Campos, matrícula PH-44821” consta do inventário na data da confirmação deste RIO.

## 4. Gate pré-produção (versão 2.4)

O dossiê de promoção PROMO-PREDCOMP-2.4, datado de **28/04/2025**, contém: métricas de desempenho na baseline; análise de falso positivo/negativo para classe Critica; e parecer de liberação assinado pelo owner e por Engenharia de Confiabilidade (assinatura digital EC-882).

A data do gate é anterior à promoção de 02/05/2025. Evidência anexada: PROMO-PREDCOMP-2.4.pdf (hash interno omitido neste RIO).

## 5. Recomendações, HITL e logging

Conforme LOG-PREDCOMP-0618:

1. Foram registradas **14 recomendações** automatizadas com timestamp, versão `PH-PREDCOMP-v2.4`, tag `TC-PH7-A`, classe/escore e flag de consumo por workflow.
2. As ordens **INT-EMERG-331** e **INT-EMERG-332** constam como “consumidas por workflow CMMS”.
3. O campo obrigatório de aprovação HITL (aprovador, matrícula, decisão) **não está preenchido** para INT-EMERG-331 nem para INT-EMERG-332. A coordenação de manutenção registrou apenas: “ação tomada com base no painel preditivo, alinhamento verbal no rádio de turno”.

Não há, neste RIO, identificador de aprovador HITL citável para as duas intervenções de alto impacto.

Retenção do log: repositório `logs-ia/predcomp/` com política de retenção configurada para **2 anos**.

## 6. Drift, confirmação e rollback

- **Detecção:** 18/06/2025, 10:30 — alerta Alta em `drift-predcomp-prod`.
- **Confirmação RIO:** 18/06/2025, 11:15.
- **Prazo MUST de ação (rollback ou desabilitar auto-recomendação):** 6 horas após confirmação → limite **18/06/2025, 17:15**.
- **Ação efetiva:** rollback / desabilitação concluídos em **19/06/2025, 17:50**.

Não há autorização escrita de Segurança Operacional prorrogando o prazo de 6 horas anexada a este RIO. A ata verbal das 14:00 de 18/06 não constitui extensão formal.

Versão resultante após rollback: **PH-PREDCOMP-v2.3** (model card MC-PREDCOMP-2.3 vigente).

## 7. Linhagem de features da versão em produção (v2.4)

Solicitação formal de linhagem registrada em 18/06/2025, 16:40 (ticket MLOPS-5520). Em **20/06/2025, 18:00** — após mais de 1 dia útil contado da confirmação em 18/06 11:15 — o owner anexou apenas planilha parcial `features-predcomp-2.4-rascunho.xlsx`, **sem** identificação da origem do dataset de vibração pós-recalibração nem do responsável pela extração da janela usada no último retreino menor (patch 2.4.1 de features, promovido tacitamente em 10/06/2025 sem atualização de linhagem na model card).

A model card MC-PREDCOMP-2.4 permanece com linhagem referente ao treino de abril/2025, não ao estado efetivamente servido em 18/06/2025.

## 8. Componente de fornecedor

O escore de anomalia de vibração consumido como feature deriva do componente SaaS **VibSense Insights API** (fornecedor fictício Vibratek Analytics Ltda.).

- Última diligência arquivada: **DD-VIBRATEK-2024-09**, validade declarada até **12/05/2025**.
- Na data do incidente (18/06/2025), a diligência estava **vencida**.
- Não há, neste RIO, plano de regularização datado dentro de 10 dias úteis após registro da não conformidade, nem desabilitação documentada do componente antes do rollback geral do modelo.

## 9. Impacto operacional (resumo)

- Duas intervenções não programadas no TC-PH7-A (INT-EMERG-331/332).
- Indisponibilidade parcial do trem: aproximadamente 11 horas acumuladas.
- Sem evento SMS de lesão ou escape.
- Custo de mobilização registrado no CMMS sob centro de custo interno CC-PH7-MANUT (valor omitido neste RIO sintético).

## 10. Encerramento (parcial)

Status atual: **contido** (auto-recomendação v2.4 desabilitada; produção em v2.3). Encerramento formal de governança condicionado à regularização de HITL processual, linhagem da versão que estava em produção e diligência do componente Vibratek.

**Última atualização:** 25/06/2025, 16:35 — L. Ferreira.

