print("Operação de divisão")
print("")

while True:
    n1 = int(input("Informe o primeiro número: "))
    n2 = int(input("Informe o segundo número: "))
    if n2 == 0:
        print("")
        print("Divisor = 0.\nPrograma encerrado...")
        break
    print("")
    print(f"{n1} / {n2} = {(n1/n2):.2f}")
    
print("")
print("Fim da operação de divisão")