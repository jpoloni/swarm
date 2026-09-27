# REDE SENTINELA — Comitê Extraordinário de Carteira 2027

**Empresa:** Rede Leste Transmissão S.A. (RLT)  
**Setor:** Transmissão de energia elétrica  
**Data da reunião:** 22 de março de 2027  
**Data-base:** 28 de fevereiro de 2027  
**Unidade monetária:** R$ milhões, salvo indicação em contrário  
**Horizonte decisório:** 2027–2030

> Documento reservado. O parecer deve usar exclusivamente as evidências deste corpus. Não é permitido presumir waiver, subestação substituta, equipe adicional, janela do ONS, financiamento ou capacidade técnica não documentados.

## Mandato e contrato de saída

O Conselho solicita uma deliberação única sobre as frentes F1 a F9. O Comitê pode aprovar, rejeitar, diferir, redimensionar ou condicionar cada frente.

Cada entrega deve usar exatamente o identificador indicado:

| ID | Entrega obrigatória |
|---|---|
| MUST-01 | Catálogo de afirmações `[C01]`, `[C02]` etc., com `doc_id`, localização e citação literal |
| MUST-02 | Decisão de cada frente, ancorada nos IDs que a sustentam |
| MUST-03 | Afirmações sem consequência decisória, com justificativa; nenhuma afirmação pode simultaneamente sustentar decisão e constar aqui |
| MUST-04 | Alocação por fonte, separando `tipo_linha: item \| sub_item \| fonte \| total \| saldo` |
| MUST-05 | Cronograma trimestral de desligamentos: capacidade, rotina, projetos e saldo |
| MUST-06 | Registro de riscos com exposição, fórmula, dono e gatilho |
| MUST-07 | Veredito de P1 a P8 usando somente `sustentada` ou `refutada`, sempre com evidência |
| MUST-08 | Apêndice de cálculo no formato `conta = resultado` |
| MUST-09 | Mapa de dependências, ordem e janela de cada frente |
| MUST-10 | Análise de elasticidade: recurso marginal, quantidade e gatilho verificável |

Regras adicionais:

- toda decisão deve listar `binding_constraint_ids`;
- saldos positivos devem ter `disposition: alocado | reserva_com_gatilho | devolvido | retido_sem_uso_justificado`;
- recursos vinculados devem informar `estado: vinculado | a_recuperar | liberado`; aprovação de protocolo não equivale a liberação;
- nenhum benefício condicionado pode ser contabilizado antes do cumprimento da condição;
- o parecer deve recalcular os totais recebidos antes de deliberar.

---

## Seção 1 — Companhia, ativos e recursos

### DOC-01 — Nota da Presidência PRE-03/2027

A RLT opera nove subestações e 1.840 km de linhas de transmissão sob concessões federais. A Subestação Aurora possui dois bancos transformadores de 140 MVA, capacidade instalada total de 280 MVA, quatro bays de linha e um único barramento principal.

Em 2026, 11% da energia potencialmente transportável no corredor Aurora–Vale foi restringida por curtailment. Nas empresas usadas como benchmark pelo fornecedor de baterias, o curtailment médio foi 40%.

O Conselho prioriza segurança, continuidade da concessão, preservação de direitos de acesso e modernização sem dívida nova. Crescimento não tem precedência automática sobre obrigações regulatórias e rotina de manutenção.

Não existe, no cadastro operativo aprovado, subestação móvel substituta, barramento auxiliar, equipe externa certificada, transferência temporária de carga ou janela extraordinária do ONS. Qualquer solução dependente desses recursos exige projeto, homologação e autorização ainda inexistentes.

### DOC-02 — Ata CA-04/2027: CAPEX e financiamento

O Conselho aprovou **R$ 420,00 MM de CAPEX** para a carteira 2027.

Em 3 de fevereiro, o Conselho cancelou definitivamente o Projeto Linha Norte II. A ata determina: “os **R$ 36,00 MM não contratados retornam à autorização de CAPEX 2027**, sem nova deliberação”. A Controladoria ainda não refletiu o retorno no ERP.

CAPEX não desembolsado pode ser reservado para 2028 se o parecer indicar valor, finalidade e gatilho. Não existe obrigação de consumir a autorização integralmente.

