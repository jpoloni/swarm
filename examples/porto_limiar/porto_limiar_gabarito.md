# Parecer Executivo de Governança e Decisão de Carteira

## 1. Decisões por Frente e Carteira Recomendada
- **F1 — Operação ferroviária de preservação de slots:** Aprovar. Cita [C34, C35, C36, C73, C89, C05, C06]. A operação eleva o uso para 75%, evita o gatilho de cancelamento de metade dos slots e preserva valor econômico de R$ 42,00 MM, apesar da margem negativa de R$ 3,60 MM.
- **F2 — Substituição de cabeços de amarração:** Aprovar. Cita [C37, C38, C20, C18, C19, C82, C30, C31, C32]. Obrigação de segurança crítica com prazo da Autoridade Portuária até 30/06/2027; OPEX enquadrado como compulsório e não consumidor do teto.
- **F3 — Extensão do Berço B1:** Rejeitar/Diferir para 2028+. Cita [C39, C40, C41, C83, C30, C31, C32, C33, C05, C06, C90, C91]. A interdição de 105 dias contínuos excede o máximo anual de 70 e o trimestral de 20; o benefício depende de contrato não assinado e carta de intenção não vinculante que expira em 31/07/2027. Reentrada condicionada a novo projeto executivo e nova licitação que reduzam a interdição para <=18 dias anuais e <=7 por trimestre, e a contrato vinculante.
- **F4 — Shore power de alta tensão:** Diferir/Cancelar para 2027. Cita [C42, C43, C76, C67, C84, C30, C31, C32]. Não é obrigatória sem F3, pois a licença atual é 980 mil TEU/ano e a Resolução AP-18/2025 isenta terminais <=1,20 milhão TEU. Se F3 futura for aprovada, F4 deve ser incluída antes do comissionamento da capacidade acima de 1,20 milhão TEU.
- **F5 — Automação de gates e pátio (TurnGate):** Rejeitar. Cita [C44, C45, C46, C47, C78, C79, C89, C04, C69]. O payback de 3,4 anos não se sustenta: a amostra tem 55% de transbordo e 83% do benefício é proporcional a transbordo, enquanto o TPL tem 18%. Evita take-or-pay de R$ 5,80 MM/ano por dez anos e multa de rescisão de R$ 31,32 MM.
- **F6 — Migração do TOS:** Aprovar condicionada. Cita [C48, C49, C50, C77, C85, C30, C31, C32, C22, C17]. Condições: exercer a extensão única do suporte Atlas até 30/04/2027, pagar R$ 1,80 MM, mobilizar até 01/04/2027 e concluir cutover até 31/12/2027. CAPEX 24,00; OPEX 11,80 (10,00 + 1,80); interdição 3 berço-dias no T4.
- **F7 — Sensoriamento e telemetria:** Aprovar. Cita [C51, C52, C86, C30, C31, C32]. CAPEX 12,00; OPEX 4,00; interdição 4 berço-dias (2 T2, 2 T3); benefício de R$ 6,00 MM/ano a partir de 2028.
- **F8 — IA de manutenção preditiva:** Diferir. Cita [C53, C54, C80, C87, C89, C91]. Exige 15 meses contínuos de telemetria após estabilização de F7; a promessa de R$ 8,50 MM em 2027 é incompatível. Reentrada após a janela de dados, com dono e data.
- **F9 — Dragagem e recuperação de garantias:** Aprovar. Cita [C55, C56, C57, C21, C18, C23, C24, C25, C26, C29, C75, C81, C88, C30, C31, C32]. C1 20,00; OPEX 2,18 enquadrado como compulsório; interdição 3 berço-dias no T4; concluir até 15/12/2027.
- **C2 — Protocolo independente:** Aprovar. Cita [C24, C57, C75, C74, C28, C29]. Recuperação de R$ 8,00 MM independente da dragagem; protocolar até 30/11/2027.
- **Carteira recomendada:** F1, F2, F6, F7, F9 e C2. CAPEX Fonte A: 50,00; OPEX total: 25,78; interdição: 18 berço-dias. Saldos: CAPEX 128,00; OPEX cap 11,60; C1 0,00; C2/C3 recuperados 14,00.
responde: MUST-1

