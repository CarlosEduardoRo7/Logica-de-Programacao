# faça um programa que receba como entrada os dados de um funcionário: 
# nome, número de horas trabalhadas, valor da hora trabalhada
# Após calcule seu salário bruto. Calcule um desconto de 2% de INSS
# E ao final mostrar seu nome e salário final calculado.

nome = input("Digite seu nome: ")
ht = float(input("Digite o número de horas trabalhadas: "))
vht = float(input("Digite o valor por hora trabalhada: "))
print("")

dia = ht*vht
salario = dia*31
desconto = salario/100
salariofinal = salario - desconto*2

print(f"{nome}, seu salário é {salariofinal} R$")