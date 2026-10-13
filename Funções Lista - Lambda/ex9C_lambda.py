import math

valor = float(input("Digite um valor: "))
arredondado = lambda valor: f"Valor arredondado para cima: {math.ceil(valor)}"
baixo = lambda valor: f"Valor arredondado para baixo: {math.floor(valor)}"

print(arredondado(valor))
print(baixo(valor))