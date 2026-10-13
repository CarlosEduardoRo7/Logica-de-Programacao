print(''' Escolha entre 3 opções de bebidas:
a) água
b) refri
c) água com gás''')

print("")

escolha = str(input("Escreva sua escolha: ")).lower()

print("")

if escolha == "a":
    print("Sua escolha foi água com gás")

elif escolha == "b":
    print("Sua escolha foi um refri")

else:
    if escolha == "c":
        print("Sua escolha foi água com gás")
    else: 
        print("Valor inválido")

print("")