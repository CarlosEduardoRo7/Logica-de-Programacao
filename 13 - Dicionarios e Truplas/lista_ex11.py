pessoas_cadastradas = []

while True:
    pessoa = {}

    op = int(input("Digite sua opção: \n1- Cadastrar\n2-Sair\n"))

    if op == 1:

        print("")
        nome = input("Digite seu nome: ")
        idade = int(input("Digite sua idade: "))
        cpf = input("Digite seu cpf: ")

        pessoa.update({'nome': nome})
        pessoa.update({'idade': idade})
        pessoa.update({'CPF': cpf})
        print("")

        print(pessoa)
        print("")

        pessoas_cadastradas.append(pessoa)

    elif op == 2:
        print("")
        print("Fim do programa! ")
        break

    else:
        print("")
        print("Opção não disponivel")
        print("")

for i in pessoas_cadastradas:
    if i['idade'] < 18:
        print(i['nome'])