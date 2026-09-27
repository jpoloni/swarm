# CASE: Programa HORIZONTE DIGITAL — Aurora Energia S.A.
**Ciclo decisório 2027 · Comitê de Investimentos em TIC · Reunião em 08/10/2026**

## 1. Contexto

Aurora Energia S.A. é uma operadora de capital misto com 14 ativos offshore produzindo ~780 kboed nas bacias de Campos e Santos:

| Classe | Qtd | Idade média | Observação |
|---|---|---|---|
| FPSO próprio | 6 | 11 anos | Rede OT própria, PI System local |
| FPSO afretado (BOT) | 5 | 4 anos | Casco e topside operados por terceiro; dados de automação pertencem contratualmente ao afretador |
| Plataforma fixa legada | 3 | 27 anos | Automação Foxboro/Honeywell fim de vida, sem historiador |

Em março de 2024 a Diretoria aprovou o Programa Horizonte Digital: R$ 412 MM em 4 anos (R$ 318 MM CAPEX + R$ 94 MM OPEX), com promessa de VPL de R$ 1,1 bi e payback em 2,8 anos, sustentado por três teses: manutenção preditiva, otimização de produção em tempo real e redução de ciclo de decisão exploratória.

O gerente do programa em 08/10 precisa entregar o plano 2027.

## 2. Situação financeira

| Item | Valor |
|---|---|
| Aprovado 2024–2027 | R$ 412,0 MM |
| Realizado até set/2026 | R$ 231,4 MM (56,2%) |
| Escopo entregue (EVM) | 34% |
| SPI atual | 0,61 |
| CPI atual | 0,79 |
| Solicitado para 2027 | R$ 96,0 MM |
| Teto sinalizado pela DFI em 22/09 | R$ 58,0 MM |

Dos R$ 58 MM, R$ 31,2 MM já são compromisso contratual irrevogável (multa rescisória média de 40% do saldo):

| Compromisso | Valor 2027 | Natureza |
|---|---|---|
| Manutenção licenças AVEVA PI + Unified Operations Center | R$ 8,6 MM | USD 1,43 MM a R$ 6,02 (câmbio travado até jun/27) |
| Manutenção licenças Cognitive APM Suite | R$ 2,1 MM | 22% a.a. sobre R$ 9,4 MM de licenças perpétuas |
| Fábrica de software (Consórcio TecMar) | R$ 12,4 MM | Contrato vence 31/01/2027, sem prorrogação (5º ano) |
| Cloud pública (Azure BR South + FinOps) | R$ 5,3 MM | 61% de ambientes não-produtivos |
| Link satelital VSAT banda C (14 unidades) | R$ 2,8 MM | Até dez/2028; rescisão = 18 meses de mensalidade |

Sobram R$ 26,8 MM discricionários para uma carteira que demanda R$ 89,3 MM.

## 3. Histórico de decisões

Mai/2024 — Business case do APM aprovado com premissa de R$ 40 MM/ano em redução de perda; benchmark Noruega onshore nunca validado com histórico Aurora.

Ago/2024 — Piloto no FPSO Aurora-12 (afretado): 4 alarmes verdadeiros, 2 falsos positivos, ganho anualizado R$ 1,8 MM. Classificado sucesso técnico; comitê autorizou rollout.

Nov/2024 — Arquitetura aprovada assumindo conectividade existente suficiente; nenhuma linha de orçamento para banda.

Dez/2025 — Antecipação de licenças perpétuas Cognitive APM Suite R$ 9,4 MM para 14 unidades; 3 implantadas; 11 shelfware.

Fev/2026 — E&P contratou SaaS do fabricante de turbocompressores R$ 3,2 MM/ano fora do programa; cobre 6 unidades; sobrepõe Cognitive APM em 4.

Jun/2026 — Security Assessment reprovou go-live do CIO: escrita de setpoint corporativo→controle sem broker; IEC 62443-3-2; Cibersegurança fora do design. Retrabalho R$ 6,1 MM e 7 meses.

Ago/2026 — Incidente P-Jubarte: Windows Server 2016 sem patch comprometido por pendrive; 9h modo manual; notificação ANP; Auditoria risco crítico prazo 31/12/2027.

Set/2026 — Modelo anomalia bombas: precisão 0,84→0,51; 11 meses de dados; sem retreino; cientista saiu jan/2026; vaga congelada.

## 4. Stakeholders

Renata Salgado (DFI) — teto inegociável, quer desmobilização.
Cel. Aparecido Naves (Segurança/Conformidade) — apontamento Auditoria é prazo regulatório.
Wilson Tagliatti (E&P) — programa não entregou; já resolveu por fora.
Larissa Fontoura (Subsuperfície) — OSDU em 2027 ou perde 16º ciclo ANP.
Márcio Quaresma (TIC) — preservar programa.
Consórcio TecMar — 38 alocados; conhecimento do CIO; contrato morre 31/01/2027.

## 5. Carteira 2027 candidata

F1 Remediação ciber OT — R$ 21,4 MM CAPEX — prazo 31/12/2027 — janelas mai/27 e set/27.
F2 Rollout APM 11 unidades — R$ 28,7 MM CAPEX — assume conectividade/sensoriamento.
F3 OSDU R3 — R$ 17,9 MM CAPEX — ANP 16º ciclo jun/2027 — 640 TB LTO-5.
F4 Conectividade LEO + backhaul — R$ 11,2 MM CAPEX + R$ 4,6 MM/ano OPEX — atual 12 Mbps / 640 ms.
F5 Conclusão CIO — R$ 6,1 MM CAPEX — 82% construído.
F6 Sustentação — R$ 9,4 MM OPEX — a partir 01/02/2027 — nunca teve linha própria.
Total demanda R$ 89,3 MM.

## 6. Anexo técnico

A. Sensoriamento: completo 2; parcial 5; insuficiente 7. Adequar 7 = R$ 19,3 MM fora de F2; área classificada.
B. Banda: APM 34 Mbps; CIO 55 Mbps; atual 12 Mbps. F2 e F5 inviáveis sem F4.
C. FPSOs afretados: tags do afretador; aditivo R$ 1,1 MM/unidade/ano fora do orçamento; 4 com sensor completo/parcial são afretadas.
D. LTO-5: leitora única fora de suporte; erro 3,1%; risco perda sísmica 3 blocos.
E. Shelfware: conversão 11 licenças em crédito com -30% até 30/11/2026.
F. Sem F6 em 01/02/2027: data lake regulatório ANP, portal integridade, 3 APM prod sem suporte.

## 7. Restrições duras

1. Teto R$ 58,0 MM. CAPEX↔OPEX exige Conselho (90 dias).
2. TecMar não prorrogável; nova licitação 7–11 meses; sem transfer de conhecimento.
3. Headcount congelado.
4. Janelas parada: mai/2027 e set/2027; próxima mai/2028.
5. Câmbio travado até jun/2027; 2º semestre R$ 6,40–6,85.
6. Auditoria crítica 31/12/2027 com reporte trimestral ao Comitê.
7. Conteúdo local em parte do CAPEX.

## 8. A decisão (entregáveis da recomendação)

1. Alocação dos R$ 26,8 MM discricionários.
2. Tratamento dos R$ 31,2 MM comprometidos.
3. Sequenciamento com dependências e janelas de parada.
4. Estratégia TecMar 31/01/2027.
5. Revisão do VPL R$ 1,1 bi.
6. Posição sobre SaaS paralelo do E&P.
7. Riscos dos não financiados com dono e escalonamento.
