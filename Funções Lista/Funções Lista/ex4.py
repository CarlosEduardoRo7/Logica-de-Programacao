contatos = {}

def adicionar(item, numero):
    contatos[item] = numero
    print(f'{item} foi adicionado à lista.')

def remover(item):
    if item in contatos:
        del contatos[item]
        print(f'{item} foi removido da lista.')
    else:
        print(f'{item} não encontrado na lista.')

def visualizar():
    print(contatos)

while True:
    print('''
----------------------------
1 - Adicionar contato
2 - Remover contatos
3 - Visualizar contatos
4 - Sair
----------------------------
''')
    
    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        item = input("Contato para ser adicionado: ")
        numero = input("Numero do contato: ")
        adicionar(item, numero)

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