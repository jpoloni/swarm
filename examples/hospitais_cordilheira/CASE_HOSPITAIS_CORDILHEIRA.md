# Hospitais Cordilheira S.A. — Pacote PEEA 2027 + Medidas Q4/2026
**Reunião da Diretoria Executiva:** 16/09/2026 · **Entrega do parecer ao Conselho:** 23/09/2026 · **Conselho de Administração:** 30/09/2026

*(Empresa, pessoas, contratos, normas e decisões judiciais fictícios. Qualquer semelhança com entidades reais é coincidência.)*

## Como usar este dossiê
Todo documento tem um doc_id canônico (DOC-00 a DOC-27). Todo fato extraído pelo avaliador deve ser citado como [Cxx] com doc_id e citação literal. Organização:

- DOC-00 — Termo de Referência (a tarefa do parecer)
- Seção 1 (DOC-01) — Contexto da empresa, ativos, restrições e recursos
- Seção 2 (DOC-02) — Frentes propostas F1–F9 pela Diretoria
- Seção 3 (DOC-03) — Quadro consolidado da Diretoria e premissas P1–P8
- Anexos operacionais e financeiros — DOC-04 a DOC-10, DOC-16, DOC-26, DOC-27
- Anexos regulatórios e técnicos — DOC-11 a DOC-15, DOC-17 a DOC-25

**Glossário mínimo:**
- **CC** = centro cirúrgico;
- **CME** = central de material e esterilização;
- **LINAC** = acelerador linear de radioterapia;
- **RT** = radioterapia;
- **sala-dia** = unidade de capacidade física do bloco cirúrgico (1 sala ocupada/indisponível por 1 dia);
- **NR-13** = inspeção legal de caldeiras e vasos sob pressão;
- **HVAC** = climatização;
- **take-or-pay** = obrigação de pagar mínimo contratual, consume ou não;
- **glosa** = negativa de faturamento pela operadora.

---

## DOC-00 — Termo de Referência da Consultoria (extrato)

A Diretoria contratou parecer técnico externo para a reunião do Conselho de Administração de 30/09/2026. O parecer deve avaliar o pacote PEEA (DOC-02/DOC-03) e as medidas de emergência do Q4/2026, e obrigatoriamente conter:

1. **Afirmações com ID canônico** — todo fato extraído recebe [Cxx] com doc_id e citação literal.
2. **Decisões ancoradas** — toda decisão cita os IDs das afirmações que a sustentam.
3. **Afirmações sem consequência** — seção listando claims extraídas que não alteraram decisões, com justificativa.
4. **Tabela de alocação por fonte** — coluna de destino separada da coluna de fonte, com saldos e sobras explicitados (CAPEX; custeio; rubrica compulsória 3.9.1; recursos vinculados; físico/sala-dias).
5. **Cronograma físico por trimestre** — capacidade física líquida vs. rotina vs. projetos, em sala-dias.
6. **Registro de riscos** — Item/Frente, Exposição financeira (R$ MM), Dono, Gatilho de escalonamento.
7. **Premissas contestadas** — citação, evidência que a enfraquece e efeito de tratá-la como negociável; premissas que se sustentam devem ser declaradas como tal.
8. **Apêndice de cálculo** — fórmulas no formato conta = resultado, recalculando tudo do zero.

**Prazo de entrega:** 23/09/2026, 12h. A ausência de qualquer um dos 8 itens invalida o parecer.

---

## SEÇÃO 1 — CONTEXTO

### DOC-01 — Contexto da empresa, ativos e recursos

**Empresa.** Hospitais Cordilheira S.A. (HCS), rede privada de saúde: Hospital Central Cordilheira (HCC) — hospital geral de 280 leitos, 12 salas cirúrgicas, 32 leitos de UTI — e 2 unidades ambulatoriais. Receita líquida 2025: R$ 412,0 MM; EBITDA 2025: R$ 84,2 MM. Clientes: operadora Omega Saúde (38% da receita), demais operadoras e particulares.

**Bloco cirúrgico.** 12 salas. Ocupação eletiva de 89,3% (rotina de 3.912 sala-dias sobre 4.380 disponíveis); ~17.200 cirurgias/ano (4,4 por sala-dia); margem de contribuição anual atrelada ao bloco: R$ 42,5 MM. Sazonalidade: cirurgia eletiva cai em janeiro (férias coletivas médicas — o único bloco de ociosidade conjunta do ano).

