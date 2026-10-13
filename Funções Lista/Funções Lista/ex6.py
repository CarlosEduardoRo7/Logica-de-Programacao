def valorPagamento(dias,valor):
    porcentagem = ((valor/100))
    total = valor + (porcentagem*3) + (porcentagem*0.1)
    return total

while True:
    dias = int(input("Informe os dias de atraso para o pagamento: "))
    valor = float(input("Informe o valor do pagamento: "))

    if valor > 0:
        print(f"Você precisa pagar {valorPagamento(dias,valor)} R$")
    else:
        print("Nenhuma divida, encerrando programa")