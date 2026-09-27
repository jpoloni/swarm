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

