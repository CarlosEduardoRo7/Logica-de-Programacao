# Faça um programa que peça para o usuário inserir uma idade e mostre na tela se ele é maior de idade ou não.

print("")

nome = str(input("Escreva seu nome: "))
idade = float(input("Digite a sua idade: "))

print("")

if idade >= 18:
    print(f"{nome}, você é maior de idade")
else: 
    if idade < 18:
        print(f"{nome}, você é menor de idade")
    else:
        print("Idade invalida")

print("")