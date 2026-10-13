# Crie um programa que receba números digitados e exiba todos os números
# pares e ímpares até quando o número digitado for 0.

par = []
impar = []
n = 1
i = 0

while i < 10:

    if n != 0:

        n = int(input("Digite seu numero: "))
    
        if n % 2 != 0:
            if n != 0:
                impar.append(n)
            else:
                print("Numero igual a 0, encerrando programa.")
    
        elif n % 2 == 0:
            if n != 0:
                par.append(n)
            else:
                print("Numero igual a 0, encerrando programa.")
    
    else:
        print("Numero igual a 0, encerrando programa.")

    i += 1
    
    print("")
    print(f"Numeros pares: {par}")
    print(f"Numeros impares: {impar}")
    print("")