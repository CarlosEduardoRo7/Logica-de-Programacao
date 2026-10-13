temp = []

for i in range(12):
    t = float(input(f"Digite a temperatura média do mês {i+1}: "))
    temp.append(t)
print(temp)

media = sum(temp)  / len(temp)
print(f"A média anual das temperaturas é de {media:.2f} C")