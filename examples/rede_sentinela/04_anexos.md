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
