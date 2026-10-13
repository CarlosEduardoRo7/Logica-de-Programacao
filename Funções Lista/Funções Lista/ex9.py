import math

numero = int(input("Digite um número positivo: "))

if numero >= 0:
    print(f"Raiz de {numero} é: {math.sqrt(numero):.2f}")
else:
    print("Número não é positivo!")