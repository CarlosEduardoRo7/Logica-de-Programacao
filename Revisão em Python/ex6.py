print("")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
print("")

if (idade < 16 ):
    print(f"{nome}, você é não votante")

elif (idade >= 16) and (idade < 18):
    print(f"{nome}, você pode votar de forma opcional")

elif (idade >= 18) and (idade <= 65):
    print(f"{nome}, você é um eleitor obrigatório")

elif (idade > 65):
    print(f"{nome}, você é um eleitor facultativo")

else:
    print("idade invalida")

print("")