lista = []
listabx = []
soma = 0

print("")

while True:
    
    nmr = float(input("Digite um valor: "))

    if nmr != -1:

        lista.append(nmr)
        soma += nmr

        if nmr < 7:

            listabx.append(nmr)
    
    else:
        break


print("")
print(f"A quantidade de valores é: {len(lista)}")

print("")
print(lista)

print("")
lista.sort(reverse=True)
print(lista)

print("")
print(f"A soma dos valores é: {soma}")

print("")
print(f"A média dos valores é: {soma/len(lista):.2f}")

print("")
print(listabx)

print("")
