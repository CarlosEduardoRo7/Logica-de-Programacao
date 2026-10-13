import random

def sorteio(n):
    if n == random.randint(1, 2):
        return "Você acertou!!"
    else:
        return "Número incorreto!"

numero = int(input("Tente advinhar um número de 1 a 100: "))

if (numero > 0) and (numero < 101):
    print(sorteio(numero))
else:
    print("Número indisponível!")