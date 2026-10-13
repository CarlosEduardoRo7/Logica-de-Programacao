print("")
l = int(input("Litros vendidos: "))

print('''

--- Tabela de Combustiveis ---

1 - álcool
2 - gasolina
''')

tp = int(input("Digite o tipo de combustivel: "))

if (tp == 2) and (l <= 20):
    print(f"Você recebeu 4% de desconto, ficando assim: {((5.65*l) - (((5.65*l)/100)*4)):.2f} R$")

elif (tp == 2) and (l > 20):
    print(f"Você recebeu 4% de desconto, ficando assim: {((5.65*l) - (((5.65*l)/100)*5)):.2f} R$")

if (tp == 1) and (l <= 20):
    print(f"Você recebeu 4% de desconto, ficando assim: {((4.22*l) - (((5.65*l)/100)*3)):.2f} R$")

elif (tp == 1) and (l > 20):
    print(f"Você recebeu 4% de desconto, ficando assim: {((4.22*l) - (((5.65*l)/100)*4)):.2f} R$")