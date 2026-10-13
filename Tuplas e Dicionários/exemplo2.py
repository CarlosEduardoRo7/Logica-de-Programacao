print("")
carros = {"marca": "chevrolet", "modelo": "onix", "ano": "2022"}
print(carros)

print("")
print(carros["marca"])
print(carros["ano"])
print("")

# --- função get não da erro caso não exista, demonstra "None" ---

print(carros.get("modelo"))
print("")

# --- adcionar e deletar ---

carros["NovaChave"] = "NovoItem"
print(carros)

del carros["NovaChave"]
print(carros)

carros.pop("marca")
print(carros)

# --------------------------

print("")
for aluno, notas in carros.items():
    print(f"{aluno}: {notas}")