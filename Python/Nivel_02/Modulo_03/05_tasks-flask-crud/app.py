# Documentação do Flask: 
# https://flask.palletsprojects.com/en/stable/quickstart/#routing
from flask import Flask, request, jsonify
from models.task import Task

# __name__ = "__main__"
app = Flask(__name__)

# CRUD
# Create, Read, Update and Delete = Criar, Ler, Atualizar e Deletar
# Tabela: Tarefa

tasks = []
task_id_control = 1    # criamos ela no global para que tenha um controle, porque se criassemos ela dentro, toda vez que fizessemos uma requisição
#   ela seria atribuida como 1, com isso faria que os itendificadores, ficassem duplicados

@app.route('/tasks', methods=['POST']) # posso colocar mais de um método, exemplo: methods=['POST', 'GET', 'ETC']
def create_tasks():
    global task_id_control      # ativando o global essa função vai ter acesso a variável task_id_control global
    data = request.get_json()
    new_task = Task(id=task_id_control, title=data['title'], description=data.get("description", ""))
    task_id_control += 1    # sempre que for tentar fazer uma interação de uma variável local com uma global,
#   é necessário especificar dentro da função a variável global, exemplo: global task_id_control
    tasks.append(new_task)
    print(tasks)
    return jsonify({"message:": "Nova tarefa criada com sucesso", "id": new_task.id})

@app.route('/tasks', methods=['GET'])
def get_tasks():
    task_list = []
    
    ## 1 forma:
    # for task in tasks:
    #     task_list.append(task.to_dict())
    # output = {
    #     "tasks": task_list,
    #     "total_tasks": 0
    # }

    ## 2 forma:
    task_list = [task.to_dict() for task in tasks]
    output = {
        "tasks": task_list,
        "total_tasks": 0
    }
    return jsonify(output)

@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())

    return jsonify({"message": "Não foi possível encontrar a atividade"}), 404

@app.route('/tasks/<int:id>', methods=["PUT"])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break

    print(task)
    if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']

    print(task)
    return jsonify({"message": "Tarefa atualizada com sucesso"})

@app.route('/tasks/<int:id>', methods=["DELETE"])
def delete_task(id):
    task = None
    for t in tasks:
        print(t.to_dict())
        if t.id == id:
            task = t
            break

    if not task:    # o mesmo que if task == None:
        return jsonify({"message": "Não foi possível encontrar a atividade"}), 404
    
    tasks.remove(task)
    return jsonify({"message": "Tarefa deletada com sucesso"})

####
#   Rota de exemplo de user
# @app.route('/user/<int:user_id>')
# def show_user(user_id):
#     print(user_id)
#     print(type(user_id))
#     return "%s" % user_id   # convertendo o inteiro para string
####
    
if __name__ == "__main__":
    app.run(debug=True)     # Método usado só para teste de projetos, não é algo feito para o servidor/cliente, apenas desenvolvimento local