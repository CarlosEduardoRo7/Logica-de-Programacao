# While True, repete infinitamente até que seja falso

while True:
    string_digitada = input("Digite uma palavra: ")
    if string_digitada.lower() == "sair":
        print("fim!")
        break