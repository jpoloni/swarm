# Spec: swarm one-shot para objetivos específicos

**Versão:** 0.1
**Estado:** proposta implementável
**Base:** OpenAI Agents SDK para Python

## 1. Objetivo

Executar um objetivo definido pelo solicitante em uma única chamada lógica. Um agente principal divide o trabalho, orquestradores auxiliares coordenam frentes independentes quando configurados, workers executam tarefas específicas e o principal entrega uma resposta consolidada. A quantidade e o modelo de cada agente são parâmetros da execução.

**One-shot** significa: uma entrada, uma execução com limites explícitos e uma saída final. A execução pode conter várias chamadas de modelo, mas não depende de uma conversa posterior, memória entre execuções ou intervenção interativa para terminar.

## 2. Escolha de arquitetura

O fluxo usa o **OpenAI Agents SDK** com `Agent(model=...)` para cada participante e `Runner.run(...)` para cada etapa. A aplicação controla o grafo de execução, a fila de tarefas, os limites e a consolidação; o SDK executa os agentes, suas ferramentas e o tracing. A documentação oficial confirma modelos por agente e orquestração por código. [Modelos por agente](https://developers.openai.com/api/docs/guides/agents/models), [orquestração](https://developers.openai.com/api/docs/guides/agents/orchestration).

A [Agents API](https://developers.openai.com/api/docs/guides/agents/sdk) é a recomendação atual da OpenAI para novos agentes e já permite subagentes paralelos com `max_concurrent_subagents`. Sua documentação de [multi-agent](https://developers.openai.com/api/docs/guides/agents-api/multi-agent) mostra o modelo do agente principal e o limite de subagentes, mas não documenta nessa superfície a escolha explícita do modelo de cada subagente. A exigência de modelos individuais determina o uso do SDK nesta versão da spec. Reavaliar essa escolha se a Agents API passar a documentar essa configuração.

## 3. Papéis e topologia

```text
Entrada única
    │
    ▼
Orquestrador principal ── plano e distribuição
    ├── Worker 1 ── tarefa específica
    ├── Worker 2 ── tarefa específica
    └── Orquestrador auxiliar ── coordena uma frente
         ├── Worker 3 ── tarefa específica
         └── Worker N ── tarefa específica
    │
    ▼
Orquestrador principal ── validação e síntese ── saída única
```

- **Principal:** exatamente um por execução. Define tarefas e critérios de aceite, atribui cada tarefa a um worker e cada frente a um orquestrador, acompanha resultados e produz a resposta final.
- **Orquestradores auxiliares:** `orchestrators.count - 1`. Cada um orienta sua frente antes da execução, revisa resultados depois e devolve ao principal um resumo estruturado. Não cria workers além do total configurado.
- **Workers:** executam tarefas delimitadas. Cada worker recebe objetivo local, contexto mínimo, ferramentas permitidas, formato de saída e critério de conclusão. Não responde diretamente ao solicitante.
- **Aplicação hospedeira:** instancia agentes, agenda chamadas paralelas, aplica timeout, mantém IDs, registra estados e impõe orçamento. O principal decide o plano; a aplicação garante os limites.

`orchestrators.count` inclui o principal. `workers.count` é o total de workers disponíveis em toda a execução, não a quantidade por orquestrador. Cada worker pertence a uma única frente por vez. A concorrência real é limitada por `execution.max_parallel_workers`.

## 4. Configuração de entrada

```yaml
schema_version: "1"
run_id: "migração-api-2026-09-24"
objective: "Produzir um plano de migração da API X para a API Y"
context:
  text: "Documentação, restrições e critérios fornecidos pelo solicitante."
  artifacts: []

orchestrators:
  count: 2
  agents:
    - id: principal
      role: primary
      model: "gpt-6-astra"
      instructions: "Planeje, distribua, valide evidências e sintetize."
    - id: coordenador-compatibilidade
      role: coordinator
      model: "gpt-5.6-terra"
      instructions: "Coordene a frente de compatibilidade e reporte lacunas."

workers:
  count: 3
  agents:
    - id: contratos
      specialty: "Comparar contratos e mudanças incompatíveis"
      model: "gpt-5.6-terra"
      tools: [document_search]
    - id: codigo
      specialty: "Localizar pontos de alteração no código"
      model: "gpt-6-astra"
      tools: [repository_read]
    - id: testes
      specialty: "Definir verificações de migração"
      model: "gpt-5.6-terra"
      tools: [document_search, repository_read]

execution:
  max_parallel_workers: 3
  max_model_calls: 20
  timeout_seconds: 600
  worker_timeout_seconds: 180
  max_retries_per_task: 1
  on_worker_failure: partial
  allowed_models: ["gpt-6-astra", "gpt-5.6-terra"]

output:
  language: pt-BR
  format: markdown
  require_evidence: true
```

Os nomes de modelo acima são apenas um exemplo. `allowed_models` é um catálogo local opcional; um erro de acesso ou compatibilidade retornado pela API durante a execução deve ser registrado como falha explícita, sem substituição silenciosa.

Na CLI de referência, `.env` pode sobrescrever contagens, modelos, limites, objetivo e caminhos. Variáveis exportadas no processo prevalecem sobre o arquivo. O YAML conserva o contexto e as especialidades; novos slots além dos definidos nele recebem especialidade genérica.

### Regras de validação

1. `objective` é obrigatório e descreve um resultado verificável.
2. `orchestrators.count >= 1`, `workers.count >= 1` e cada contagem é igual ao tamanho de `agents` correspondente.
3. Há exatamente um `role: primary`; os demais são `role: coordinator`. IDs são únicos entre todos os agentes.
4. Cada agente informa `model` explicitamente. Não há troca silenciosa de modelo em caso de erro.
5. `1 <= max_parallel_workers <= workers.count`; limites de chamadas e tempo são positivos.
6. Ferramentas citadas precisam existir no registro da aplicação. Cada agente recebe apenas as ferramentas de sua tarefa.
7. Se o objetivo não puder ser dividido em trabalho útil para os agentes configurados, o principal encerra com `status: rejected` e explica a incompatibilidade, sem inventar subtarefas.
8. `on_worker_failure` aceita `partial` ou `fail`. Todas as frentes e tarefas planejadas têm um responsável válido; nenhum orquestrador auxiliar fica sem frente.

## 5. Protocolo de execução

1. **Validar:** conferir schema, modelos, ferramentas, permissões e limites antes de chamar qualquer agente.
2. **Planejar:** o principal gera um plano estruturado com frentes, tarefas independentes, dependências, responsável e critério de aceite de cada tarefa. Cada tarefa tem um ID estável.
3. **Atribuir:** a aplicação verifica que nenhum worker recebe duas tarefas simultâneas e que o total ativo respeita `max_parallel_workers`. Com mais de um orquestrador, o principal atribui frentes explícitas aos auxiliares.
4. **Orientar e executar:** orquestradores auxiliares dão instruções às tarefas de suas frentes. Tarefas sem dependência rodam em paralelo; as dependentes aguardam os resultados necessários. Cada `Runner.run` recebe somente o contexto pertinente à tarefa.
5. **Revisar:** o orquestrador responsável verifica completude, evidências, conflitos e critérios de aceite. Pode solicitar uma correção dentro do orçamento e do limite de retry.
6. **Consolidar:** o principal reúne resultados, resolve divergências com base nas evidências e informa o que ficou inconclusivo. Encerra todos os trabalhos ativos antes de emitir a saída.
7. **Finalizar:** a aplicação grava o resultado estruturado, métricas e referências de trace. O `run_id` não é reutilizado para continuar conversa.

O principal mantém a responsabilidade pela resposta final. Esse arranjo segue o padrão de gerente da documentação do Agents SDK; handoff completo não é necessário para workers com tarefas delimitadas. [Orquestração e handoffs](https://developers.openai.com/api/docs/guides/agents/orchestration).

## 6. Contratos entre agentes

### Plano do principal

```json
{
  "tracks": [
    {"id": "compatibilidade", "orchestrator_id": "coordenador-compatibilidade"}
  ],
  "tasks": [
    {
      "id": "T1",
      "track_id": "compatibilidade",
      "worker_id": "contratos",
      "goal": "Listar mudanças incompatíveis entre X e Y",
      "inputs": ["context.artifacts"],
      "depends_on": [],
      "acceptance": "Cada mudança inclui evidência e impacto"
    }
  ]
}
```

### Resultado de worker

```json
{
  "task_id": "T1",
  "status": "completed",
  "findings": [
    {"claim": "Mudança observada", "evidence": "fonte ou artefato", "impact": "efeito prático"}
  ],
  "artifacts": [],
  "open_questions": [],
  "errors": []
}
```

### Saída final

```json
{
  "run_id": "migração-api-2026-09-24",
  "status": "completed",
  "answer": "Resposta final no formato solicitado",
  "completed_tasks": ["T1"],
  "incomplete_tasks": [],
  "evidence": [],
  "limitations": [],
  "usage": {"model_calls": 0, "elapsed_seconds": 0},
  "agent_models": {"principal": "gpt-6-astra"},
  "trace_ref": null
}
```

`status` aceita `completed`, `partial`, `failed` ou `rejected`. `partial` só é permitido quando `on_worker_failure: partial`; a resposta precisa listar tarefas faltantes e o efeito sobre a conclusão. Com `on_worker_failure: fail`, qualquer tarefa obrigatória não concluída produz `failed`. Contratos estruturados devem ser validados pela aplicação, inclusive quando produzidos por um modelo.

## 7. Falhas, limites e observabilidade

- Retry apenas para falha transitória ou saída estruturalmente inválida, até `max_retries_per_task`. A mesma tarefa mantém o mesmo ID, com número de tentativa separado.
- Timeout de worker cancela sua chamada e marca a tarefa como incompleta. O limite global cancela as tarefas pendentes e produz `partial` ou `failed`, conforme haja material suficiente para uma conclusão útil.
- O orçamento de chamadas inclui planejamento, workers, revisões e síntese. Ao atingir o limite, o principal encerra com o que estiver verificado.
- Logs e traces registram `run_id`, agente, modelo solicitado, tarefa, tentativa, duração, estado, uso e erro. Segredos e conteúdo sensível não entram nos logs operacionais.
- A CLI exibe barras por fase: planejamento, coordenação, workers, revisão e síntese.
- Tarefas que editam o mesmo recurso exigem atribuição serial ou isolamento por workspace; a aplicação não agenda edições conflitantes em paralelo. A documentação da Agents API também destaca a necessidade de coordenação quando agentes compartilham arquivos. [Multi-agent](https://developers.openai.com/api/docs/guides/agents-api/multi-agent).

## 8. Critérios de aceite da implementação

1. Uma configuração com 1 orquestrador e N workers executa até N tarefas independentes, respeitando o limite de concorrência.
2. Uma configuração com mais de 1 orquestrador distribui frentes sem duplicar tarefas nem ultrapassar o pool total de workers.
3. Traces e resultado mostram qual modelo foi solicitado para cada agente, sem substituição implícita.
4. Dependências são respeitadas, falhas isoladas seguem a política configurada e o processo termina dentro do timeout global.
5. A saída sempre segue o contrato final e distingue fatos verificados, lacunas e tarefas incompletas.
6. Execuções com contagens inválidas, modelos fora do catálogo configurado ou ferramentas ausentes falham na validação antes do planejamento; erros de acesso retornados pela API aparecem como falha explícita.

## 9. Fora do escopo desta versão

Memória entre execuções, workers criados dinamicamente acima da contagem configurada, conversas contínuas, aprovação humana durante a execução e troca automática de provedor ou modelo.
