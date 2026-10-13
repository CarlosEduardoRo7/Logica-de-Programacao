tarefas = []

def adicionar(item):
    tarefas.append(item)
    print(f'{item} foi adicionado à lista.')

def remover(item):
    if item in tarefas:
        tarefas.remove(item)
        print(f'{item} foi removido da lista.')
    else:
        print(f'{item} não encontrado na lista.')

def visualizar():
    print(tarefas)

while True:
    print('''
----------------------------
1 - Adicionar item
2 - Remover item
3 - Visualizar itens
4 - Sair
----------------------------
''')
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        item = input("Item para ser adicionado: ")
        adicionar(item)

    elif escolha == 2:
        item = input("Item para ser removido: ")
        remover(item)

    elif escolha == 3:
        visualizar()

    elif escolha == 4:
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")
