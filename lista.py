# Lista de tarefas simples em Python

# Função para exibir as opções do menu
def mostrar_menu():
    print("\nEscolha uma opção:")
    print("1. Adicionar tarefa")
    print("2. Visualizar tarefas")
    print("3. Editar tarefa")
    print("4. Excluir tarefa")
    print("5. Sair")

# Função para adicionar uma nova tarefa
def adicionar_tarefa(tarefas):
    tarefa = input("Digite a descrição da tarefa: ")
    tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

# Função para visualizar as tarefas
def visualizar_tarefas(tarefas):
    if not tarefas:
        print("\nNenhuma tarefa na lista.")
    else:
        print("\nTarefas:")
        for index, tarefa in enumerate(tarefas, 1):
            print(f"{index}. {tarefa}")

# Função para editar uma tarefa
def editar_tarefa(tarefas):
    visualizar_tarefas(tarefas)
    try:
        tarefa_id = int(input("\nDigite o número da tarefa que deseja editar: ")) - 1
        if tarefa_id < 0 or tarefa_id >= len(tarefas):
            print("Tarefa não encontrada.")
        else:
            nova_tarefa = input("Digite a nova descrição da tarefa: ")
            tarefas[tarefa_id] = nova_tarefa
            print("Tarefa atualizada com sucesso!")
    except ValueError:
        print("Por favor, insira um número válido.")

# Função para excluir uma tarefa
def excluir_tarefa(tarefas):
    visualizar_tarefas(tarefas)
    try:
        tarefa_id = int(input("\nDigite o número da tarefa que deseja excluir: ")) - 1
        if tarefa_id < 0 or tarefa_id >= len(tarefas):
            print("Tarefa não encontrada.")
        else:
            tarefa_removida = tarefas.pop(tarefa_id)
            print(f"Tarefa '{tarefa_removida}' excluída com sucesso!")
    except ValueError:
        print("Por favor, insira um número válido.")

# Função principal para rodar o programa
def main():
    tarefas = []
    while True:
        mostrar_menu()
        try:
            escolha = int(input("\nDigite a opção desejada: "))
            if escolha == 1:
                adicionar_tarefa(tarefas)
            elif escolha == 2:
                visualizar_tarefas(tarefas)
            elif escolha == 3:
                editar_tarefa(tarefas)
            elif escolha == 4:
                excluir_tarefa(tarefas)
            elif escolha == 5:
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    main()
