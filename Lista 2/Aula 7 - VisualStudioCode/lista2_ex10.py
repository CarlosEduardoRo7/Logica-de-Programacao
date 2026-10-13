print("")
nome = str(input("Escreva seu nome: "))
temperatura = float(input("Digite a temperatura em Celsius: "))

if temperatura >= 0:

    
    if temperatura >= 18:
        if temperatura <= 30:
            print("")
            print(f"A temperatura está agradável, com {temperatura} graus.")

        else:
            print(f"A temperatura está quente, com {temperatura} graus.")
    else:
        print(f"A temperatura está fria, com {temperatura} graus.")
        

elif temperatura < 0:
    print("")
    print(f"A temperatura está muito fria, com {temperatura} graus.")

else:
    print("")
    print("A temperatura está em um valor inválido")