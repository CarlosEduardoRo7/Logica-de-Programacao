
while True:
    dias = int(input("Informe os dias de atraso para o pagamento: "))
    valor = float(input("Informe o valor do pagamento: "))
    valorPagamento = lambda dias, valor: valor + ((valor/100)*3) + ((valor/100)*0.1)

    if valor > 0:
        print(f"Você precisa pagar {valorPagamento(dias,valor)} R$")
    else:
        print("Nenhuma divida, encerrando programa")