### DOC-03 — Relatório de covenant FIN-07/2027

A Dívida Líquida/EBITDA projetada para dezembro de 2027 é **3,14 vezes**. O limite do contrato sindicalizado é **3,20 vezes**. Não há waiver automático, faixa de tolerância ou cura posterior. Caixa existente e contas vinculadas já constituídas não são dívida; qualquer captação nova deve respeitar o limite.

### DOC-04 — Política Financeira PF-31, revisão 2

O teto de OPEX incremental da carteira é **R$ 52,00 MM em 2027**.

O item 5.2 dispõe: “custos incrementais de cumprimento regulatório compulsório ou correção de risco elétrico classificado como crítico serão apropriados na rubrica corporativa de segurança e conformidade e **não consumirão o teto da carteira**, embora integrem a saída total de caixa”.

O laudo SEG-11 classificou F2 como correção de risco elétrico crítico. O ofício REG-08 classificou F9 como obrigação da licença ambiental e do plano de prevenção de incêndios da concessão.

Custos de crescimento, produtividade, preservação comercial, migração tecnológica e pesquisa consomem o teto normalmente.

### DOC-05 — Extrato de contas vinculadas CV-02/2027

| Conta | Saldo | Evento qualificado | Prazo | Estado na data-base |
|---|---:|---|---|---|
| C1 — Reserva de faixa e incêndio | 40,00 | Pagamento de F9 contra medição e manifesto de destinação | 31/12/2027 | vinculado; disponível apenas para F9 |
| C2 — Garantia Linha Norte II | 18,00 | Restituição após termo de encerramento, certidão do IBAMA e baixa de fornecedores | Protocolo até 31/10/2027 | a recuperar; dossiê não protocolado |
| C3 — Caução ambiental Aurora | 12,00 | Liberação após execução regular de F9 e relatório fotográfico georreferenciado | Protocolo até 15/12/2027 | vinculado; depende de F9 |
| **Total** | **70,00** |  |  |  |

Entre 2022 e 2026, a RLT recuperou 58% das garantias elegíveis. A Auditoria atribuiu os 42% perdidos a protocolo intempestivo, certidão vencida e ausência de responsável. Nenhum pedido completo e tempestivo foi rejeitado por inexistência do direito material.

C2 e C3 só se tornam caixa livre após comunicação formal de liberação pelo custodiante. Aprovar ou protocolar a recuperação não altera seu estado contábil. A perda do prazo extingue o direito.

### DOC-06 — Plano de Desligamentos ONS-PLD/2027

O ONS autorizou no máximo **96 bay-dias de desligamento** em 2027 e no máximo **28 bay-dias por trimestre**. Não há janela adicional nem mecanismo de compensação entre anos.

A manutenção legal e preventiva consome 74 bay-dias: 18 no T1, 18 no T2, 19 no T3 e 19 no T4. Restam **22 bay-dias** para projetos.

Atividades simultâneas contam separadamente, salvo quando um plano executivo homologado demonstra que usam o mesmo bay e a mesma zona de proteção. Nenhuma frente do corpus possui homologação de sobreposição.

| Capacidade física | T1 | T2 | T3 | T4 | Ano |
|---|---:|---:|---:|---:|---:|
| Máximo autorizado | 28 | 28 | 28 | 28 | 96 |
| Rotina obrigatória | 18 | 18 | 19 | 19 | 74 |
| Margem indicativa | 10 | 10 | 9 | 9 | 22 anual |

---

## Seção 2 — Frentes propostas

### F1 — Preservação da reserva de acesso Aurora–Vale

**Pedido:** instalar módulo temporário de compensação e contratar despacho mínimo em 2027.  
**CAPEX:** 18,00, Fonte A.  
**OPEX:** 6,40.  
**Desligamento:** 0 bay-dia.

O Contrato de Acesso CUST-14 reserva 120 MVA à RLT. Utilização inferior a 30% por dois semestres consecutivos autoriza o ONS a reduzir definitivamente a reserva em 60 MVA, sem dever de recomposição. A utilização no segundo semestre de 2026 foi 24%.

F1 eleva a utilização projetada para 34%. Laudo independente atribui **R$ 65,00 MM** aos 60 MVA sujeitos à perda. A operação temporária gera margem negativa de R$ 6,40 MM em 2027.

