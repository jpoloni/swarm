# Registro de Evento Orçamentário de TIC (REO)
## REO-2025-0142 | Severidade financeira: Alta | Status: Em apuração — overrun em curso

**Tipo:** overrun de Opex cloud + compromisso Capex de telecom em Unidade Offshore Delta  
**Empresa:** PetroHorizonte S.A.  
**Unidade:** Unidade Offshore Delta (UOD)  
**Linha orçamentária:** WBS-TIC-UOD-CLOUD-2025 (Opex cloud) e WBS-TIC-UOD-NET-2025 (Capex telecom)  
**Orçamento aprovado (ano):** Cloud R$ 4.200.000,00 | Telecom Capex R$ 1.800.000,00  
**Data/hora da abertura deste REO:** 28/06/2025, 10:40 (America/Sao_Paulo)  
**Trimestre:** 2T2025 (change freeze orçamentário: 21/06/2025 a 30/06/2025)  
**Área gestora:** TIC Operações Offshore — Delta  
**Responsável pelo registro:** M. Andrade (gestão orçamentária TIC UOD)

---

## 1. Resumo executivo

Em junho/2025, a Unidade Offshore Delta acelerou workload sísmico em cloud e contratou upgrade emergencial de link VSAT após degradação de latência. O realizado + comprometido da linha cloud ultrapassou 10% do orçamento aprovado; um novo compromisso Opex de suporte gerenciado (R$ 72.000,00) foi firmado em **24/06/2025**, dentro da janela de change freeze. O Capex de telecom de R$ 620.000,00 obteve ata CGTIC antes do PO. Parte das obrigações de forecast e FinOps foi cumprida; rebaseline, exceção de freeze e regularização de emergência permanecem abertos neste REO.

## 2. Linha do tempo

| Horário (BRT) | Evento |
|---|---|
| 05/06/2025 17:10 | Forecast junho publicado em `orcamento-tic/forecast/2025-06-UOD-CLOUD.md` (variação +6,2% vs OAT; justificativa: campanha sísmica Q2) |
| 09/06/2025 11:00 | Relatório FinOps semanal W23 arquivado em `orcamento-tic/finops/semanal/2025-W23-uod-cloud.pdf` |
| 16/06/2025 11:05 | Relatório FinOps semanal W24 arquivado em `orcamento-tic/finops/semanal/2025-W24-uod-cloud.pdf` |
| 18/06/2025 14:30 | Ata CGTIC-2025-0618 aprova Capex telecom VSAT UOD no valor de R$ 620.000,00 |
| 19/06/2025 09:15 | PO-78441 emitido para Capex VSAT (após ata CGTIC-2025-0618); arquivo em `orcamento-tic/atas-cgtic/CGTIC-2025-0618.pdf` |
| 21/06/2025 00:00 | Início do change freeze orçamentário do 2T2025 (últimos 10 dias do trimestre) |
| 22/06/2025 08:40 | Alerta FinOps: realizado + comprometido cloud = **R$ 4.662.000,00** (11,0% acima do orçamento aprovado de R$ 4.200.000,00) |
| 23/06/2025 16:20 | Desembolso emergencial cloud spot + R$ 95.000,00 para jobs sísmicos (autorização verbal do gerente UOD; sem despacho CGTIC/CFO na data) |
| 24/06/2025 15:45 | Assinatura de aditivo Opex suporte gerenciado cloud com fornecedor NébulaOps Ltda., valor **R$ 72.000,00**, competência junho–agosto |
| 25/06/2025 10:00 | Pedido informal de rebaseline enviado por chat ao secretário do CGTIC; **sem ata de rebaseline** até a abertura deste REO |
| 28/06/2025 10:40 | Abertura do REO-2025-0142; Controladoria e DTI cientificadas |

## 3. Números e alçadas

- **Orçamento cloud aprovado (WBS-TIC-UOD-CLOUD-2025):** R$ 4.200.000,00.
- **Realizado + comprometido cloud em 22/06/2025:** R$ 4.662.000,00 (**+11,0%**).
- **Novo compromisso Opex em 24/06/2025 (NébulaOps):** R$ 72.000,00 (acima do limiar de R$ 50.000,00 do change freeze).
- **Capex VSAT aprovado:** R$ 620.000,00 (acima do limiar de R$ 500.000,00) — ata CGTIC-2025-0618 em 18/06/2025; PO-78441 em 19/06/2025.
- **Contingência TIC da UOD:** saldo R$ 300.000,00; **nenhum despacho de drawdown** registrado em `orcamento-tic/contingencia/` até 28/06/2025.