## 2. Alocação por Fonte/Entidade e Demonstração de Aderência aos Tetos
Tabela de alocação com metadados por linha:
| tipo_linha | item_id | fonte | valor_solicitado | valor_deliberado | decisao | escopo_removido | depends_on | binding_constraint_ids | responde | janela |
|---|---|---|---:|---:|---|---|---|---|---|---|
| CAPEX | F2 | Fonte A | 14,00 | 14,00 | Aprovar | 0,00 | SEC-02 | [C09,C10,C12,C37,C38] | MUST-2 | até 30/06/2027 |
| OPEX | F2 | Conformidade (exempt) | 4,20 | 4,20 | Aprovar | 0,00 | SEC-02 | [C18,C19,C20] | MUST-2 | 2027 |
| CAPEX | F3 | Fonte A | 88,00 | 0,00 | Diferir/Rejeitar 2027 | 88,00 | Novo projeto executivo e licitação | [C30,C31,C32,C33,C39,C40,C41,C83] | MUST-2 | 2028+ |
| OPEX | F3 | OPEX cap | 5,40 | 0,00 | Diferir/Rejeitar 2027 | 5,40 | Novo projeto executivo e licitação | [C30,C31,C32,C33,C39,C40,C41,C83] | MUST-2 | 2028+ |
| Interdição | F3 | Berço-dias | 105 | 0 | Diferir/Rejeitar 2027 | 105 | Novo projeto executivo e licitação | [C30,C31,C32,C33,C39,C40,C41,C83] | MUST-2 | 2028+ |
| CAPEX | F4 | Fonte A | 22,00 | 0,00 | Diferir | 22,00 | F3 | [C42,C43,C76,C67,C84] | MUST-2 | após F3 |
| OPEX | F4 | OPEX cap | 2,00 | 0,00 | Diferir | 2,00 | F3 | [C42,C43,C76,C67,C84] | MUST-2 | após F3 |
| Interdição | F4 | Berço-dias | 10 | 0 | Diferir | 10 | F3 | [C42,C43,C76,C67,C84] | MUST-2 | após F3 |
| CAPEX | F5 | Fonte A | 36,00 | 0,00 | Rejeitar | 36,00 | nenhum | [C44,C45,C46,C47,C78,C79] | MUST-2 | 2027 |
| OPEX | F5 | OPEX cap | 5,80/ano | 0,00 | Rejeitar | 5,80/ano | nenhum | [C44,C45,C46,C47,C78,C79] | MUST-2 | 2027 |
| CAPEX | F6 | Fonte A | 24,00 | 24,00 | Aprovar condicionada | 0,00 | Extensão Atlas até 30/04/2027 | [C48,C49,C50,C77,C85,C22] | MUST-2 | mobilização até 01/04/2027; cutover até 31/12/2027 |
| OPEX | F6 | OPEX cap | 10,00 | 10,00 | Aprovar condicionada | 0,00 | Extensão Atlas | [C48,C49,C50,C77,C85,C22] | MUST-2 | 2027 |
| OPEX | F6 extensão | OPEX cap | 1,80 | 1,80 | Aprovar condicionada | 0,00 | Notificação até 30/04/2027 | [C50,C77] | MUST-2 | 2027 |
| Interdição | F6 | Berço-dias | 3 | 3 | Aprovar condicionada | 0,00 | Extensão Atlas | [C30,C31,C32,C48,C49,C50] | MUST-2 | T4/2027 |
| CAPEX | F7 | Fonte A | 12,00 | 12,00 | Aprovar | 0,00 | nenhum | [C51,C52,C86] | MUST-2 | 2027 |
| OPEX | F7 | OPEX cap | 4,00 | 4,00 | Aprovar | 0,00 | nenhum | [C51,C52,C86] | MUST-2 | 2027 |
| Interdição | F7 | Berço-dias | 4 | 4 | Aprovar | 0,00 | nenhum | [C30,C31,C32,C51,C52] | MUST-2 | T2/T3 2027 |
| CAPEX | F8 | Fonte A | 9,00 | 0,00 | Diferir | 9,00 | F7 + 15 meses telemetria | [C53,C54,C80,C87] | MUST-2 | após 15 meses |
| OPEX | F8 | OPEX cap | 1,90 | 0,00 | Diferir | 1,90 | F7 + 15 meses telemetria | [C53,C54,C80,C87] | MUST-2 | após 15 meses |
| C1 | F9 | C1 | 20,00 | 20,00 | Aprovar | 0,00 | Sítio Delta | [C23,C55,C56,C57,C81,C88] | MUST-2 | até 15/12/2027 |
| OPEX | F9 | Conformidade (exempt) | 2,18 | 2,18 | Aprovar | 0,00 | REG-04 | [C18,C21] | MUST-2 | 2027 |
| Interdição | F9 | Berço-dias | 3 | 3 | Aprovar | 0,00 | Sítio Delta | [C30,C31,C32,C55,C56] | MUST-2 | T4/2027 |
| Vinculado | C2 | C2 | 8,00 | 8,00 | Aprovar protocolo independente | 0,00 | Certidões e termo | [C24,C57,C75,C74,C28,C29] | MUST-2 | até 30/11/2027 |
| Vinculado | C3 | C3 | 6,00 | 6,00 | Aprovar condicionada a F9 | 0,00 | F9 | [C25,C29,C57] | MUST-2 | até 15/12/2027 |
| OPEX | F1 | OPEX cap | 3,60 | 3,60 | Aprovar | 0,00 | nenhum | [C17,C22,C34,C35,C36] | MUST-2 | 2027 |

**Totais e reconciliação:**
- CAPEX Fonte A disponível: 160,00 + 18,00 = 178,00. Alocado: 14,00 + 24,00 + 12,00 = 50,00. Saldo: 178,00 − 50,00 = 128,00.
- OPEX cap: teto 31,00. Consumido: F1 3,60 + F6 11,80 + F7 4,00 = 19,40. Folga: 31,00 − 19,40 = 11,60.
- OPEX compulsório/exempt: F2 4,20 + F9 2,18 = 6,38. OPEX total: 19,40 + 6,38 = 25,78.
- C1: 20,00 alocado, saldo 0,00. C2: 8,00 recuperado. C3: 6,00 recuperado condicionado. Total recuperado: 14,00.
- Interdição: máximo 70; rotina 52; projetos 18; saldo 0.

**Disposition dos saldos positivos:**
- CAPEX Fonte A saldo 128,00: disposition: reserva_com_gatilho; fração_expirante: 0,00 (0,00%); data_limite: 31/12/2028. Gatilhos: F3 (novo projeto executivo e licitação), F4 (se F3), F8 (após 15 meses de telemetria).
- OPEX cap folga 11,60: disposition: reserva_com_gatilho; fração_expirante: 0,00 (0,00%); data_limite: 31/12/2027. Gatilhos: F8 (1,90) se condição cumprida; F3/F4 se aprovados em 2027 (não recomendado).
- C1 saldo 0,00: não há saldo.
- C2 saldo 0,00: recuperado; disposition: reserva_com_gatilho para 2028; fração_expirante: 0,00; data_limite: 31/12/2028.
- C3 saldo 0,00: recuperado condicionado; disposition: reserva_com_gatilho para 2028; fração_expirante: 0,00; data_limite: 31/12/2028.
- Interdição saldo 0: não há saldo.
responde: MUST-2

