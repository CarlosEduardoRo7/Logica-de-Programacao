print(" ")

nome = input("Escreva seu nome: ")
inicial = input("Digite a inicial do seu gênero: ")

print(" ")

if inicial == "F" :
    print(f"{nome}, você é do sexo feminino")
elif inicial == "M" :
    print(f"{nome}, você é do sexo masculino")
else :
    print(f"{nome}, seu sexo é indefinido")

print(" ")