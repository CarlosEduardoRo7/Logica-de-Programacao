estoque = {"Caneta": {"Preço": 8.99, "Quantidade": 20}, "Caneca": {"Preço": 20, "Quantidade": 50},}

print("")

print('''
----- TABELA DE OPÇÕES -----
      
1 - Adcionar Produto
2 - Atualizar Quantidade
3 - Calcular valor total do estoque
4 - Listar todos os produtos

''')

escolha = input("Escolha uma opção: ")

if escolha == "1":

    nome        = input("Nome do produto: ").lower()
    preco       = input("Preço do produto: ").lower()
    quantidade  = input("Qauntidade do produto: ").lower()

    estoque[nome] = {'preço': preco, 'quantidade': quantidade}

elif escolha == "2":

    nome = input("Digite o nome do produto que será atualizado a quantidade: ").lower()

    if nome in estoque:
        nova_quantidade = int(input("Nova Quantidade: "))
        estoque[nome]["quantidade"] = nova_quantidade
    else:
        print("Produto não encontrado")

elif escolha == "3":

    total = 0
    for produtos, dados in estoque.items():
        total += dados['Preço']*dados["Quantidade"]
        
    print(f"O valor total do estoque é: {total} R$")

elif escolha == "4":
    if estoque:
        print("Produtos no estoque: ")
        for produto, dados in estoque.items():
            print(f"{produto}: Preço R$ {dados['Preço']}, Quantidade {dados['Quantidade']}")
            print('')
            
else:
    print("Opção inválida")