import math

def hipotenusa(oposto, adjacente):
    hipotenusa = oposto**2 + adjacente**2
    return math.sqrt(hipotenusa)

oposto = int(input("Digite o valor do cateto oposto: "))
adjacente = int(input("Digite o valor do cateto adjacente: "))

print(f"A hipotenusa vale: {hipotenusa(oposto, adjacente):.2f}")