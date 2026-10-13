# Faça um programa que peça nome e nota do aluno (entre zero e dez). Mostre uma
# mensagem caso o valor nota seja inválido e continue pedindo até que o usuário informe
# um valor válido.

i = 0

while i < 10:
    nome = str(input("Digite seu nome: "))
    nota = float(input("Digite sua nota: "))
    i += 1

    if nota > -1:

        if nota < 11:

            print(f"Olá {nome}, sua nota é {nota}")
            break

        else:
            
            print("Nota inválida")

    else:
        
        print("Nota inválida")