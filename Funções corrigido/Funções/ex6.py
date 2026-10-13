def numero_esta_na_lista(lista, numero):
 return numero in lista
# Exemplo de uso
lista = [1, 3, 5, 7, 9]
numero = int(input("Digite o número que deseja verificar na lista: "))
resultado = numero_esta_na_lista(lista, numero)
print(f"O número {numero} está na lista? {resultado}")
