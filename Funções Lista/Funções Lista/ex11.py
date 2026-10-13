from datetime import datetime

data = datetime.now()
print("Data e hora atuais:", data)

ano = int(input("Ano de nascimento: "))

idade = data.year - ano
print("Idade: ", idade)