## 3. Tratamento dos Compromissos Contratuais e Valores Comprometidos
- **RF-11:** F1 aprovada eleva uso para 75%, evitando o gatilho de cancelamento de metade dos slots. Valor econômico preservado: R$ 42,00 MM [C35, C36, C73].
- **Atlas 7:** F6 condicionada à extensão única por seis meses, com notificação até 30/04/2027 e pagamento de R$ 1,80 MM [C50, C77].
- **TurnGate:** F5 rejeitada. Evita take-or-pay de R$ 5,80 MM/ano por dez anos e multa de rescisão de R$ 31,32 MM [C47, C79, C89].
- **C2:** protocolo independente da dragagem; recuperação de R$ 8,00 MM após certidões e termo de encerramento [C24, C57, C75].
- **C3:** recuperação de R$ 6,00 MM condicionada à execução regular de F9 e comprovação de destinação licenciada [C25, C29].
- **F9:** C1 de R$ 20,00 MM alocado exclusivamente à campanha de dragagem [C23].
responde: MUST-3

## 4. Cronograma Físico Trimestral e Capacidade Operacional
| Trimestre | Capacidade bruta | Rotina obrigatória | Projetos aprovados | Total | Saldo |
|---|---:|---:|---:|---:|---:|
| T1 | 20 | 13 | F2 4 | 17 | 3 |
| T2 | 20 | 13 | F2 4 + F7 2 | 19 | 1 |
| T3 | 20 | 13 | F7 2 | 15 | 5 |
| T4 | 20 | 13 | F6 3 + F9 3 | 19 | 1 |
| Ano | 70 | 52 | 18 | 70 | 0 |

**Janelas:** F2 até 30/06/2027; F6 mobilização até 01/04/2027 e cutover até 31/12/2027; F7 T2/T3; F9 até 15/12/2027; C2 até 30/11/2027; C3 até 15/12/2027.
responde: MUST-4

## 5. Registro de Riscos
| Item/Frente | Exposição (R$ MM) | Dono | Gatilho e Mitigação |
|---|---:|---|---|
| F1 | 42,00 = valor econômico dos slots | Diretoria Comercial | Gatilho: uso <70% por 2 trimestres. Mitigação: F1 eleva para 75%. |
| F2 | 68,00 = 20% × 340,00 | Diretoria de Segurança | Gatilho: não concluir até 30/06/2027. Mitigação: F2. |
| F3 | 0,00 em 2027 (oportunidade não reconhecida) | Diretoria Comercial | Gatilho: LOI expira 31/07/2027. Mitigação: novo projeto executivo e licitação, contrato vinculante. |
| F4 | 0,00 em 2027 | Assessoria Regulatória | Gatilho: F3 aprovada. Mitigação: incluir F4 antes do comissionamento >1,2M TEU. |
| F5 | 31,32 = 60% × 9 × 5,80 | Diretoria de Operações | Gatilho: assinatura do contrato. Mitigação: rejeitar/renegociar. |
| F6 | 12,00 = 25% × 48,00 | Diretoria de TI | Gatilho: não exercer extensão até 30/04/2027. Mitigação: exercer extensão, pagar 1,80. |
| F7 | 6,00/ano a partir de 2028 | Diretoria de Manutenção | Gatilho: não instalar sensores. Mitigação: F7. |
| F8 | 10,90 = 9,00 + 1,90 | Diretoria de TI | Gatilho: contratar antes de 15 meses. Mitigação: diferir. |
| F9 | 75,00 = 50 × 1,50 | Diretoria de Operações | Gatilho: não concluir até 15/12/2027. Mitigação: F9. |
| C2 | 8,00 | Controladoria/Jurídico | Gatilho: não protocolar até 30/11/2027. Mitigação: protocolo independente. |
| C3 | 6,00 | Diretoria de Meio Ambiente | Gatilho: não comprovar destinação até 15/12/2027. Mitigação: F9 regular. |
responde: MUST-5

## 6. Revisão do Business Case, Metas Financeiras e Análise de Elasticidade
- **F5:** benefício ajustado ao TPL: 16,40 × 0,83 = 13,612; 13,612 × 18/55 = 4,455; 16,40 × 0,17 = 2,788; total = 7,243; líquido = 7,243 − 5,80 = 1,443; payback = 36,00 ÷ 1,443 = 24,95 anos. Rejeitar [C45, C46, C78].
- **F3:** benefício de R$ 28,00 MM/ano a partir de 2029, mas CAPEX 88,00, OPEX 5,40 e interdição 105 > 70. Não viável em 2027 [C39, C40, C41].
- **F8:** promessa de R$ 8,50 MM em 2027 incompatível com 15 meses de telemetria. Diferir [C54, C80].
- **Elasticidade:** o recurso vinculante é a interdição. Um novo projeto executivo e nova licitação que reduzam F3 de 105 para <=18 dias anuais e <=7 por trimestre, ou um berço substituto certificado, mudariam a carteira. CAPEX e OPEX não são restrições: saldo CAPEX 128,00 e folga OPEX 11,60. Gatilho: conclusão do novo projeto e licitação, mais contrato vinculante com Aliança.
responde: MUST-6

## 7. Mapa de Dependências e Posicionamentos Estruturantes
- F2: pré-requisito Laudo SEC-02; concluir até 30/06/2027 [C82].
- F3: pré-requisito novo projeto executivo se houver mudança de método; método atual exige 105 dias contínuos [C83].
- F4: pré-requisito F3 civilmente concluída; energizar antes de comissionar capacidade >1,20M TEU [C84].
- F6: pré-requisito extensão Atlas se cutover após 30/06; nove meses entre mobilização e cutover [C85].
- F7: sem pré-requisito; estabilização 30 dias após instalação [C86].
- F8: pré-requisito F7 estabilizada + 15 meses de dados; primeiro modelo produtivo somente depois da janela [C87].
- F9: pré-requisito reserva do Sítio Delta; concluir até 15/12/2027 [C88].
- C2: independente de F9; protocolar até 30/11/2027 [C57, C75].
- C3: depende de F9; comprovar até 15/12/2027 [C25, C29].
- Decisões antecipadas: F6 extensão até 30/04/2027; F2 até 30/06/2027; C2 até 30/11/2027; F9 até 15/12/2027.
responde: MUST-7 e MUST-8

