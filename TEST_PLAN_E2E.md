# Plano de testes E2E

**Pré-requisito pendente:** `OPENAI_API_KEY` preenchida no `.env` ou exportada no shell, com acesso aos modelos dos arquivos de exemplo. Instalação e testes locais não dependem da chave.

## Ambiente e comando

```sh
python3 -m venv venv
venv/bin/python -m pip install -e '.[dev]'
# Preencha OPENAI_API_KEY no .env.
venv/bin/python scripts/e2e.py
```

O script executa `examples/e2e.yaml` e `examples/e2e_multi.yaml` pela CLI real e grava os resultados em `artifacts/e2e-result.json` e `artifacts/e2e-multi-result.json`. Não imprime a chave. Se a variável estiver ausente, encerra antes de fazer chamadas externas com instrução clara.

## Cenários

| ID | Cenário | Resultado esperado |
|---|---|---|
| E1 | Configuração de 1 orquestrador e 2 workers com modelos explícitos | Plano válido, tarefas concluídas, saída final estruturada |
| E2 | Execução paralela de tarefas independentes | Barras chegam a 100%; cada tarefa tem um worker e evidência |
| E3 | Dependência entre tarefas, quando gerada pelo planejador | Tarefa dependente inicia após os resultados necessários |
| E4 | Configuração com 2 orquestradores | Cada coordenador recebe frente; principal sintetiza |
| E5 | Modelo inválido ou sem acesso | Falha explícita, sem troca automática de modelo |
| E6 | Timeout/budget pequeno | Encerramento controlado com status e lacunas |

O teste automatizado com chave cobre E1, E2 e E4. E3, E5 e E6 são cenários de aceitação guiada; seus invariantes de agendamento e falha são cobertos por testes locais determinísticos. Não há garantia de que um planejador LLM gere uma dependência específica sem instrução específica para isso.

## Verificações do script E2E

1. Processo termina com código zero e resultado JSON válido.
2. `run_id` confere com a configuração, `status == completed` e `incomplete_tasks` é vazio.
3. Todas as tarefas concluídas aparecem no resultado e a resposta não está vazia.
4. `usage.model_calls > 0`; relatório registra modelo de cada agente executado e evidência na resposta.
5. Arquivo de saída não contém `OPENAI_API_KEY`.

## Evidências a guardar

Os dois JSONs em `artifacts/`, saída da CLI com barras de progresso e traces agrupados por `run_id`. Registrar versão do pacote, modelos usados, duração e eventuais erros de acesso. Nunca salvar a chave no repositório.
