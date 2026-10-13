print("")
irmaos = str(input("Você possui irmãos?: ")).lower()

if irmaos == "sim":
    
    print(" ")
    numero = float(input("Quantos irmãos você possui?: "))

    print(f"Você possui {numero:.0f} irmãos")

elif irmaos == "não":

    print("")
    escolha = str(input("Você gostaria de ter irmãos?: ")).lower()

    if escolha == "sim":

        print("")
        print(f"Você não possui irmãos e não gostaria de ter irmãos")

    elif escolha == "não":

        print("")
        print(f"Você não possui irmãos e gostaria de ter irmãos")

    else:

        print("")
        print("Insira uma resposta Válida")

else:
    print("Insira uma resposta válida")
    
print("")