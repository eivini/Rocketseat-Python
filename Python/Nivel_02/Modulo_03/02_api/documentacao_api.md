
[x] https://swagger.io/
[x] https://editor.swagger.io/

## API da Rocketseat
openapi: 3.0.0
info:
  title: API de Gerenciamento de Tarefas
  description: Documentação da API para o gerenciamento de tarefas (To-Do List)
  version: 1.0.0
servers:
  - url: http://127.0.0.1:5000
    description: Servidor de Desenvolvimento
paths:
  /tasks:
    get:
      summary: Obter todas as tarefas
      responses:
        '200':
          description: Lista de tarefas obtida com sucesso
          content:
            application/json:
              schema:
                type: object
                properties:
                  tasks:
                    type: array
                    items:
                      type: object
                      properties:
                        id:
                          type: integer
                        title:
                          type: string
                        description:
                          type: string
                        completed:
                          type: boolean
                  total_tasks:
                    type: integer
    post:
      summary: Criar nova tarefa
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              properties:
                title:
                  type: string
                description:
                  type: string
              required:
                - title
      responses:
        '200':
          description: Nova tarefa criada com sucesso
  '/tasks/{taskId}':
    put:
      summary: Atualizar tarefa existente
      requestBody:
        required: true
        content:
          application/json:
            schema:
              type: object
              description: Dados da tarefa a serem atualizados
              properties:
                title:
                  type: string
                description:
                  type: string
                completed:
                  type: boolean
              required:
                - title
      parameters:
        - name: taskId
          in: path
          description: ID da tarefa a ser atualizada
          required: true
          schema:
            type: integer

      responses:
        '200':
          description: Tarefa atualizada com sucesso
    delete:
      summary: Deletar tarefa existente
      parameters:
        - name: taskId
          in: path
          description: ID da tarefa a ser deletada
          required: true
          schema:
            type: integer
      responses:
        '200':
          description: Tarefa deletada com sucesso
###### ###### ###### ###### ###### ###### ###### ######
# As diferenças de cores são definidas pelos métodos

    • GET = utilizado para recuperar informações
        [200] - Lista de tarefas obtida com sucesso

    • POST = utilizado para inserir informações
        Request body
        Example Value | Schema
            {
                "title": "string",
                "description": "string"
            }
        [200] - Nova tarefa criada com sucesso

    • PUT = atualização de uma informação existente
        taskId * | ID da tarefa a ser atualizada
        integer (path) | taskId
        Request body
        Example Value | Schema
            {
                "title": "string",
                "description": "string",
                "completed": true
            }
        [200]	- Tarefa atualizada com sucesso

    • DELETE = deleta uma tarefa existente
        taskId * | ID da tarefa a ser deletada
        integer (path) | taskID
        [200]	- Tarefa deletada com sucesso