# faça um programa que leia a largura e a altura de uma parede em metros
# e calcule a sua área e a quantidade da tinta necessária para pinta-la 
# sabendo que cada litro de tinta, pinta uma área de 2m².

print("")
b = float(input("Digite a largura em metros: "))
a = float(input("Digite a altura em metros: "))
print("")

mq = b*a

print(f"Será necessário {mq/2} metros quadrados de tinta para pintar a parede")