**Radioterapia (em crise).** Habilitação de alto custo com 1 LINAC de 9 anos (vida útil técnica de referência: 10). Disponibilidade caiu de 89% (2024) para 68% (2026) por falhas repetidas de magnetron e guia de onda. Regulamento técnico do Ministério da Saúde (RT-MS 11/2024): produção mínima de 11.000 sessões/ano; abaixo de 90% do mínimo por 2 exercícios consecutivos → desabilitação do serviço (re-habilitação em 18–24 meses); abaixo de 60% em qualquer exercício → desabilitação imediata. Histórico: 2024 = 10.120 (92,0%); 2025 = 9.790 (89,0% — primeiro exercício abaixo de 90%); previsão 2026 sem operação de reforço: 8.910 (81,0%). Margem de contribuição da RT: R$ 11,8 MM/ano.

**Demais ativos.** CME com capacidade física de 2.450 instrumentais/dia e demanda de 2.380 (97%); 2 ressonâncias (1,5T e 3T), 1 tomógrafo, 1 angiô (214 mil exames/ano); 480 bombas de infusão (32% acima da vida útil, 287 quebras em 2025); 2 caldeiras e vasos sob pressão (CME); climatização central (chillers) do bloco cirúrgico.

**Contrato Omega vigente (n. 55/2024, até 31/12/2028).** Cláusula 7.2: "manutenção de no mínimo 10 salas cirúrgicas operacionais em horário útil; descumprimento → redução de 12% sobre o faturamento cirúrgico Omega do período de descumprimento". Glosas da Omega sobre a HCS em 2025: R$ 5,3 MM.

**Recursos para o ciclo (não fungíveis entre si — política PO-12, DOC-07):**
- **Fonte A — CAPEX 2027:** teto aprovado pelo Conselho de R$ 42,0 MM (DOC-06). Obras em andamento já comprometem R$ 36,5 MM. O extrato do módulo de investimentos do ERP reporta saldo disponível de R$ 5,5 MM (DOC-16).
- **Fonte B — Custeio incremental 2027:** teto rígido de R$ 16,0 MM (DOC-05). A Política Financeira PO-12, Art. 4º, §2º, prevê rubrica própria (3.9.1 — Despesas Compulsórias Regulatórias e de Segurança Assistencial) que não consome o teto de custeio.
- **Fonte C — Recursos vinculados:** caução do TCRA nº 05/2023 com saldo de R$ 9,0 MM, recuperável contra comprovação de obras de infraestrutura e segurança assistencial, com glosas administrativas médias de 18% e prazo decadencial de 24 meses por campanha (DOC-12). A campanha concluída em 05/02/2025 (R$ 4,50 MM comprovados) ainda não teve a reivindicação protocolada.
- **Fonte D — Capacidade física:** 4.380 sala-dias/ano no bloco cirúrgico; rotina consome 3.912; manutenções programadas 84; ocioso agregado de 384 sala-dias, pulverizado (DOC-22).

**Situação financeira.** EBITDA 12M (30/06/2026): R$ 84,9 MM; dívida líquida: R$ 252,6 MM; DívLíq/EBITDA = 2,98x. Covenant da 5ª emissão de debêntures: ≤ 3,25x, teste trimestral (DOC-27).

---

## SEÇÃO 2 — FRENTES PROPOSTAS PELA DIRETORIA (reunião de 16/09/2026)

### DOC-02 — Pauta da Diretoria: pacote PEEA 2027

Palavra da Diretoria Executiva: "O pacote abaixo cabe nos tetos aprovados e reposiciona a rede na alta complexidade: bloco cirúrgico novo, diagnósticos blindados e inteligência artificial."

