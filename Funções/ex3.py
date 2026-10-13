# Escreva um script em linguagem Python com uma função para imprimir o nome e salário
# de um funcionário usando as seguintes condições. Deve aceitar o nome e o salário do
# funcionário. Se o salário estiver faltando na chamada de função, atribua o valor padrão 9000
# ao salário.

def impressao(nome, salario=9000):
    print(f"{nome} tem o salário de {salario} R$")

impressao("Carlos", 2000)
impressao("Julia")