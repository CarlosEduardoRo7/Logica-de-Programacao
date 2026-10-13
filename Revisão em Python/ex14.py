temperaturas = []

for i in range(12):
    t = float(input(f"Digite a temperatura do mês {i+1}: "))
    temperaturas.append(t)

print(f'''

Janeiro      -      {temperaturas[0]} C
Fevereiro    -      {temperaturas[1]} C
Março        -      {temperaturas[2]} C
Abril        -      {temperaturas[3]} C
Maio         -      {temperaturas[4]} C
Junho        -      {temperaturas[5]} C
Julho        -      {temperaturas[6]} C
Agosto       -      {temperaturas[7]} C
Setembro     -      {temperaturas[8]} C
Outubro      -      {temperaturas[9]} C
Novembro     -      {temperaturas[10]} C
Dezembro     -      {temperaturas[11]} C

Média Anual  -      {sum(temperaturas)/len(temperaturas)}
''')

md = sum(temperaturas)/len(temperaturas)

print("Temperaturas acima da média: ")
print("")

for i in range(12):
    if temperaturas[i] > md:
        if i == 0:
            print("Janeiro")
        elif i == 1:
            print("Fevereiro")
        elif i == 2:
            print("Março")
        elif i == 3:
            print("Abril")
        elif i == 4:
            print("Maio")
        elif i == 5:
            print("Junho")
        elif i == 6:
            print("Julho")
        elif i == 7:
            print("Agosto")
        elif i == 8:
            print("Setembro")
        elif i == 9:
            print("Outubro")
        elif i == 10:
            print("Novembro")
        elif i == 11:
            print("Dezembro")
    
print("")
        