| # | Frente | Custo declarado | Fonte pedida | Justificativa da Diretoria |
|---|---|---|---|---|
| F1 | Expansão Ala Cirúrgica Norte: +6 salas, CME nova, +120 leitos | R$ 24,6 MM capex (fase A 16,4: engenharia 4,8, fundações/estrutura 7,1, subestação+SPDA 4,5; fase B 8,2: interligação de gases 3,1, exaustão/climatização/chillers 5,1) | CAPEX | Habilita o contrato Omega Excelência (F9). Contrapartida Omega de R$ 8,5 MM (4,25 na fase A, 4,25 na fase B), "mediante contrato definitivo". Fase A jan–jun/2027; fase B mar–ago/2027, com interdição de 5 das 12 salas de 01/04 a 28/08/2027 (140 dias) para a interligação — "única janela sem férias coletivas". "A ocupação eletiva é de 89%; as 7 salas remanescentes absorvem a demanda" (premissa P4). Após a interligação, "shutdown da climatização para troca dos chillers em set–dez/2027". "Sem impacto regulatório identificado." |
| F2 | Modernização do bloco existente: salas 1–6 (mesas, luzes, torres) + parada geral | R$ 7,4 MM capex (equipamentos 5,9 + requalificação de gases 0,95 embutida + facilities da parada 0,55) | CAPEX | "Salas com 14 anos. Requalificação da central de gases incluída na parada geral de jul/2027, com economia de mobilização." |
| F3 | Renovação do contrato de manutenção de diagnósticos (Geomed) | R$ 6,80 MM/ano × 5 anos | Custeio | "Assinatura até 30/11/2026, sob pena de perder a tabela e os slots de manutenção 2027." |
| F4 | Preditiva de equipamentos assistenciais (EquipTech) | R$ 3,1 MM capex + R$ 1,1 MM/ano | CAPEX | "Redução de 18% das paradas corretivas; R$ 4,6 MM/ano de economia já em 2027." |
| F5 | IA de agendamento e recuperação de glosas (MedFlow) | R$ 1,9 MM capex + licença anual | CAPEX + custeio | "Payback típico de 2,8 anos comprovado em clientes. Licença take-or-pay de 5 anos; não há alternativa certificada no mercado." |
| F6 | Recertificação ONA nível 3 + programa de segurança do paciente | R$ 1,45 MM/ano | Custeio | Diferencial de contratação e acreditação. |
| F7 | Reposição do parque de bombas de infusão | R$ 5,3 MM capex (380 unidades) | CAPEX | "32% da frota acima da vida útil." |
| F8 | Recomposição de caixa e reservas operacionais | R$ 2,20 MM/ano | Custeio | Prudência financeira. |
| F9 | Contrato Omega Excelência | Receita | — | Margem incremental de R$ 9,6 MM/ano. Quadro da Diretoria assume EBITDA incremental a partir do T3/2027. |

**Medida de emergência (pedido da Diretoria Médica, recomendado e rejeitado pela Diretoria Financeira):** operação de reforço da radioterapia — regime dedicado do fabricante do LINAC (Radlin: 2 engenheiros clínicos + técnico residente, kit de peças críticas em consignação, 2 turnos + sábados) de 01/10 a 31/12/2026, prorrogável por até um trimestre, custo R$ 3,2 MM (2026) + R$ 1,2 MM (T1/2027), recuperando ~1.220 sessões no Q4/2026. Rejeição registrada: "sem fonte orçamentária em 2026 e sem ROI no trimestre" (DOC-24).

---

## SEÇÃO 3 — QUADRO CONSOLIDADO DA DIRETORIA

### DOC-03 — Quadro consolidado e premissas declaradas

Capex (participação HCS, já líquida da contrapartida Omega): F1 16,1 (24,6 − 8,5) + F2 7,4 + F4 3,1 + F5 1,9 + F7 5,3 = **R$ 33,8 MM**. Afirmativo da Diretoria: "o pacote de R$ 33,8 MM cabe no teto de capex de R$ 42,0 MM aprovado pelo Conselho".

Custeio incremental 2027 — Quadro 5 da Diretoria (teto R$ 16,0 MM):

| Linha | R$ MM |
|---|---:|
| F5 — licença MedFlow ano 1 | 2,05 |
| F4 — opex EquipTech | 1,10 |
| F6 — recertificação ONA | 0,85 |
| F6 — programa de segurança do paciente (obrigatório) | 0,60 |
| F8 — recomposição de caixa e reservas | 2,20 |
| Contratos de manutenção novos (incl. delta Geomed 1,05) | 2,60 |
| TI e segurança da informação | 1,60 |
| Treinamento e certificações | 1,25 |
| Reajustes contratuais (índices) | 1,15 |
| Requalificação da central de gases (jul/2027) | 0,95 |
| Inspeção NR-13 dos vasos da CME | 0,35 |
| Vigilância e segurança patrimonial | 0,88 |
| Estudos e auditorias de suporte | 0,40 |
| **Total impresso** | **15,98** |

