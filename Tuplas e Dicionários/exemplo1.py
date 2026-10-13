minha_tupla  =  (1, 2, 3, "hello", True, 'World', 25)
primeiro_elemento = minha_tupla[0]
ultimo_dois = minha_tupla[-2:]

print(" ")
print(primeiro_elemento)
print(ultimo_dois)
print(" ")

for i in minha_tupla:
    print(f'itens da lista {i}')

print(" ")

# enumerate(iterable, start)

for indice, valor in enumerate(minha_tupla):
    print(f"O valor na posição {indice} é {valor}")

print(" ")