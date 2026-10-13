nome    =   str(input("Digite o seu nome: "))
idade   =   int(input("Digite a sua idade: "))
peso    =   int(input("Digite a seu peso: "))

if (idade > 0) and (idade <= 15):
    print(f"{nome}, você não possui idade necessária para doar sangue")

else:
    if (idade >= 16) and (idade <= 17) and (peso >= 55):
        print(f"{nome}, você pode doar sangue com autorização de seus pais")
    else:
        if (peso < 55):
            print(f"{nome}, você não possui peso necessário para doar sangue")
        else:
            if (idade >= 18) and (idade <= 69) and (peso >= 60):
                print(f"{nome}, você pode doar sangue")
            else:
                if (peso < 60):
                    print(f"{nome}, você não possui peso necessário para doar sangue")
                else:
                    if (idade > 69):
                        print(f"{nome}, você não pode doar sangue devido a idade necessária")
                    else:
                        print("Informações Inválidas")