Afirmativo da Diretoria: "o quadro fecha com folga de R$ 0,02 MM no teto de custeio". (A proposta da MedFlow Sistemas é de licença de R$ 2,45 MM/ano — DOC-18.)

**Projeção financeira do pacote (anexo ao Quadro 5).** A Diretoria projeta EBITDA 2027 de R$ 94,5 MM — "R$ 84,2 MM de base + R$ 9,6 MM do Omega Excelência (T3/2027) + R$ 4,5 MM de ganhos digitais (MedFlow + EquipTech) − R$ 3,8 MM de impacto da interdição, mitigado pelas 7 salas remanescentes" — e dívida líquida de R$ 268,4 MM ao fim de 2027 com o capex integral do pacote: "razão projetada de 2,84x — confortavelmente dentro do covenant".

**Premissas declaradas pela Diretoria (P1–P8):**
- **P1.** "A requalificação da central de gases até 28/11/2026 foi homologada judicialmente e não admite revisão."
- **P2.** "O covenant de 3,25x é duro, testado trimestralmente; qualquer plano precisa respeitá-lo."
- **P3.** "A CME atual opera a 97% da capacidade física; qualquer acréscimo de volume cirúrgico exige a CME nova."
- **P4.** "O bloco cirúrgico absorve a interdição de 5 salas entre abril e agosto sem impacto material, pois a ocupação eletiva é de 89%."
- **P5.** "O take-or-pay de gases medicinais é fixo em R$ 2,45 MM/mês até 2028, sem flexibilidade sazonal."
- **P6.** "Não há folga financeira fora dos tetos aprovados; qualquer custo adicional exige cortar outra frente."
- **P7.** "A renovação Geomed precisa ser assinada até 30/11/2026; depois disso perde-se a tabela e os slots de 2027."
- **P8.** "MedFlow e EquipTech agregam R$ 9,1 MM de EBITDA já em 2027."

---

## ANEXOS OPERACIONAIS E FINANCEIROS

### DOC-04 — Ata CA-1.096/2026 (Conselho, 26/05/2026, item 2) — extrato
"…aprovada a proposta da Diretoria Financeira de cancelar o projeto MAT-07 — Ampliação da Maternidade, no valor de R$ 7,2 MM, determinando a liberação do saldo para reapreciação no ciclo 2027, com baixa contábil a efetivar pela Contabilidade no fechamento do exercício."

### DOC-05 — Ata CA-1.102/2026 (Conselho, 31/07/2026, item 5) — extrato
"…aprovado o Orçamento 2027 com teto de custeio incremental de R$ 16,0 MM, nos termos da Política Financeira PO-12."

### DOC-06 — Ata CA-1.105/2026 (Conselho, 14/08/2026, itens 4 e 7) — extrato
Item 4: "…aprovado o teto de CAPEX 2027 de R$ 42,0 MM, englobando as obras em andamento (comprometido de R$ 36,5 MM em 10/08/2026) e novas aprovações." Item 7: "…convocada a apreciação do pacote consolidado da Diretoria Executiva na reunião de 30/09/2026, com parecer técnico prévio."

### DOC-07 — Política Financeira PO-12 (v. 4) — artigos citados
- **Art. 4º, §2º.** "As despesas compulsórias de natureza regulatória, de segurança assistencial ou impostas por autoridade pública são contabilizadas na rubrica 3.9.1 — Despesas Compulsórias Regulatórias e de Segurança Assistencial, que não consome o teto de custeio incremental."
- **Art. 8º.** "Recursos vinculados, cauções e depósitos não são fungíveis entre si nem com recursos livres; sua aplicação observa exclusivamente a destinação do instrumento de origem."
- **Art. 9º.** "A Presidência pode contratar emergencialmente até R$ 3,5 MM por evento, com ratificação obrigatória do Conselho na reunião seguinte."
- **Art. 10.** "O Conselho pode suplementar teto de capex ou custeio em até 10% por exercício, por decisão fundamentada."

### DOC-08 — Contrato de Manutenção de Diagnósticos n. 214/2022 (HCS × Geomed Services)
Objeto: manutenção integrada (peças OEM e mão de obra) das 2 ressonâncias, tomógrafo e angiô. Valor: R$ 5,75 MM/ano. Vigência: até 28/02/2027.

**Cláusula 8.2 (prorrogação).** "O presente contrato poderá ser prorrogado por 12 (doze) meses, mediante aviso escrito com antecedência mínima de 60 (sessenta) dias do termo final, mantidas as demais condições, inclusive o valor anual de R$ 5,75 MM." → Para vigência até 28/02/2027, o aviso deve ser expedido até 30/12/2026.

