# tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) – 58

nome = input("Escreva seu nome: ")
h = float(input("Digite sua Altura (em metros): "))
print("")

calculo = 72.7*h
pesoideal = calculo - 58

print(f"{nome}, seu peso ideal é {pesoideal:.2f} kg")