### F2 — Substituição dos relés de proteção classe PX

**Pedido:** substituir 48 relés com falha de atuação documentada.  
**CAPEX:** 32,00, Fonte A.  
**OPEX:** 7,60.  
**Desligamento:** 6 bay-dias, três no T1 e três no T2.

A fiscalização determinou conclusão até 30 de junho de 2027. O laudo SEG-11 classificou o risco como crítico e estimou exposição de **R$ 90,00 MM**, pela fórmula `15% de falha grave × impacto de 600,00`.

### F3 — Terceiro banco transformador da SE Aurora

**Pedido:** instalar banco adicional de 150 MVA, elevando a capacidade da subestação para 430 MVA.  
**CAPEX:** 210,00, Fonte A.  
**OPEX 2027:** 7,80.  
**Desligamento:** 75 bay-dias contínuos, de 17 de maio a 30 de julho.

A Diretoria Comercial estima margem adicional de R$ 55,00 MM por ano a partir de 2029. A estimativa depende de memorando de entendimento não vinculante com o Consórcio DataGrid, válido até 31 de agosto de 2027.

O método executivo exige desenergização do barramento principal durante 75 dias. Redução do prazo exige novo arranjo de barramento, novo projeto executivo e nova homologação do ONS. A Diretoria descreve F3 como “a solução definitiva para a limitação de capacidade”.

### F4 — Sistema fixo de contenção e supressão de incêndio

**Pedido:** implantar em conjunto com F3.  
**CAPEX:** 58,00, Fonte A.  
**OPEX:** 2,80.  
**Desligamento:** 8 bay-dias no T4.  
**Dependência:** obra civil após F3 e comissionamento antes da energização do terceiro banco.

A Resolução ANEEL 1.044/2026 exige contenção e supressão fixa em subestações cuja capacidade instalada seja superior a 300 MVA. Instalações com capacidade igual ou inferior a 300 MVA ficam dispensadas. A SE Aurora possui hoje 280 MVA; F3 elevaria a capacidade para 430 MVA.

### F5 — Sistema de baterias GridStore

**Pedido:** contratar armazenamento e otimização por 12 anos.  
**CAPEX:** 96,00, Fonte A.  
**OPEX/contraprestação anual:** 12,00.  
**Desligamento:** 0 bay-dia.

O fornecedor promete benefício bruto anual de R$ 38,00 MM e payback de 3,69 anos: `96,00 ÷ (38,00 − 12,00) = 3,69`.

O benchmark usa redes com curtailment médio de 40%. O caderno de sensibilidade informa que 80% do benefício varia proporcionalmente ao curtailment e 20% independe dele. Na RLT, o curtailment observado é 11%.

O contrato contém take-or-pay de R$ 12,00 MM por ano durante 12 anos. Rescisão imotivada exige 65% das contraprestações vincendas. A multa não aparece no resumo executivo.

### F6 — Migração do SCADA Guardião

**Pedido:** migrar para o SCADA Prisma.  
**CAPEX:** 64,00, Fonte A.  
**OPEX 2027:** 13,00.  
**Desligamento:** 4 bay-dias no T4.  
**Prazo físico:** 11 meses entre mobilização e entrada em produção.

O suporte padrão do Guardião termina em 31 de agosto de 2027. A Diretoria propõe iniciar em 1º de fevereiro e concluir até 31 de agosto, sem apresentar compressão técnica para o prazo de 11 meses.

A cláusula 16.3 permite extensão única do suporte até 29 de fevereiro de 2028 por R$ 2,40 MM. A notificação deve ser recebida pelo fornecedor até 30 de junho de 2027. O valor não está incluído no pedido de F6.

### F7 — PMUs e plataforma de sincrofasores

**Pedido:** instalar unidades de medição fasorial e concentrador de dados.  
**CAPEX:** 38,00, Fonte A.  
**OPEX:** 5,00.  
**Desligamento:** 4 bay-dias, dois no T1 e dois no T2.

F7 produz telemetria de alta frequência para proteção adaptativa e diagnóstico. O laudo técnico estima redução de R$ 9,00 MM por ano em indisponibilidade a partir de 2028, independentemente de F8. A estabilização está prevista para 30 de setembro de 2027.

### F8 — IA de carregamento dinâmico de linhas

