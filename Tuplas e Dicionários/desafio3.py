frase = input("Digite uma frase: ")

palavras = frase.split()

frequencia={}

print(palavras)

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra]+=1
    else:
        frequencia[palavra]=1
        
print(frequencia)