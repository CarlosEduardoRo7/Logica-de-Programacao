import math

angulo = int(input("Digite um angulo em graus: "))
calculo = lambda angulo: f"o Seno de {angulo} é: {math.sin(angulo):.2f}"

print(calculo(angulo))