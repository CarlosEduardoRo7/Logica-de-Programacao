# escrever um programa que imprima a tabuada de um número informado pelo usuário

num = int(input("Digite um numero: "))
cont = 0

while cont < 10:
    cont += 1
    tabuada = num * cont
    print(f"{num} x {cont} = {tabuada}")