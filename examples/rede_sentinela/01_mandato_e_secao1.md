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

