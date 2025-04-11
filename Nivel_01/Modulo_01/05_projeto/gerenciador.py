# Projeto com base a estrutura while, para testar sua funcionalidade
#1.
def adicionar_tarefa(tarefas, nome_tarefa): # é possível passar um padrão para tarefa, caso não coloque nenhuma tarefa, exemplo: nome_tarefa="tarefa padrão"
    # tarefa: nome da tarefa
    # completada: indicar se essa tarefa já foi completada ou não
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"\nTarefa {nome_tarefa} foi adicionada com sucesso!")
    return 

#2.
def ver_tarefas(tarefas):
    print("\nLista de tarefas:")
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "✓" if tarefa["completada"] else " "
        nome_tarefa = tarefa["tarefa"]
        print(f"{indice}. [{status}] {nome_tarefa}")
    return

#3.
def atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) - 1 # tratamento da informação, pois o usuário o indice começa no 1 e não no 0 e também transformando em int
    if indice_tarefa_ajustado >= 0 and indice_tarefa_ajustado < len(tarefas):
        tarefas[indice_tarefa_ajustado]["tarefa"] = novo_nome_tarefa
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome_tarefa}")
    else:
        print("Indice de tarefa inválido.")
    return

#4.
def completar_tarefa(tarefas, indice_tarefa):
    indice_tarefa_ajustado = int(indice_tarefa) -1
    tarefas[indice_tarefa_ajustado]["completada"] = True
    print(f"Tarefa {indice_tarefa} marcada como completada")
    return

#5.
def deletar_tarefas_completadas(tarefas):
    for tarefa in tarefas:
        if tarefa["completada"]: # no python não é necessário cofazer a comparação com True/ == True
            tarefas.remove(tarefa)
    print("Tarefas completadas foram deletadas.")
    return

tarefas = []
while True:
    print("\nMenu do Gerenciador de Lista de tarefas:")
    print("1. Adicionar tarefa")
    print("2. Ver tarefa")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("\nDigite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    
    elif escolha == "2":
        ver_tarefas(tarefas)
    
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja atualizar: ")
        novo_nome = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefas(tarefas, indice_tarefa, novo_nome)

    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = input("Digite o número da tarefa que deseja completar: ")
        completar_tarefa(tarefas, indice_tarefa)

    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)

    elif escolha == "6":
        break


print("\nPrograma finalizado")