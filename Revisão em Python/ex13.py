tarefas = []

while True:

    print('''

1 - Adcionar nova tarefa
2 - Remover tarefa existente
3 - Exibir todas as tarefas
4 - Buscar tarefa especifica
5 - Sair

    ''')

    escolha = int(input(""))

    if escolha == 1:
        print("")
        t = input("Digite sua nova tarefa: ")
        tarefas.append(t)

    elif escolha == 2:
        print("")
        t = input("Remova uma tarefa: ")
        tarefas.remove(t)
    
    elif escolha == 3:
        print("")
        print(tarefas)
    
    elif escolha == 4:
        print("")
        t = input("Pesquise uma tarefa: ")
        print(f"Sua tarefa está na posição: {tarefas.index(t) + 1}")
    
    elif escolha == 5:
        print("")
        break

print("Programa encerrado")
print("")