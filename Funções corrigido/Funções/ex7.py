def eh_bissexto(ano):
 if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
 return True
 else:
 return False
# Exemplo de uso
ano = int(input("Digite o ano que deseja verificar: "))
resultado = eh_bissexto(ano)
print(f"O ano {ano} é bissexto? {resultado}")