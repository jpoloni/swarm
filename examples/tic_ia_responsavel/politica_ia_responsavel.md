# Política de Inteligência Artificial Responsável — Modelos em Produção Operacional
## Documento POL-TIC-IA-2025-04 | Versão 1.2 | Vigência: 15/03/2025

**Emitente:** Diretoria de TIC e Digital, com anuência de Engenharia de Confiabilidade, Segurança Operacional e Comitê de Dados  
**Abrangência:** modelos de aprendizado de máquina e sistemas de recomendação automatizada em uso produtivo na PetroHorizonte S.A., inclusive preditiva de manutenção, vigilância de poços e triagem de contratados quando classificados como **alto impacto**  
**Classificação:** Uso interno — confidencialidade operacional  
**Escopo deste corpus de calibração:** modelo preditivo de manutenção de trens de compressão (série PH-PREDCOMP)

---

## 1. Objetivo

Estabelecer requisitos obrigatórios, testáveis e auditáveis para governança de modelos de IA em produção operacional, de modo a reduzir risco de decisão automatizada inadequada, drift não tratado, ausência de rastreabilidade e uso de componentes de fornecedor sem diligência vigente.

Esta política **não** substitui normas de SMS (segurança, meio ambiente e saúde) nem procedimentos de intervenção em ativos; ela condiciona a promoção e a operação de modelos que influenciem recomendações técnicas.

## 2. Definições operacionais

Para os efeitos desta política:

- **Modelo em produção:** artefato versionado que gera escore, classificação ou recomendação consumida por painel operacional, workflow ou API de decisão em ambiente produtivo.
- **Alto impacto:** recomendação cuja execução possa implicar parada de trem de compressão, mobilização emergencial de equipe, intervenção não programada em ativo crítico, ou alteração material de plano de manutenção com custo estimado superior ao limiar interno LIM-IA-OPS-01.
- **Owner do modelo:** colaborador nomeado, com matrícula, responsável pela conformidade contínua do modelo (inventário, evidências, resposta a drift e incidentes).
- **HITL (human-in-the-loop):** aprovação humana registrada **antes** da execução de ação decorrente de recomendação de alto impacto.
- **Drift:** desvio estatístico ou operacional das features de entrada ou da performance do modelo em relação à baseline da model card vigente, detectado por monitor aprovado pelo Comitê de Dados.
- **Model card:** ficha técnica versionada do modelo (objetivo, dados, métricas, limitações, owner, data de promoção).
- **Linhagem de features:** registro rastreável das fontes, transformações e janelas temporais das variáveis usadas no último treino ou retreino promovido.

## 3. Requisitos MUST (obrigatórios e testáveis)

Os requisitos a seguir são **MUST**. O não cumprimento configura não conformidade de governança de IA e deve ser registrado no Registro de Incidentes Operacionais (RIO) ou no registro de não conformidade TIC, com justificativa formal e evidência anexada.

### MUST-01 — Inventário de modelos e owner nomeado

Antes de qualquer promoção a produção, e a cada alteração de versão maior, a área de TIC/Digital **MUST** registrar o modelo no inventário corporativo `inv-modelos-ia` com, no mínimo: identificador versionado; finalidade operacional; classificação de impacto; owner (nome e matrícula); data de promoção; e link para a model card vigente.

Alteração de owner **MUST** ser refletida no inventário **em até 5 (cinco) dias úteis**. Modelo em produção sem owner nomeado **MUST** ser marcado como não conforme e ter recomendação automatizada desabilitada até regularização.

### MUST-02 — Human-in-the-loop para decisões de alto impacto

Toda recomendação classificada como **alto impacto** (conforme definição desta política e matriz LIM-IA-OPS-01) **MUST** obter aprovação HITL registrada — identificador do aprovador, matrícula, carimbo de data/hora e decisão (aprovar / rejeitar / escalar) — **antes** da execução da ação operacional correspondente.

A ausência de registro HITL **MUST** ser tratada como não conformidade. Sistemas que permitam “execução automática” de recomendações de alto impacto **MUST** permanecer desabilitados, salvo exceção escrita do Comitê de Dados com prazo máximo de 90 dias e plano de compensação.

### MUST-03 — Avaliação de segurança e desempenho antes da produção

