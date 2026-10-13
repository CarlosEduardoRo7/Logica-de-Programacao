tarefas = []

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
        adicionar = lambda item: tarefas.append(item)
        adicionar(item)
        print(f'{item} foi adicionado à lista.')

    elif escolha == 2:
        item = input("Item para ser removido: ")
        remover = lambda item: tarefas.remove(item)
        remover(item)

    elif escolha == 3:
        visualizar = lambda: print(tarefas)
        visualizar()

    elif escolha == 4:
        print("Encerrando o programa.")
        break

    else:
        print("Opção inválida! Tente novamente.")