## 8. Premissas Contestadas e Governança
- **P1:** Recusada. O CAPEX disponível é 160,00 + 18,00 = 178,00, pois os R$ 18,00 MM do Armazém Norte retornam à mesma autorização [C09, C10, C11, C12, C65].
- **P2:** Recusada. F2 e F9 são compulsórios e não consomem o teto, conforme item 4.3 e pareceres SEC-02/2027 e REG-04/2027 [C17, C18, C19, C20, C21, C22, C66].
- **P3:** Recusada. A Resolução AP-18/2025 isenta terminais <=1,20 milhão TEU; a licença atual é 980 mil TEU/ano. F4 não é obrigatória sem F3 [C43, C76, C67].
- **P4:** Recusada. A cláusula 14.6 permite extensão única por seis meses até 31/12/2027, mediante notificação até 30/04/2027 e pagamento de R$ 1,80 MM [C50, C77, C68].
- **P5:** Recusada. A amostra tem 55% de transbordo e 83% do benefício é proporcional a transbordo; o TPL tem 18%. O payback de 3,4 anos não se sustenta [C46, C78, C69, C04].
- **P6:** Parcialmente aceita. Os limites de 70 anuais e 20 trimestrais existem, mas atividades simultâneas podem contar pelo maior prazo se houver plano técnico de sobreposição; nenhum plano foi apresentado. F3 com 105 dias excede sozinha o limite [C30, C31, C32, C33, C70].
- **P7:** Parcialmente aceita. O covenant de 3,50x existe, mas há folga de 0,08x (3,42x projetado) e não há waiver automático. Não se recomenda dívida nova [C13, C14, C15, C71].
- **P8:** Aceita. A disposição na Célula Alfa é proibida; o Sítio Delta é o destino licenciado e já está no orçamento de F9 [C72, C81].
- **Brechas do Premise Breaker:** (1) F4 diferível sem F3; (2) F6 diferível com extensão Atlas; (3) F5 rejeitada por benefício superestimado; (4) plano de sobreposição pode reduzir interdição, mas F3 excede; (5) F3 pode ser redesenhada com novo projeto e licitação; (6) C2 independente de F9; (7) C2/C3 tornam-se caixa livre após liberação; (8) folga de covenant não autoriza dívida automaticamente; (9) cancelamento de slots é faculdade da concessionária e pode ser evitado com F1.
responde: MUST-9

