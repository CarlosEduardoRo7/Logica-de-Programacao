print("")
nome        = str(input("Digite o seu nome: "))
nomep       = str(input("Digite o nome do produto: "))
quantidade  = int(input("Digite a quantidade: "))
preco       = int(input("Digite a preço: "))

print('''
--------- Tabela de Pagamentos ---------
      
1 - À vista em dinheiro
2 - À vista em cartãp de crédito
3 - Duas Vezes
4 - Três Vezes
      
''')

pagamento = int(input("Digite a forma de pagamento: "))


if pagamento == 1 :
    print(f"{nome}, você escolheu pagar à vista em dinheiro, o resultado fica { ((preco -(preco/100)*10)*quantidade) } R$")

elif pagamento == 2 :
    print(f"{nome}, você escolheu pagar à vista em cartão de crédito, o resultado fica { ((preco -(preco/100)*5)*quantidade) } R$")

elif pagamento == 3 :
    print(f"{nome}, você escolheu pagar em duas vezes, o resultado fica { ((preco)*quantidade) } R$")

elif pagamento == 2 :
    print(f"{nome}, você escolheu pagar à vista em cartão de crédito, o resultado fica { ((preco + (preco/100)*5)*quantidade) } R$")

else:
    print("Valores Inválidos")
    
print("")