### DOC-09 — Contrato Omega n. 55/2024 (vigente)
Vigência até 31/12/2028; representa 38% da receita da HCS.
- **Cláusula 7.2:** mínimo de 10 salas cirúrgicas operacionais em horário útil; descumprimento → −12% sobre o faturamento cirúrgico Omega do período (faturamento cirúrgico Omega ≈ R$ 5,7 MM/mês → penalidade ≈ R$ 3,4 MM por 5 meses de descumprimento).
- **Cláusula 9.1:** glosas de 2025 somaram R$ 5,3 MM.

### DOC-10 — Contrato de Fornecimento de Gases Medicinais n. 77/2023 (HCS × White Gases)
- **Cláusula 5.2 (take-or-pay):** faturamento mínimo mensal de R$ 2,45 MM; sobre o faltante incide multa de 115%.
- **Cláusula 6.7 (reequilíbrio sazonal):** "As partes poderão acordar banda mensal de R$ 1,80 a R$ 2,45 MM para o exercício seguinte, mediante pedido protocolado até 60 dias antes do início do exercício de referência." → Para 2027, o pedido deve ser protocolado até 01/12/2026.
- **Estudo interno:** a interdição de 5 salas por 5 meses derruba o consumo de gases em ~30% (para ~R$ 1,72 MM/mês).

### DOC-16 — Extrato do módulo de investimentos (ERP, relatório de 10/09/2026)
| Projeto | Status | Comprometido |
|---|---|---:|
| MAN-31 Reforma da UTI | Em execução | 9,8 |
| MAN-34 Ampliação do Pronto-Socorro | Em execução | 8,2 |
| Outros em andamento (11 projetos) | Em execução | 18,5 |
| MAT-07 Ampliação da Maternidade | Em execução | 7,2 |
| **Saldo disponível reportado** | — | **5,5** |

### DOC-26 — Extrato de reservas e rubricas (Controladoria, 30/06/2026)
| Instrumento | Dotação | Consumido | Saldo |
|---|---:|---:|---:|
| Caução TCRA nº 05/2023 | 9,0 | 0,0 | 9,0 |
| Provisão de contingências 2026 | 4,6 | 1,2 | 3,4 |
| Rubrica 3.9.1 (compulsórias) 2026 | 5,2 | 3,3 | 1,9 |

### DOC-27 — Escritura da 5ª emissão de debêntures (resumo financeiro)
- **Covenant:** DívLíq/EBITDA ≤ 3,25x, apurado e testado trimestralmente; descumprimento constitui evento de inadimplemento com vencimento antecipado da dívida (R$ 252,6 MM).
- Não há mecanismo automático de waiver; dispensa exige assembleia de debenturistas (prazo inviável dentro do ciclo de planejamento 2027).
- **Base 30/06/2026:** EBITDA 12M = 84,9; DívLíq = 252,6 → **2,98x**.

---

## ANEXOS REGULATÓRIOS E TÉCNICOS

### DOC-11 — Ação Civil Pública 0042.2025 + decisão judicial
ACP 0042.2025 (homologada em 11/03/2025): a HCS deve requalificar a central de gases medicinais e a rede de distribuição até 28/11/2026, sob multa de R$ 180.000/dia a partir de 29/11/2026.

Sentença terminativa (trânsito em julgado em 30/07/2026): rejeita o pedido de revisão do prazo formulado pela HCS. "A obrigação de requalificar a central de gases até 28/11/2026 é inerível à instituição, não admitindo revisão, dilatação ou compensação."

### DOC-12 — Termo de Compromisso de Ajustamento — TCRA nº 05/2023 (caução)
- Caução constituída em 2023: R$ 9,0 MM (saldo atual, DOC-26).
- **Cláusula 7.1:** retorno contra comprovação (ART/laudo) de obras de infraestrutura e segurança assistencial.
- **Cláusula 7.3:** glosas administrativas históricas médias de 18% sobre o valor reivindicado (recuperação efetiva ≈ 82%).
- **Cláusula 9 (decadência):** "O direito à reivindicação de retorno prescreve/decade em 24 meses da conclusão de cada campanha qualificada."
- **Cláusula 11 (destinação):** "Os valores retornados aplicam-se exclusivamente a obras e serviços de infraestrutura e segurança assistencial do HCC, inclusive reforma elétrica, SPDA e requalificação de gases."
- **Campanha pendente:** concluída em 05/02/2025 (rede elétrica essencial + SPDA), R$ 4,50 MM comprovados → reivindicação de R$ 4,50 MM (recuperação esperada ≈ R$ 3,7 MM). Nenhuma reivindicação protocolada até 10/09/2026.

