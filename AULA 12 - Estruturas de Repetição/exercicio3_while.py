numeros = []
i = 1

while i <= 10:
    numero = float(input(f"Digite seu número: "))
    numeros.append(numero)
    i += 1

print(f"Seu valor máximo é : {max(numeros)}")
print(f"Seu valor mínimo é : {min(numeros)}")