## 9. Afirmações Rastreáveis
| ID | doc_id | locator | Citação literal |
|---|---|---|---|
| C01 | 01_mandato_e_secao1 | line:24 | O TPL opera o Terminal Limiar, no litoral Sudeste, sob concessão até 2044. |
| C02 | 01_mandato_e_secao1 | line:24 | A infraestrutura principal é composta por dois berços contíguos, B1 e B2, quatro portêineres, pátio de 420 mil m², ramal ferroviário próprio e um único centro de controle operacional. |
| C03 | 01_mandato_e_secao1 | line:26 | Em 2026, o terminal movimentou 842 mil TEU. A licença operacional vigente autoriza até 980 mil TEU/ano. |
| C04 | 01_mandato_e_secao1 | line:26 | Cargas de transbordo representaram 18% dos movimentos; importação e exportação de clientes cativos representaram 82%. |
| C05 | 01_mandato_e_secao1 | line:28 | A prioridade do Conselho para 2027 é preservar a concessão, eliminar pendências de segurança e modernizar o terminal sem criar dívida nova nem interromper a rotina contratual. |
| C06 | 01_mandato_e_secao1 | line:28 | Projetos de crescimento não têm precedência automática sobre obrigações existentes. |
| C07 | 01_mandato_e_secao1 | line:30 | Não há no cadastro homologado do TPL berço substituto, terminal parceiro, instalação offshore, equipe externa de operação ou janela extraordinária de fechamento. |
| C08 | 01_mandato_e_secao1 | line:30 | Qualquer solução que dependa de um desses recursos exige contrato e certificação prévios, inexistentes na data-base. |
| C09 | 01_mandato_e_secao1 | line:34 | O Conselho aprovou **R$ 160,00 MM de CAPEX** para a carteira 2027. |
| C10 | 01_mandato_e_secao1 | line:36 | os **R$ 18,00 MM ainda não contratados retornam à mesma autorização de CAPEX 2027**, sem necessidade de nova deliberação, devendo a Controladoria efetuar a baixa no ERP |
| C11 | 01_mandato_e_secao1 | line:36 | A baixa ainda não foi processada no relatório gerencial de janeiro. |
| C12 | 01_mandato_e_secao1 | line:38 | Valores de CAPEX não utilizados em 2027 permanecem em caixa e podem ser reservados para 2028 mediante indicação de finalidade e gatilho. Não existe obrigação de gastar a autorização integralmente. |
| C13 | 01_mandato_e_secao1 | line:40 | É vedada contratação de dívida nova que leve a relação Dívida Líquida/EBITDA acima de 3,50 vezes. |
| C14 | 01_mandato_e_secao1 | line:44 | A relação Dívida Líquida/EBITDA projetada para 31 de dezembro de 2027 é **3,42 vezes**, antes de qualquer dívida nova. |
| C15 | 01_mandato_e_secao1 | line:44 | O contrato sindicalizado não prevê waiver automático, faixa de tolerância ou cura posterior para o limite de 3,50 vezes. |
| C16 | 01_mandato_e_secao1 | line:44 | Caixa já disponível e recursos vinculados não são dívida. |
| C17 | 01_mandato_e_secao1 | line:48 | O teto de **OPEX incremental da carteira é R$ 31,00 MM em 2027**. |
| C18 | 01_mandato_e_secao1 | line:50 | despesas incrementais comprovadamente compulsórias por norma regulatória, determinação da autoridade portuária ou correção de risco de segurança classificado como crítico serão apropriadas na rubrica central de conformidade e **não consumirão o teto da carteira**, embora devam constar do fluxo de caixa total |
| C19 | 01_mandato_e_secao1 | line:52 | O enquadramento exige parecer da Diretoria de Segurança ou da Assessoria Regulatória. |
| C20 | 01_mandato_e_secao1 | line:52 | O parecer SEC-02/2027 já classificou a troca dos cabeços de amarração de F2 como correção de risco crítico. |
| C21 | 01_mandato_e_secao1 | line:52 | O ofício REG-04/2027 classificou a campanha de dragagem de F9 como obrigação da licença operacional. |
| C22 | 01_mandato_e_secao1 | line:54 | Despesas de crescimento, produtividade, migração tecnológica e preservação comercial consomem o teto normalmente. |
| C23 | 01_mandato_e_secao1 | line:60 | C1 — Escrow de dragagem | 20,00 | Pagamento da campanha F9 contra medição hidrográfica e manifesto de destinação | 31/12/2027 | Disponível; não pode financiar outra frente |
| C24 | 01_mandato_e_secao1 | line:61 | C2 — Caução do Armazém Norte | 8,00 | Restituição após termo de encerramento e certidões fiscais | Protocolo até 30/11/2027 | Marcos materiais cumpridos; dossiê ainda não protocolado |
| C25 | 01_mandato_e_secao1 | line:62 | C3 — Garantia ambiental | 6,00 | Liberação após comprovação de destinação licenciada do material dragado | Protocolo até 15/12/2027 | Depende da execução regular de F9 |
| C26 | 01_mandato_e_secao1 | line:63 | | **Total** | **34,00** |  |  |  | |
| C27 | 01_mandato_e_secao1 | line:65 | O histórico de 2022–2026 mostra recuperação de 62% das cauções elegíveis. |
| C28 | 01_mandato_e_secao1 | line:65 | A Auditoria Interna atribuiu a perda remanescente a protocolos fora do prazo, ausência de certidões e falta de dono do processo. Não foi identificada rejeição por inexistência do direito material quando o dossiê estava completo e tempestivo. |
| C29 | 01_mandato_e_secao1 | line:67 | Recursos C2 e C3 continuam vinculados até a liberação. Seu reconhecimento como caixa livre antes da comprovação é proibido. A perda do prazo extingue o direito de restituição. |
| C30 | 01_mandato_e_secao1 | line:71 | A concessão e os contratos take-or-pay com armadores exigem disponibilidade anual mínima equivalente a 660 berço-dias. Como B1 e B2 oferecem juntos 730 berço-dias por ano, o TPL pode consumir no máximo **70 berço-dias de interdição em 2027**. Não há procedimento de waiver previsto nos contratos vigentes. |
| C31 | 01_mandato_e_secao1 | line:73 | A rotina legal e preventiva já programada consome 52 berço-dias, distribuídos igualmente: 13 em cada trimestre. Sobram 18 berço-dias para toda a carteira de projetos. |
| C32 | 01_mandato_e_secao1 | line:75 | Por razões de fila náutica e segurança, nenhum trimestre pode superar 20 berço-dias totais de interdição. |
| C33 | 01_mandato_e_secao1 | line:75 | Atividades simultâneas no mesmo berço contam pelo maior prazo apenas quando o plano técnico comprova sobreposição; nenhum plano de sobreposição foi apresentado para as frentes deste corpus. |
| C34 | 02_secao2_frentes_propostas | line:5 | **Pedido:** aprovar operação mínima de dois trens semanais durante 2027.  
**CAPEX:** 0,00.  
**OPEX incremental:** 3,60.  
**Interdição de berço:** 0 dia. |
| C35 | 02_secao2_frentes_propostas | line:10 | O Contrato Ferroviário RF-11 reserva quatro slots semanais ao TPL. O uso abaixo de 70% dos slots reservados por dois trimestres consecutivos autoriza a concessionária a cancelar definitivamente metade dos slots, sem dever de recomposição. O uso no T4/2026 foi 61%. |
| C36 | 02_secao2_frentes_propostas | line:12 | A operação mínima proposta eleva o uso de 2027 para 75%. Avaliação independente da LogisVal atribui **R$ 42,00 MM** ao valor econômico dos dois slots sujeitos à perda. A operação isolada tem margem operacional negativa de R$ 3,60 MM no ano. |
| C37 | 02_secao2_frentes_propostas | line:16 | **Pedido:** aprovar substituição dos 16 cabeços críticos de B1 e B2.  
**CAPEX:** 14,00, Fonte A.  
**OPEX incremental:** 4,20.  
**Interdição:** 8 berço-dias, quatro no T1 e quatro no T2. |
| C38 | 02_secao2_frentes_propostas | line:21 | Inspeção certificada encontrou perda de seção acima do limite em 16 cabeços. A Autoridade Portuária determinou correção até 30 de junho de 2027. O laudo SEC-02/2027 classificou o risco como crítico e estimou exposição de R$ 68,00 MM: `probabilidade de ruptura 20% × impacto operacional e indenizatório de 340,00`. |
| C39 | 02_secao2_frentes_propostas | line:25 | **Pedido:** aprovar a extensão em 120 metros, elevando a capacidade licenciável do terminal para 1,25 milhão de TEU/ano.  
**CAPEX:** 88,00, Fonte A.  
**OPEX incremental 2027:** 5,40.  
**Interdição:** 105 berço-dias contínuos de B1, de 15 de maio a 27 de agosto. |
| C40 | 02_secao2_frentes_propostas | line:30 | A Diretoria Comercial estima margem adicional estabilizada de R$ 28,00 MM por ano a partir de 2029. A estimativa depende de contrato ainda não assinado com a Aliança Navega. A carta de intenção da Aliança é não vinculante e expira em 31 de julho de 2027. |
| C41 | 02_secao2_frentes_propostas | line:32 | O método construtivo da proposta exige acesso pelo cais existente e interdição integral de B1. A contratada declara que reduzir a interdição abaixo de 105 dias exigiria novo projeto executivo e nova licitação. |
| C42 | 02_secao2_frentes_propostas | line:36 | **Pedido:** aprovar implantação conjunta com F3.  
**CAPEX:** 22,00, Fonte A.  
**OPEX incremental 2027:** 2,00.  
**Interdição:** 10 berço-dias no T4.  
**Dependência declarada:** energização após conclusão civil de F3 e antes do comissionamento da capacidade ampliada. |
| C43 | 02_secao2_frentes_propostas | line:42 | A Resolução AP-18/2025 exige shore power para terminais cuja capacidade licenciada seja superior a 1,20 milhão de TEU/ano. A licença atual do TPL é de 980 mil TEU/ano. A resolução determina adequação antes da entrada em operação da capacidade que ultrapassar o limiar; não exige retrofit de terminais abaixo dele. |
| C44 | 02_secao2_frentes_propostas | line:46 | **Pedido:** contratar solução TurnGate por dez anos.  
**CAPEX inicial:** 36,00, Fonte A.  
**OPEX incremental/contraprestação anual:** 5,80.  
**Interdição de berço:** 0 dia. |
| C45 | 02_secao2_frentes_propostas | line:51 | A proposta comercial promete benefício bruto anual de R$ 16,40 MM e payback de 3,4 anos, pela fórmula apresentada: `36,00 ÷ (16,40 − 5,80) = 3,40 anos`. |
| C46 | 02_secao2_frentes_propostas | line:53 | O estudo usa a média de cinco terminais de referência, nos quais transbordo representa 55% dos movimentos. O anexo metodológico afirma que 83% do ganho decorre da automação de movimentos de transbordo e reposicionamento. No TPL, transbordo representa 18% dos movimentos. |
| C47 | 02_secao2_frentes_propostas | line:55 | O contrato proposto contém obrigação take-or-pay de R$ 5,80 MM por ano durante dez anos. Rescisão imotivada exige pagamento de 60% das contraprestações vincendas. Essa obrigação não aparece na página-resumo do business case. |
| C48 | 02_secao2_frentes_propostas | line:59 | **Pedido:** migrar do sistema Atlas 7 para o Nexus Port.  
**CAPEX:** 24,00, Fonte A.  
**OPEX incremental 2027:** 10,00.  
**Interdição:** 3 berço-dias no T3 para cutover.  
**Prazo físico:** nove meses entre mobilização e cutover. |
| C49 | 02_secao2_frentes_propostas | line:65 | O suporte padrão do Atlas 7 termina em 30 de junho de 2027. A Diretoria propõe mobilização em 1º de fevereiro e entrada em produção até 30 de junho, sem apresentar compressão técnica para os nove meses requeridos. |
| C50 | 02_secao2_frentes_propostas | line:67 | O contrato Atlas, cláusula 14.6, permite extensão única do suporte por seis meses, até 31 de dezembro de 2027, ao preço de R$ 1,80 MM. A opção deve ser exercida por notificação escrita recebida pelo fornecedor até 30 de abril de 2027. O valor não está incluído no pedido de OPEX de F6. |
| C51 | 02_secao2_frentes_propostas | line:71 | **Pedido:** instalar sensores em portêineres, RTGs e subestações.  
**CAPEX:** 12,00, Fonte A.  
**OPEX incremental 2027:** 4,00.  
**Interdição:** 4 berço-dias, dois no T2 e dois no T3. |
| C52 | 02_secao2_frentes_propostas | line:76 | O projeto produz séries padronizadas de vibração, temperatura, corrente e ciclos operacionais. O laudo de engenharia estima redução anual de R$ 6,00 MM em paradas não planejadas a partir de 2028, independentemente da contratação do módulo de IA de F8. |
| C53 | 02_secao2_frentes_propostas | line:80 | **Pedido:** contratar o módulo PrediCrane em 2027.  
**CAPEX:** 9,00, Fonte A.  
**OPEX incremental:** 1,90.  
**Interdição:** 0 dia.  
**Dependência declarada pelo fornecedor:** dados da plataforma F7. |
| C54 | 02_secao2_frentes_propostas | line:86 | O resumo executivo promete economia de R$ 8,50 MM já em 2027. O caderno técnico, seção 6.2, exige pelo menos 15 meses de telemetria contínua após a estabilização de F7, cobrindo sazonalidade de verão e inverno, antes do primeiro modelo produtivo. Dados históricos do TPL não têm frequência nem taxonomia compatíveis. |
| C55 | 02_secao2_frentes_propostas | line:90 | **Pedido:** executar campanha mínima da licença operacional e protocolar as liberações C2 e C3.  
**Custo de execução:** 20,00, exclusivamente pela Fonte C1.  
**OPEX incremental de fiscalização e documentação:** 2,18.  
**Interdição:** 3 berço-dias no T4. |
| C56 | 02_secao2_frentes_propostas | line:95 | A licença exige recomposição do calado mínimo até 15 de dezembro de 2027. O descumprimento expõe o terminal a suspensão parcial e perda estimada de R$ 75,00 MM: `50 dias de restrição × margem diária de 1,50`. |
| C57 | 02_secao2_frentes_propostas | line:97 | O orçamento de R$ 20,00 MM considera transporte e destinação no Sítio Delta, único destino licenciado disponível. A execução regular gera os documentos necessários à liberação de C3. O protocolo de C2 é administrativamente independente da dragagem, mas foi incluído na mesma frente por compartilhar a equipe documental. |
| C58 | 03_secao3_quadro_diretoria_premissas | line:5 | A Diretoria recomenda aprovar F1, F2, F3, F4, F6, F7 e F9; rejeitar F5; e aprovar F8 apenas se houver saldo no encerramento do T2. |
| C59 | 03_secao3_quadro_diretoria_premissas | line:11 | | F2 | Fonte A | 14,00 |
| F3 | Fonte A | 88,00 |
| F4 | Fonte A | 22,00 |
| F6 | Fonte A | 24,00 |
| F7 | Fonte A | 12,00 |
| **Total Fonte A** |  | **160,00** |
| **CAPEX disponível no ERP** |  | **160,00** |
| **Saldo declarado** |  | **0,00** | |
| C60 | 03_secao3_quadro_diretoria_premissas | line:20 | F9 é apresentado separadamente contra a Fonte C1. F8 não está incluído na alocação inicial. |
| C61 | 03_secao3_quadro_diretoria_premissas | line:24 | | F1 | 3,60 |
| F2 | 4,20 |
| F3 | 5,40 |
| F4 | 2,00 |
| F6 | 10,00 |
| F7 | 4,00 |
| F9 | 2,18 |
| **Total declarado pela Diretoria** | **30,98** |
| **Teto de custeio** | **31,00** |
| **Folga declarada** | **0,02** | |
| C62 | 03_secao3_quadro_diretoria_premissas | line:37 | A Diretoria afirma que “todo o custeio incremental, inclusive segurança e regulação, consome o teto de R$ 31,00 MM”. A extensão de suporte de F6 não foi incluída. |
| C63 | 03_secao3_quadro_diretoria_premissas | line:41 | | F2 | 4 dias | 4 dias | — | — |
| F3 | — | 47 dias | 58 dias | — |
| F4 | — | — | — | 10 dias |
| F6 | — | — | 3 dias | — |
| F7 | — | 2 dias | 2 dias | — |
| F9 | — | — | — | 3 dias | |
| C64 | 03_secao3_quadro_diretoria_premissas | line:50 | a nova capacidade criada por F3 compensará a interdição durante a própria obra |
| C65 | 03_secao3_quadro_diretoria_premissas | line:56 | O limite absoluto de CAPEX disponível em 2027 é R$ 160,00 MM. |
| C66 | 03_secao3_quadro_diretoria_premissas | line:57 | Todo OPEX incremental, inclusive segurança crítica e obrigação regulatória, consome o teto de R$ 31,00 MM. |
| C67 | 03_secao3_quadro_diretoria_premissas | line:58 | Shore power é obrigação vigente dos berços atuais e F4 deve ocorrer mesmo sem F3. |
| C68 | 03_secao3_quadro_diretoria_premissas | line:59 | A migração F6 precisa entrar em produção até 30/06/2027; não existe alternativa contratual de suporte. |
| C69 | 03_secao3_quadro_diretoria_premissas | line:60 | O perfil dos terminais usados pela TurnGate é representativo do TPL e sustenta o payback de F5. |
| C70 | 03_secao3_quadro_diretoria_premissas | line:61 | O máximo anual de 70 berço-dias de interdição e o máximo trimestral de 20 não podem ser excedidos em 2027. |
| C71 | 03_secao3_quadro_diretoria_premissas | line:62 | O covenant de Dívida Líquida/EBITDA de 3,50 vezes impede dívida adicional além da folga demonstrada. |
| C72 | 03_secao3_quadro_diretoria_premissas | line:63 | O material dragado não pode ser destinado à Célula Alfa e deve seguir para o Sítio Delta. |
| C73 | 04_anexos_operacionais_financeiros_regulatorios | line:5 | Se o Usuário utilizar menos de 70% dos slots reservados por dois trimestres civis consecutivos, a Concessionária poderá cancelar, de modo definitivo e sem obrigação de reposição, dois dos quatro slots semanais. O cancelamento não gera indenização. |
| C74 | 04_anexos_operacionais_financeiros_regulatorios | line:9 | Das cauções elegíveis entre 2022 e 2026, 62% foram recuperadas. Dos 38% não recuperados, 21 pontos percentuais decorreram de protocolo posterior ao prazo, 12 pontos de certidão ausente e cinco pontos de ausência de responsável designado. Nos processos completos e tempestivos, não houve indeferimento por falta de direito material. |
| C75 | 04_anexos_operacionais_financeiros_regulatorios | line:11 | Para C2, todos os marcos contratuais foram cumpridos. Faltam emitir duas certidões e protocolar o termo de encerramento. Prazo estimado para montar o dossiê: 20 dias úteis. |
| C76 | 04_anexos_operacionais_financeiros_regulatorios | line:15 | Terminais com capacidade anual licenciada superior a 1.200.000 TEU deverão dispor de conexão elétrica para navios antes da entrada em operação da capacidade excedente. Terminais com capacidade igual ou inferior ao limiar ficam dispensados, sem prejuízo de adesão voluntária. |
| C77 | 04_anexos_operacionais_financeiros_regulatorios | line:19 | O Cliente poderá estender uma única vez o suporte do Atlas 7 por seis meses, mediante notificação recebida até 30 de abril de 2027 e pagamento de R$ 1.800.000,00. Durante a extensão serão mantidos patches críticos e atendimento de severidade 1. |
| C78 | 04_anexos_operacionais_financeiros_regulatorios | line:23 | O payback de 3,4 anos usa benefício bruto anual de R$ 16,40 MM e contraprestação anual de R$ 5,80 MM. A amostra de referência tem 55% de transbordo. O próprio anexo de sensibilidade informa que 83% do benefício é proporcional ao volume de transbordo e reposicionamento. |
| C79 | 04_anexos_operacionais_financeiros_regulatorios | line:25 | Cláusula 19: prazo mínimo de dez anos. Em caso de rescisão imotivada, o cliente paga 60% das contraprestações vincendas, trazidas a valor nominal na data da rescisão. |
| C80 | 04_anexos_operacionais_financeiros_regulatorios | line:29 | O treinamento produtivo requer no mínimo 15 meses contínuos de telemetria após estabilização dos sensores, com cobertura de ciclos sazonais. Séries agregadas de manutenção não substituem os sinais brutos. Antes disso, os resultados são experimentais e não devem ser reconhecidos como economia contratada. |
| C81 | 04_anexos_operacionais_financeiros_regulatorios | line:33 | Decisão transitada em julgado proibiu definitivamente a disposição de sedimentos do TPL na Célula Alfa. O Sítio Delta possui licença válida e capacidade reservada para a campanha de 2027. O orçamento de F9 já incorpora o transporte adicional ao Sítio Delta. |
| C82 | 04_anexos_operacionais_financeiros_regulatorios | line:39 | | F2 | Laudo SEC-02 | Concluir até 30/06/2027 | |
| C83 | 04_anexos_operacionais_financeiros_regulatorios | line:40 | | F3 | Novo projeto executivo se houver mudança de método | Método atual exige 105 dias contínuos | |
| C84 | 04_anexos_operacionais_financeiros_regulatorios | line:41 | | F4 | F3 civilmente concluída | Energizar antes de comissionar capacidade acima de 1,20 milhão de TEU | |
| C85 | 04_anexos_operacionais_financeiros_regulatorios | line:42 | | F6 | Extensão Atlas se cutover ocorrer após 30/06 | Nove meses entre mobilização e cutover | |
| C86 | 04_anexos_operacionais_financeiros_regulatorios | line:43 | | F7 | Nenhum | Estabilização prevista 30 dias após instalação | |
| C87 | 04_anexos_operacionais_financeiros_regulatorios | line:44 | | F8 | F7 estabilizada + 15 meses de dados | Primeiro modelo produtivo somente depois da janela de dados | |
| C88 | 04_anexos_operacionais_financeiros_regulatorios | line:45 | | F9 | Reserva do Sítio Delta | Concluir até 15/12/2027 | |
| C89 | 04_anexos_operacionais_financeiros_regulatorios | line:51 | | Perda dos dois slots ferroviários | Avaliação independente: 42,00 |
| Ruptura de cabeço crítico | 20% × 340,00 = 68,00 |
| Restrição de calado por não executar F9 | 50 dias × 1,50/dia = 75,00 |
| Perda de C2 por decadência | 8,00 |
| Perda de C3 por decadência ou destinação irregular | 6,00 |
| Suporte estendido do Atlas | Custo certo de 1,80 se a opção for exercida |
| Operação do Atlas sem suporte entre julho e outubro | 25% de incidente severo × impacto de 48,00 = 12,00 |
| Paradas não planejadas mitigáveis por F7 | 6,00 por ano a partir de 2028 |
| Compromisso prematuro de F8 antes de dados utilizáveis | 9,00 + 1,90 = 10,90 |
| Rescisão de F5 ao fim do primeiro ano | 60% × 9 anos restantes × 5,80 = 31,32 | |
| C90 | 04_anexos_operacionais_financeiros_regulatorios | line:64 | O Conselho não exige aprovação de projeto de crescimento em 2027. Exige que qualquer saldo material tenha destinação declarada: `alocado`, `reserva com gatilho`, `devolvido` ou `retido sem uso justificado`. |
| C91 | 04_anexos_operacionais_financeiros_regulatorios | line:66 | Uma recomendação de diferimento deve indicar data, dono e condição objetiva de reentrada. Uma recomendação de aprovação condicionada não pode contabilizar benefício antes do cumprimento da condição. |
| C92 | 03_secao3_quadro_diretoria_premissas | line:33 | | **Total declarado pela Diretoria** | **30,98** | |

