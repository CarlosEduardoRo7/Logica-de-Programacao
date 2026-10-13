carros = {"marca": "chevrolet", "modelo": "onix", "ano": 2022}

print("")
print(carros)

print("")
print(carros["marca"])
print(carros["modelo"])

print(carros.get("ano"))

print(carros.get("cor", "chave não encontrada"))
print("")

print(carros.keys())
print(carros.values())
print("")

# adcionar itens novos ao dicionário

carros["placa"] = "AQX1H54"
print(carros)

# deletando um item do dicionário

carros.pop("placa") # consegue salva o valor deletado em uma variavel
del carros["ano"] # deleta para sempre

print("")
print(carros)

# VERIFICANDO SE CHAVE OU VALOR ESTÁ NO DICIONÁRIO

print("")
print("marca" in carros) # retorna um bool true caso a chave estiver, ou false caso a chave não for encontrada no dicionário

# verificar se um determinado valor está no dicionário

print("")
print("onix" in carros.values()) # retorna True pois está no dicionário
print("prisma" in carros.values()) # retorna falso pois não está no dicionário

# iterando sobre um dicionário

print("")

for i in carros:
    print(i)
    print("")

for i in carros.values():
    print(i)
    print("")

for chave,valor in carros.items():
    print(f"{chave}: {valor}")

print("")