## 4. Evidências de cumprimento parcial

Forecast junho: o gestor da linha publicou em **05/06/2025** o arquivo `orcamento-tic/forecast/2025-06-UOD-CLOUD.md`, dentro do 5º dia útil, com variação **+6,2%** e justificativa da campanha sísmica Q2.

FinOps semanal: relatórios **2025-W23** e **2025-W24** arquivados em `orcamento-tic/finops/semanal/`, com conta `ph-uod-prod`, valor da semana, acumulado do mês e top-5 serviços.

Capex telecom: a ata **CGTIC-2025-0618** (18/06/2025) precede o PO-78441 (19/06/2025) para o compromisso de R$ 620.000,00.

## 5. Lacunas observadas neste REO

Change freeze: em **24/06/2025**, dentro da janela 21/06–30/06/2025, foi assumido compromisso Opex de **R$ 72.000,00** com a NébulaOps Ltda. **Não há** exceção formal do CFO (e-mail ou despacho numerado) arquivada no dossiê da linha WBS-TIC-UOD-CLOUD-2025.

Rebaseline: desde o alerta de **22/06/2025**, com overrun de **11,0%**, novos desembolsos e o compromisso NébulaOps ocorreram **sem** ata de rebaseline do CGTIC. O pedido em chat de 25/06/2025 não constitui aprovação.

Spend emergencial: o desembolso de **R$ 95.000,00** em 23/06/2025 foi autorizado verbalmente pelo gerente UOD. Até **28/06/2025** (5 dias após o primeiro desembolso) **não há** aprovação retrospectiva do CGTIC ou do CFO no dossiê; o prazo de 15 dias corridos ainda não venceu na abertura deste REO, porém a regularização permanece pendente e sem protocolo numerado.

Contingência: o overrun cloud **não** foi coberto por drawdown documentado; saldo de contingência permanece R$ 300.000,00 sem despacho do Diretor de TIC.

## 6. Fornecedores e sistemas

- **NébulaOps Ltda.:** suporte gerenciado cloud (aditivo Opex 24/06/2025).
- **OrbitLink Comunicações:** fornecedor do Capex VSAT (PO-78441).
- **Conta cloud:** `ph-uod-prod` (região sa-east-1 / workloads sísmicos).

## 7. Avaliação preliminar por requisito (não substitui parecer de conformidade)

MUST-01 (Capex ≥ R$ 500 mil com ata CGTIC antes do PO): CUMPRIDO para VSAT — ata CGTIC-2025-0618 em 18/06/2025; PO-78441 em 19/06/2025; path `orcamento-tic/atas-cgtic/CGTIC-2025-0618.pdf`.

MUST-02 (forecast até 5º dia útil): CUMPRIDO — forecast junho publicado em 05/06/2025 com variação +6,2% e justificativa.

MUST-03 (change freeze / exceção CFO): LACUNA — compromisso Opex R$ 72.000,00 em 24/06/2025 sem exceção formal do CFO.

MUST-04 (rebaseline antes de continuar overrun >10%): LACUNA — alerta 22/06/2025 com +11,0%; desembolso 23/06 e compromisso 24/06 sem ata de rebaseline.

MUST-05 (relatório semanal FinOps): CUMPRIDO para W23 e W24 — arquivos em `orcamento-tic/finops/semanal/`.

MUST-06 (regularização emergencial em 15 dias): PENDENTE / EM CURSO — desembolso 23/06/2025; até 28/06/2025 sem aprovação retrospectiva numerada (prazo de 15 dias ainda aberto na data do REO).

MUST-07 (drawdown de contingência documentado): N/A neste REO quanto a drawdown executado — não houve drawdown; saldo intacto sem despacho.

## 8. Próximas ações registradas

1. Solicitar despacho de exceção CFO para o aditivo NébulaOps (retroativo) ou cancelamento do compromisso.
2. Incluir rebaseline WBS-TIC-UOD-CLOUD-2025 na pauta CGTIC de 02/07/2025.
3. Protocolar regularização do spend emergencial de 23/06/2025 antes de 08/07/2025 (15º dia corrido).

---