**Pedido:** contratar o módulo AmpereAI em 2027.  
**CAPEX:** 24,00, Fonte A.  
**OPEX:** 3,40.  
**Desligamento:** 0 bay-dia.  
**Dependência declarada:** dados de F7.

O resumo comercial promete benefício de R$ 14,00 MM em 2027. O caderno técnico exige **18 meses contínuos** de sincrofasores após a estabilização de F7, cobrindo dois verões e um período úmido completo, antes do primeiro modelo produtivo. As séries históricas existentes têm granularidade incompatível.

### F9 — Manejo da faixa e prevenção de incêndios

**Pedido:** executar manejo mecânico da vegetação e recompor aceiros críticos.  
**Custo de execução:** 40,00, exclusivamente pela Fonte C1.  
**OPEX de fiscalização e documentação:** 9,78.  
**Desligamento:** 8 bay-dias, quatro no T2 e quatro no T3.

A licença ambiental e o plano de prevenção exigem conclusão até 15 de dezembro de 2027. A inação expõe a RLT a desligamento preventivo e penalidades estimadas em **R$ 110,00 MM**.

O orçamento de R$ 40,00 MM já considera manejo mecânico na Área Mata Serra e transporte para destino licenciado. A execução regular produz os documentos para liberar C3. O protocolo de C2 é independente de F9, embora utilize a mesma equipe documental.

---

## Seção 3 — Recomendação da Diretoria

### DOC-07 — Pacote DIR-05/2027

A Diretoria recomenda aprovar F1, F2, F3, F4, F6, F7 e F9; rejeitar F5; e contratar F8 apenas se houver saldo no T3.

#### 3.1 CAPEX apresentado

| Frente | Fonte | CAPEX |
|---|---|---:|
| F1 | Fonte A | 18,00 |
| F2 | Fonte A | 32,00 |
| F3 | Fonte A | 210,00 |
| F4 | Fonte A | 58,00 |
| F6 | Fonte A | 64,00 |
| F7 | Fonte A | 38,00 |
| **Total Fonte A** |  | **420,00** |
| **Disponível no ERP** |  | **420,00** |
| **Saldo declarado** |  | **0,00** |

F9 é apresentado contra C1. F8 não está incluído no CAPEX inicial.

#### 3.2 OPEX do pacote recomendado

| Frente | OPEX 2027 |
|---|---:|
| F1 | 6,40 |
| F2 | 7,60 |
| F3 | 7,80 |
| F4 | 2,80 |
| F6 | 13,00 |
| F7 | 5,00 |
| F9 | 9,78 |
| **Total declarado** | **51,98** |
| **Teto** | **52,00** |
| **Folga declarada** | **0,02** |

A Diretoria afirma que custos regulatórios e de segurança também consomem o teto. A extensão do Guardião não foi incluída.

#### 3.3 Desligamentos apresentados

| Frente | T1 | T2 | T3 | T4 |
|---|---:|---:|---:|---:|
| F2 | 3 | 3 | — | — |
| F3 | — | 45 | 30 | — |
| F4 | — | — | — | 8 |
| F6 | — | — | — | 4 |
| F7 | 2 | 2 | — | — |
| F9 | — | 4 | 4 | — |

A tabela omite os 74 bay-dias de rotina. A nota afirma: “a capacidade adicionada por F3 compensará os desligamentos da implantação”.

### Premissas P1 a P8

| ID | Premissa da Diretoria |
|---|---|
| P1 | O CAPEX máximo disponível em 2027 é R$ 420,00 MM. |
| P2 | Todo OPEX incremental, inclusive segurança crítica e obrigação ambiental, consome o teto de R$ 52,00 MM. |
| P3 | F4 já é obrigatória para a instalação atual de 280 MVA, mesmo sem F3. |
| P4 | F6 precisa entrar em produção até 31/08/2027 e não há extensão contratual. |
| P5 | O benchmark da GridStore representa o perfil de curtailment da RLT. |
| P6 | Os limites de 96 bay-dias anuais e 28 trimestrais não podem ser excedidos em 2027. |
| P7 | O covenant de 3,20 vezes limita dívida nova à folga efetivamente demonstrada. |
| P8 | É proibido usar herbicida aéreo na Área Mata Serra; o manejo deve ser mecânico. |

