nome = str(input("Digite o nome do aluno: "))
idade = int(input("Digite a sua idade: "))

if (idade >= 0) and (idade <= 2):
    print(f"O nivel escolar de {nome} é Berçário ")

elif (idade >= 3) and (idade <= 6):
    print(f"O nivel escolar de {nome} é Educação Infantil ")

elif (idade >= 7) and (idade <= 10):
    print(f"O nivel escolar de {nome} é Fundamental Nível I ")

elif (idade >= 11) and (idade <= 15):
    print(f"O nivel escolar de {nome} é Fundamental Nível II ")

elif (idade >= 16) and (idade <= 18):
    print(f"O nivel escolar de {nome} é Ensino Médio ")

else:
    print("Idade Inválida")