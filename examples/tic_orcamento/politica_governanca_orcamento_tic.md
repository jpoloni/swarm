# Política de Governança de Orçamento de TIC
## Documento POL-TIC-ORC-2025-02 | Versão 2.1 | Vigência: 01/03/2025
## Substitui: POL-TIC-ORC-2024-06 (v1.8)

**Emitente:** Diretoria de Tecnologia da Informação (DTI), com anuência de Controladoria e Finanças  
**Abrangência:** todo Capex e Opex de TIC da PetroHorizonte S.A., inclusive unidades offshore e joint ventures sob controle operacional  
**Classificação:** Uso interno — confidencialidade financeira

---

## 1. Objetivo

Estabelecer requisitos obrigatórios para planejamento, execução, forecast e controle de desvios de gasto de TIC (cloud, infraestrutura, telecom, software e serviços), de modo que overrun, change freeze e drawdown de contingência sejam detectáveis e auditáveis.

## 2. Definições operacionais

- **Capex de TIC:** investimento capitalizável em ativos de TIC (ex.: links dedicados, appliances, licenças perpétuas aprovadas como investimento).
- **Opex de TIC:** despesa operacional recorrente ou pontual de TIC (ex.: cloud pay-as-you-go, suporte, SaaS).
- **Linha orçamentária:** código WBS/CC aprovado no orçamento anual de TIC (OAT).
- **Forecast:** projeção atualizada do gasto até o fim do exercício ou do trimestre, conforme calendário desta política.
- **Change freeze orçamentário:** período em que novos compromissos Opex acima do limite desta política exigem exceção formal.
- **CGTIC:** Comitê de Governança de TIC (aprovação de Capex e rebaselines).
- **FinOps TIC:** célula responsável por medição de cloud e arquivamento de evidências de spend.

## 3. Requisitos MUST (obrigatórios e testáveis)

Os requisitos a seguir são **MUST**. Descumprimento configura não conformidade de governança de spend de TIC.

### MUST-01 — Aprovação CGTIC antes de Capex TIC acima do limiar

Qualquer compromisso Capex de TIC com valor igual ou superior a **R$ 500.000,00** **MUST** possuir ata de aprovação do CGTIC (número e data) **antes** da emissão de pedido de compra (PO) ou assinatura de contrato, arquivada em `orcamento-tic/atas-cgtic/`.

### MUST-02 — Forecast mensal até o 5º dia útil

Até o **5º (quinto) dia útil** de cada mês, o gestor da linha orçamentária **MUST** publicar forecast atualizado no repositório `orcamento-tic/forecast/`, com: valor projetado do mês; acumulado YTD; e, se a variação frente ao orçamento aprovado for **maior que 5%**, justificativa escrita da causa.

### MUST-03 — Change freeze no fechamento do trimestre

Nos **últimos 10 (dez) dias corridos** de cada trimestre civil, é **MUST** não assumir novo compromisso Opex de TIC **acima de R$ 50.000,00** sem **exceção formal do CFO** (e-mail ou despacho numerado) arquivada no dossiê da linha.

### MUST-04 — Rebaseline antes de continuar overrun acima de 10%

Quando o gasto realizado + comprometido de uma linha superar **10%** do orçamento aprovado daquela linha, a área **MUST** obter rebaseline aprovado pelo CGTIC **antes** de autorizar novo desembolso ou novo compromisso na mesma linha. Continuar gastando sem rebaseline **MUST** ser registrado como não conformidade.

### MUST-05 — Relatório semanal FinOps de cloud arquivado

Para contas cloud sob gestão da DTI, a célula FinOps TIC **MUST** arquivar, **toda semana**, relatório de spend (CSV ou PDF) em `orcamento-tic/finops/semanal/`, contendo: conta/subscription; valor da semana; acumulado do mês; e top-5 serviços por custo.

### MUST-06 — Regularização de spend emergencial em 15 dias

Gasto emergencial de TIC autorizado fora do fluxo regular (incidente operacional, segurança ou continuidade) **MUST** ser regularizado com aprovação retrospectiva do CGTIC ou do CFO (conforme alçada Capex/Opex) **em até 15 (quinze) dias corridos** da data do primeiro desembolso, com evidência no dossiê.

### MUST-07 — Drawdown de contingência TIC documentado

Uso da reserva de contingência de TIC **MUST** ser autorizado por despacho do Diretor de TIC, com: valor; linha beneficiada; motivo; e saldo remanescente da contingência, arquivado em `orcamento-tic/contingencia/` **antes** do drawdown contabilizado.

Quando houver overrun de uma linha de TIC, o Diretor de TIC **MUST** formalizar em despacho a decisão de usar ou não a reserva de contingência, mesmo que não ocorra drawdown. A ausência de drawdown não dispensa a decisão formal sobre a contingência.

---

## 4. Papéis

| Papel | Responsabilidade principal |
|---|---|
| Gestor da linha orçamentária | Forecast, pedido de rebaseline, respeito ao change freeze |
| FinOps TIC | Relatórios semanais de cloud, alertas de overrun |
| CGTIC | Aprovação Capex ≥ limiar, rebaselines, atas |
| CFO | Exceções de change freeze Opex |
| Controladoria | Conciliação OAT × realizado |

## 5. Vigência e revisão

Versão **2.1** entra em vigor na data do cabeçalho. Alteração de limiar, prazo ou alçada de MUST exige bump de versão maior.

**Aprovação:** Comitê Executivo de TIC — ata CEX-TIC-2025-03.
