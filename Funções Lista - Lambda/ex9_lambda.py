import math

numero = int(input("Digite um número positivo: "))
raiz = lambda numero: f"Raiz de {numero} é: {math.sqrt(numero):.2f}"

if numero >= 0:
    print(raiz(numero))
else:
    print("Número não é positivo!")