## 10. Afirmações sem Consequência
- [C01] Contexto de concessão; não alterou alocação.
- [C02] Contexto de ativos; não alterou alocação.
- [C03] Contexto de movimentação e licença; não alterou decisão.
- [C07] Contexto de indisponibilidade de recursos alternativos; não alterou decisão.
- [C08] Contexto de exigência de contrato e certificação; não alterou decisão.
- [C13] Covenant; não houve contratação de dívida nova.
- [C14] Projeção de covenant; não houve dívida nova.
- [C15] Ausência de waiver; não houve dívida nova.
- [C16] Definição de dívida; não houve dívida nova.
- [C26] Total de vinculados; usado apenas para reconciliação.
- [C27] Histórico de recuperação; usado como contexto de C2/C3.
- [C28] Causas de perda; usado como contexto de C2/C3.
- [C29] Regra de vinculação; usado como contexto de C2/C3.
- [C58] Recomendação da Diretoria; não adotada integralmente.
- [C59] Alocação de CAPEX da Diretoria; corrigida.
- [C60] Separação de F9 e F8; corrigida.
- [C61] Custeio da Diretoria; corrigido.
- [C62] Afirmação da Diretoria sobre teto; refutada.
- [C63] Cronograma da Diretoria; ajustado.
- [C64] Nota de rodapé; refutada.

