biblioteca = {"Torto Arado": {"Autor": "Itamar Vieira Junior", "Ano": "2019"}, "Tempo de Colher Flores": {"Autor": "André Zamboni", "Ano": "2023"}}
titulo = input("Procure um livro: ")

print("")
print(biblioteca.get(titulo, "Não encontrado"))