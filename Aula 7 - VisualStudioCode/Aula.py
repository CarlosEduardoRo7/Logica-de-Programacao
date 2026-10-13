# -------------------------------- declaração de variáveis a baixo --------------------------------

a = 6
b = 7.8
c = "Cadu"
d = True

# -------------------------------- visualização dos tipos das variáveis --------------------------------

print(type(a))
print(type(b))
print(type(c))
print(type(d))

print("")

# -------------------------------- mostrando para o usuário a variável "a" --------------------------------

print(a)

print("")

# -------------------------------- mostrando string para o usuário --------------------------------

print("Hello World!!!")

print("")

# -------------------------------- combina texto com variável (com a virgula) --------------------------------

valor = 9.00
print("O valor digitado foi:", valor,)

print("")

# -------------------------------- combina texto com variável sem virgula, e com o uso de {} e "f" antes das aspas --------------------------------

print(f"Oi {c}, o valor digitado foi de {valor} reais")

print("")

#  -------------------------------- coletar informações do usuário com o input --------------------------------

nome = input("Digite o seu nome: ")
print("")

idade = input("Digite a sua idade: ")
print("")

print(f"Oi {nome}, tudo bem? Você tem {idade} anos")

print("")

# -------------------------------- pedir e somar dois valores --------------------------------

valor1 = float(input("Digite o primeiro valor: "))
print("")

valor2 = float(input("Digite o segundo valor: "))
print("")

soma = valor1 + valor2

print(f"A soma dos valores {valor1} e {valor2} é: {soma}")
print("")

# -------------------------------- operadores --------------------------------

a = 6
b = 2

soma = a+b
mult = a*b

# a elevado a b (7 elevado a 2)
pota = a**b

# a elevado a b (2 elevado a 7)
potb = b**a

div = a/b
divr = a//b

divs = a%b

print(" ")
print(f" Resultados: \n\
     Soma: {soma}\n\
     Multiplicação: {mult}\n\
     Potencia de a: {pota}\n\
     Divisão: {div}\n\
     Divisão resto de 0: {divr}\n\
     Resto da divisão: {divs}\n\
     Potencia de b: {potb}\n\ ")

# \n  pula a linha