## 11. Apêndice de Cálculo e Memória Aritmética
- CAPEX disponível: 160,00 + 18,00 = 178,00
- CAPEX alocado: 14,00 + 24,00 + 12,00 = 50,00
- Saldo CAPEX: 178,00 − 50,00 = 128,00
- OPEX cap consumido: 3,60 + 11,80 + 4,00 = 19,40
- OPEX exempt: 4,20 + 2,18 = 6,38
- OPEX total: 19,40 + 6,38 = 25,78
- Folga OPEX: 31,00 − 19,40 = 11,60
- D-001: 3,60 + 4,20 + 5,40 + 2,00 + 10,00 + 4,00 + 2,18 = 31,38; 31,38 − 30,98 = 0,40. Adotado 31,38 para soma bruta; após exclusões e diferimentos, OPEX deliberado = 25,78.
- Interdição: rotina 13 × 4 = 52; projetos 8 + 3 + 4 + 3 = 18; total 52 + 18 = 70; saldo 0.
- Trimestres: T1 13 + 4 = 17; T2 13 + 4 + 2 = 19; T3 13 + 2 = 15; T4 13 + 3 + 3 = 19.
- F5 payback ajustado: 16,40 × 0,83 = 13,612; 13,612 × 18/55 = 4,455; 16,40 × 0,17 = 2,788; total = 7,243; líquido = 7,243 − 5,80 = 1,443; payback = 36,00 ÷ 1,443 = 24,95.
- F5 rescisão: 60% × 9 × 5,80 = 31,32.
- F2 exposição: 20% × 340,00 = 68,00.
- F9 exposição: 50 × 1,50 = 75,00.
- F6 sem suporte: 25% × 48,00 = 12,00.
- F8 prematuro: 9,00 + 1,90 = 10,90.
- C2/C3: 8,00 + 6,00 = 14,00.
responde: MUST-10