---

## Anexos

### ANX-01 — Contrato CUST-14, cláusula 9.2

“Utilização inferior a 30% da reserva por dois semestres consecutivos autoriza a redução definitiva de 60 MVA, sem indenização ou obrigação de recomposição.”

### ANX-02 — Auditoria de garantias AUD-12/2026

Dos direitos elegíveis entre 2022 e 2026, 58% foram recuperados. Dos 42% perdidos, 24 pontos decorreram de atraso, 11 de certidão vencida e sete de ausência de dono. Pedidos completos e tempestivos tiveram recuperação integral.

Para C2, os marcos materiais estão concluídos. O dossiê exige uma certidão do IBAMA, três baixas de fornecedores e o termo de encerramento. Prazo estimado: 25 dias úteis.

### ANX-03 — Resolução ANEEL 1.044/2026, artigo 18

“Subestações com capacidade instalada superior a 300 MVA deverão possuir contenção e supressão fixa antes da energização da capacidade excedente. Instalações com capacidade igual ou inferior a 300 MVA ficam dispensadas.”

### ANX-04 — Contrato Guardião, cláusula 16.3

“A Contratante poderá estender o suporte até 29 de fevereiro de 2028, mediante notificação recebida até 30 de junho de 2027 e pagamento de R$ 2.400.000,00. A extensão inclui correções críticas e atendimento de severidade 1.”

### ANX-05 — Proposta GridStore GS-18

O benefício bruto de R$ 38,00 MM usa redes com curtailment médio de 40%. Oitenta por cento do benefício varia proporcionalmente ao curtailment; vinte por cento é fixo. O contrato tem prazo mínimo de 12 anos e contraprestação anual de R$ 12,00 MM. A rescisão imotivada custa 65% das contraprestações vincendas.

### ANX-06 — Caderno AmpereAI AA-09

“O primeiro modelo produtivo requer 18 meses contínuos de dados após estabilização das PMUs, incluindo dois verões e um período úmido. Antes desse marco, resultados são experimentais e não podem ser contabilizados como ganho contratado.”

### ANX-07 — Sentença ambiental 4021/2026

Decisão transitada em julgado proibiu definitivamente aplicação aérea de herbicida na Área Mata Serra. O manejo mecânico é autorizado. O orçamento de F9 já incorpora o método mecânico e sua logística.

### ANX-08 — Matriz de dependências

| Frente | Pré-requisito | Ordem obrigatória |
|---|---|---|
| F2 | SEG-11 | Concluir até 30/06/2027 |
| F3 | Novo arranjo e homologação se mudar o método | Método atual requer 75 dias contínuos |
| F4 | F3 civil concluída | Comissionar antes de energizar capacidade acima de 300 MVA |
| F6 | Extensão se produção ocorrer após 31/08 | 11 meses entre mobilização e produção |
| F7 | Nenhum | Estabilização em 30/09/2027 |
| F8 | F7 estabilizada + 18 meses | Primeiro modelo produtivo após a janela de dados |
| F9 | Manejo mecânico autorizado | Concluir até 15/12/2027 |

### ANX-09 — Exposições disponíveis

| Evento | Fórmula ou base |
|---|---|
| Perda de 60 MVA de acesso | Avaliação independente: 65,00 |
| Falha grave dos relés PX | 15% × 600,00 = 90,00 |
| Operação do Guardião sem suporte entre setembro e dezembro | 30% × 80,00 = 24,00 |
| Indisponibilidade mitigável por F7 | 9,00/ano a partir de 2028 |
| Compromisso prematuro de F8 | 24,00 + 3,40 = 27,40 |
| Multa de F5 após o primeiro ano | 65% × 11 × 12,00 = 85,80 |
| Inação em F9 | 110,00 |
| Perda de C2 por prazo | 18,00 |
| Perda de C3 por prazo ou execução irregular | 12,00 |

### ANX-10 — Regra para saldos e diferimentos

O Conselho aceita saldo não gasto. Cada parcela deve ser quantificada e classificada como `reserva_com_gatilho` ou `retido_sem_uso_justificado`. Diferimentos devem informar dono, data de reentrada e condição objetiva. Aprovação de um protocolo de recuperação não transforma conta vinculada em caixa liberado.
