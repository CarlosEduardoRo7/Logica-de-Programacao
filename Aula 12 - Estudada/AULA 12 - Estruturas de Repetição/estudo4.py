lista = []
i = 0

while i < 10:
    numero = float(input("Digite seu numero: "))
    lista.append(numero)
    i += 1

print(f"O valor máximo é: {max(lista):.0f}")
print(f"O valor mínimo é: {min(lista):.0f}")