### DOC-13 — RDC 07/2025 (regulamento sanitário federal, fictício)
Art. 14. "Hospitais gerais com mais de 350 leitos operacionais devem dispor de central de material e esterilização (CME) com barreira física e automação plena ['CME plena'], exigível a partir da renovação da licença sanitária seguinte ao enquadramento." Leitos atuais do HCC: 280. Com a expansão da Ala Cirúrgica Norte (+120 leitos): 400. Orçamento de referência da CME plena: R$ 4,2 MM capex + R$ 0,7 MM/ano; licença ampliada prevista para meados de 2029 se a obra concluir em 2028.

### DOC-14 — Norma Técnica NT-GM 07/2021 (gases medicinais)
- Requalificação completa da central e da rede a cada 60 meses, executada por empresa certificada, com esvaziamento setorial das alas e interdição parcial de 10–12 dias por bloco (teste de estanqueidade, alarmes e redundância).
- Última execução: 28/11/2021 → ciclo vence em 28/11/2026.
- A única empresa certificada na região (QualiGás Engenharia) confirmou disponibilidade apenas para 05–23/10/2026 ou abril/2027.
- A requalificação desmobiliza parcialmente a CME (rede de gases e vácuo do setor). A inspeção NR-13 dos vasos sob pressão da CME (caldeiras e autoclaves) vence em 20/01/2027 e exige parada de 6–8 dias; executada dentro da mesma janela de out/2026, evita uma segunda interdição isolada — estimativa interna de custo dessa segunda parada: R$ 0,5 MM (esterilização terceirizada + cancelamentos).

### DOC-15 — Apólice de responsabilidade civil hospitalar (cláusulas citadas)
- **Cláusula 10.4:** "a manutenção das requalificações obrigatórias em dia é condição de vigência da cobertura; requalificação vencida suspende a cobertura de eventos assistenciais correlatos a partir da data-limite."
- **Cláusula 8.1:** inspeções legais (NR-13) válidas como condição de cobertura.
- **Cláusula 9.3:** mesas cirúrgicas com laudo de conformidade vigente.

### DOC-17 — Proposta Geomed Services (08/09/2026, "urgente")
- Renovação por 5 anos: R$ 6,80 MM/ano, "proposta válida até 30/11/2026; após, nova tabela (+8%) e slots de manutenção 2027 sujeitos a disponibilidade".
- A campanha de upgrades das ressonâncias está programada pela Geomed para o 2º trimestre de 2027 (pós-assinatura).
- Internamente, o rito de contratação competitiva (edital → adjudicação) só conclui em abril/2027.

### DOC-18 — Proposta MedFlow Sistemas Ltda. (05/09/2026)
- Implantação: R$ 1,9 MM; licença take-or-pay: R$ 2,45 MM/ano por 5 anos; multa rescisória de 40% das parcelas restantes após o 12º mês.
- **Business case:** "hospitais com mais de 600 leitos e ocupação de 78% obtiveram R$ 14,5 MM/ano em recuperação de glosas e ociosidade de salas; payback típico de 2,8 anos."
- **Perfil HCS:** 280 leitos; glosas totais 2025: R$ 5,3 MM (DOC-09); ociosidade de salas estimada pela própria HCS: R$ 3,1 MM/ano.

### DOC-19 — Proposta EquipTech Telemetria (03/09/2026)
- Retrofit de sensores em autoclaves, chillers, geradores e mesas cirúrgicas: R$ 3,1 MM (execução mar–ago/2027) + R$ 1,1 MM/ano.
- **Comercial:** "redução de 18% das paradas corretivas, R$ 4,6 MM/ano de economia já no primeiro exercício (2027)."
- **Anexo técnico do próprio fabricante:** "o modelo preditivo v1 requer a operação do CMMS (sistema de gestão de manutenção) por 6 meses, a implantação de telemetria e 14 meses de dados acumulados após a conclusão do retrofit; alertas básicos por sensor disponíveis desde a semana 4." A HCS não possui CMMS (implantação: R$ 0,8 MM, 6 meses).

