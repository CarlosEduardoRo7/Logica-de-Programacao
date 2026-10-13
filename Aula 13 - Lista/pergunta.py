perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?",
]

resp = []

for i in perguntas:
    resposta = input(f"{i}\n (SIM/NÃO): ").upper()
    resp.append(resposta)

for i in resp:
    if i == "SIM" or i == "S":
        count += 1

if count == 2:
    print("você é considerado suspeito")

elif count <= 3 or count <= 4:
    print("você é considerado Cúmplice")

elif count == 5:
    print("você é considerado Assasino")

else:
    print("você é considerado inocente")