def soma(a, b, c):
    soma = (a + b)
    if soma > c:
        return "True"
    else:
        return "False"
    
a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))
c = int(input("Digite o parametro: "))
resultado = soma(a, b, c)

print(f"{a} + {b} é maior que {c}? {resultado}")