### DOC-20 — Laudo de avaliação do bloco cirúrgico (EngClínica, ago/2026)
- "Mesas cirúrgicas das salas 3 e 5 com falhas de travamento hidráulico (condição nível 4); risco assistencial; substituição recomendada de forma imediata."
- "A modernização das salas 1–6 é desejável, mas as demais integridades estão preservadas."
- "A requalificação da rede de gases é indispensável e deve anteceder qualquer reforma profunda do bloco."

### DOC-21 — Laudo de capacidade da CME (EngClínica, ago/2026)
- Capacidade física de processamento: 2.450 instrumentais/dia; demanda corrente: 2.380 (97% de utilização).
- "Acima de 2% de acréscimo de volume cirúrgico, a fila compromete o turnaround de instrumentais; não há alavanca de processo que substitua capacidade física."

### DOC-22 — Cronograma físico do bloco cirúrgico 2027 + parecer de método (E-77)
- Capacidade: 12 salas × 365 = 4.380 sala-dias. Rotina (cirurgias): 3.912 (89,3%). Manutenções programadas: 84. Ocioso agregado: 384 sala-dias, pulverizado; o único bloco de ociosidade conjunta é janeiro (≈62 sala-dias — férias coletivas); demais janelas ≤ 15 dias.
- **Nota de engenharia E-77 (parecer de método construtivo):** "a interdição de 5 salas por 140 dias é exigência do método convencional de interligação de gases/exaustão. Existe método alternativo — 3 etapas noturnas com contenção estanque e pressão negativa móvel — que mantém 10 salas operacionais, com acréscimo de R$ 1,6 MM e +2 meses de prazo."
- **Nota E-78 (climatização):** "a troca dos chillers exige desligamento do HVAC do bloco; pela RT-07/2023, centros cirúrgicos exigem pressão positiva contínua — interrupção do HVAC implica interdição total do bloco, salvo locação de chiller provisório (+R$ 0,9 MM). Lead time dos chillers novos: 10 meses de fabricação + 10 semanas de instalação/comissionamento. A janela de menor risco eletivo para o cutover é janeiro (férias coletivas)."

### DOC-23 — Relatório do parque de bombas de infusão (ago/2026)
- 480 bombas; 154 (32%) acima da vida útil; 287 quebras registradas em 2025 (alta de 41% sobre 2024).
- Reposição integral (380 unidades novas): R$ 5,3 MM. Alternativa de mercado: compra de 180 unidades (R$ 2,5 MM) + locação de 200 unidades (R$ 0,45 MM/ano).

### DOC-24 — Escopo da operação de reforço da radioterapia + restrições
- Regime dedicado Radlin de 01/10 a 31/12/2026: recupera ~1.220 sessões → 2026 fecha em 10.130 sessões (92,1% do mínimo); sem o reforço, 8.910 (81,0%) — segundo exercício consecutivo abaixo de 90% → desabilitação (RT-MS 11/2024).
- Custo: R$ 3,2 MM (2026) + R$ 1,2 MM (T1/2027, opção de prorrogação por 1 trimestre). Rejeitado pela Diretoria Financeira: "sem fonte orçamentária em 2026 e sem ROI no trimestre" (DOC-02).
- O contrato dedicado Radlin inclui o laudo anual de radioproteção (vence 31/03/2027); desmobilizar em 31/12/2026 exigiria remobilização de R$ 0,6 MM apenas para o laudo.
- A substituição do LINAC (Radlin, R$ 18,5 MM) é solução definitiva com entrega em 2028 — decisão de capex até 30/06/2027. Enquanto isso, a margem pós-reforço de 2026 é estreita: apenas +230 sessões acima de 90%.

### DOC-25 — LOI Omega Excelência (assinada 28/08/2026)
- Margem incremental estimada: R$ 9,6 MM/ano.
- **Condições para o contrato definitivo (assinatura até 15/12/2026):** (i) manutenção da habilitação de radioterapia; (ii) engenharia da expansão aprovada e compromisso de 16 salas e CME nova prontas até 31/12/2028; (iii) startup da operação em 01/03/2029.
- **Contrapartida:** "aporte total de R$ 8,5 MM — 50% das despesas elegíveis da fase A até R$ 4,25 MM e 50% da fase B até R$ 4,25 MM — pagos trimestralmente contra comprovação de desembolso, condicionados ao contrato definitivo."
