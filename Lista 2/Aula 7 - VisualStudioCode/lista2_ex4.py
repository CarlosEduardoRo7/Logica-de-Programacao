# Faça um programa que peça para o usuário inserir um nome
# pergunte se ele gosta do nome
# em ambos os possíveis casos de resposta (Sim ou Não), mostre uma mensagem de sua escolha na tela.

print(" ")

nome = str(input("Escreva um nome: "))

print(" ")

resposta = str(input("Você gosta desse nome? ")).lower()

if resposta == "sim":

    print(" ")
    print("Legal!")

elif resposta == "não":

    print(" ")
    print("que pena")

else:

    print(" ")
    print("insira uma resposta válida")

print(" ")