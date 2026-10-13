task = ['estudar', 'fazer comida', 'caminhar', 'ler', 'brincar', 'treinar', 'trabalhar']

print('')

'''INDEX POSITIVO'''

# print(task[0])
# print(task[1])
# print(task[2])

'''INDEX NEGATIVO'''

# print(task[-1])
# print(task[-2])
# print(task[-3])

'''FATIAMENTO DA LISTA'''

print(task[1:5])

# do inicio até o valor definido

print('')
print(task[0: ])

# do valor definido até o final

print('')
print(task[-8: ])

# mudando o item de uma lista

print('')
task[-3] = 'jogar bola'
print(task)

# adicionando valores na lista

# adicionar no final com "append"

print('')
task.append('dormir')

# adicionar onde quiser com "insert"

task.insert(0,'acordar')
print(task)

# adicionar elemento onde quiser com "insert"

print('')
task.insert(2,'comer')
print(task)

# remover com "del"

print('')
del(task[1])
print(task)

# remover item de uma lista com "remove", só deleta o primeiro item com o nome correspondente

# print('')
# task.remove("acordar")
# print(task)

# recortar variavel com "pop"

print('')
itemRemovido = task.pop(0)
print(task)
print('')

print(itemRemovido)
print('')

# ordenar a lista

task.sort()
print(task)

# ordenar de trás para frente

print('')
task.sort(reverse=True)
print(task)
print('')

# retorna quantos itens tem na lista

print(len(task))
print('')

# conta quantas vezes um valor aparece

print(task.count('ler'))
print('')

# retorna o índice do valor (primeira ocorrência)

print(task.index('ler'))
print('')

# criar uma copia idependente da lsita

nova_task = task.copy()
print(nova_task)
print('')

# Remove todos os itens da lista

task.clear()
print(task)
print('')

# Junta os valores de duas listas

combinada = task + nova_task
print(combinada)
print('')