Nenhuma versão de modelo **MUST** ser promovida a produção sem gate de avaliação pré-produção concluído e arquivado, contendo no mínimo: métricas de desempenho na baseline aprovada; verificação de falhas de segurança operacional relevantes ao caso de uso (falsos positivos/negativos em classes críticas); e parecer de liberação assinado pelo owner e por representante de Engenharia de Confiabilidade.

O gate **MUST** ter data anterior ou igual à data de promoção registrada no inventário. Promoção sem gate arquivado **MUST** ser revertida **em até 24 (vinte e quatro) horas** após identificação.

### MUST-04 — Resposta a drift e rollback

Quando o monitor de drift emitir alerta de severidade **Alta** ou **Crítica** para modelo em produção, o owner (ou plantão TIC designado) **MUST** confirmar o evento no RIO **em até 2 (duas) horas** e **MUST** executar uma das ações a seguir **em até 6 (seis) horas** contadas da confirmação: (a) rollback para a última versão estável com model card vigente; ou (b) desabilitar a emissão de recomendações automatizadas do modelo afetado.

A ação escolhida, o identificador da versão resultante e o horário de conclusão **MUST** constar do RIO. Extensão do prazo **MUST** ser autorizada por escrito por Segurança Operacional e registrada no mesmo RIO.

### MUST-05 — Linhagem de dados das features de treino

Para cada versão promovida, o owner **MUST** anexar à model card (ou ao dossiê de promoção) a linhagem das features de treino, incluindo: origem dos datasets; janela temporal; transformações principais; e responsável pela extração.

Retreino ou hot-fix que altere features **MUST** atualizar a linhagem **antes** da promoção. Em incidente envolvendo o modelo, a linhagem da versão em produção **MUST** estar recuperável **em até 1 (um) dia útil** a partir da confirmação no RIO.

### MUST-06 — Logging de recomendações automatizadas

Todo modelo em produção **MUST** registrar, em log imutável ou com trilha de auditoria, cada recomendação automatizada emitida, com no mínimo: timestamp; identificador e versão do modelo; ativo ou tag operacional alvo (código interno fictício permitido); classe/escore; e se a recomendação foi ou não consumida por workflow.

Logs de recomendações de alto impacto **MUST** ser retidos por **no mínimo 2 (dois) anos**. Falha de logging por mais de 4 (quatro) horas contínuas em produção **MUST** desabilitar novas recomendações até restauração.

### MUST-07 — Due diligence de componente ou modelo de fornecedor

Se o modelo em produção depender de componente, API ou modelo fornecido por terceiro (vendor), a área de TIC/Digital **MUST** manter diligência vigente: avaliação de segurança/qualidade arquivada com data de validade **não superior a 12 (doze) meses**, e revisão obrigatória **antes** do go-live de nova versão major do componente.

Diligência vencida **MUST** ser registrada como não conformidade; o owner **MUST** apresentar plano de regularização **em até 10 (dez) dias úteis** ou desabilitar o uso do componente em produção.

---

## 4. Papéis

| Papel | Responsabilidade principal |
|---|---|
| Owner do modelo | Inventário, model card, gate pré-prod, linhagem, resposta a drift, evidências no RIO |
| Engenharia de Confiabilidade | Parecer de liberação; validação de impacto operacional das recomendações |
| Segurança Operacional | Autorização de extensão de prazo de rollback; interface com procedimentos SMS |
| Plantão TIC / MLOps | Monitoramento de drift, logging, execução técnica de rollback |
| Comitê de Dados | Exceções HITL, classificação de impacto, revisão anual desta política |
| Fornecedor (quando aplicável) | Evidências para due diligence; suporte a incidente que envolva seu componente |

## 5. Relação com outros normativos

Incidentes de modelo que também envolvam dados pessoais permanecem sujeitos às políticas de privacidade vigentes. Esta política trata **governança de IA operacional**, não substituindo LGPD, contratos de fornecedor genéricos nem orçamentos de infraestrutura.

## 6. Vigência e revisão

Versão **1.2** entra em vigor na data do cabeçalho. Alteração de prazo, limiar de alto impacto ou escopo de MUST exige bump de versão menor ou maior conforme materialidade, com comunicação às áreas owners.

**Aprovação:** Comitê de Dados — ata CD-IA-2025-02; ratificação Diretoria TIC/Digital.
