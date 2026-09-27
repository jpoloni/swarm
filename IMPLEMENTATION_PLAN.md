# Plano de implementação

Base: [SPEC.md](SPEC.md). Estado: implementação local concluída; o teste com a API depende de `OPENAI_API_KEY`.

## Entregáveis

1. Pacote Python `swarm_oneshot` com configuração tipada, validação do plano, adaptador OpenAI Agents SDK, agendador de tarefas, orçamento e resultado estruturado.
2. CLI `swarm-oneshot` com `validate` e `run`, saída JSON e barras de progresso para planejamento, workers, revisão e síntese.
3. Exemplo de configuração sem ferramentas externas, pronto para teste E2E com chave.
4. Testes locais com adaptador simulado e roteiro E2E com verificações automáticas.
5. README com instalação, execução e limites conhecidos.

## Etapas e critérios de conclusão

| Etapa | Trabalho | Critério |
|---|---|---|
| 1. Contratos | Esquemas de configuração, plano, resultados e saída | Configuração inválida rejeitada com erro legível |
| 2. Agendador | Plano, dependências, pool de workers, coordenadores, retry e timeout | Cada tarefa executa uma vez por tentativa e respeita dependências e concorrência |
| 3. SDK | `Agent` por participante, modelo explícito, `Runner.run`, saída tipada e trace | Modelos configurados chegam ao agente correspondente |
| 4. Operação | CLI, JSON, barras de progresso e relatório de uso | Usuário acompanha fases e recebe artefato final |
| 5. Testes | Unitários locais e E2E com API real | Testes locais passam; E2E fica pronto para receber a chave |

## Decisões

- Python 3.11+ e OpenAI Agents SDK. Cada chamada recebe um `Agent` com modelo próprio. Saídas intermediárias usam modelos Pydantic via `output_type`, conforme a [documentação oficial](https://developers.openai.com/api/docs/guides/agents/define-agents).
- O agendamento é da aplicação: o modelo propõe o plano, mas a aplicação valida IDs, dependências, responsáveis e limites antes de executar.
- Workers são slots configurados e podem executar várias tarefas em sequência. Um lock por worker impede tarefas simultâneas no mesmo slot.
- Cada coordenador auxiliar orienta sua frente antes da execução e revisa os resultados depois. O principal conserva a responsabilidade pelo plano global e pela resposta final.
- `max_model_calls` é um teto conservador: cada `Runner.run` reserva antecipadamente seu máximo de turnos; turnos não usados são devolvidos quando o SDK fornece uso. Uma chamada interrompida consome a reserva por segurança.
- Traces do SDK ficam agrupados por `run_id`; logs locais não incluem prompts nem chaves. O SDK oferece [tracing](https://developers.openai.com/api/docs/guides/agents/integrations-observability), e seu resultado expõe uso por chamada.
- O modo E2E usa objetivo e contexto embutidos no arquivo de exemplo para que a única credencial pendente seja `OPENAI_API_KEY`.

## Ordem de construção

1. Contratos e validação.
2. Adaptador do SDK e ferramentas de leitura.
3. Orquestrador assíncrono e orçamento.
4. CLI, barras e exemplo.
5. Testes locais e runner E2E.
6. Revisão da documentação e execução sem chave para conferir a prontidão.

## Riscos a verificar no E2E

- Disponibilidade dos modelos na conta usada.
- Capacidade dos modelos de produzir os contratos estruturados no cenário real.
- Contagem de uso e comportamento de cancelamento do SDK na versão instalada.
- Latência e custo de uma execução com múltiplos agentes.
