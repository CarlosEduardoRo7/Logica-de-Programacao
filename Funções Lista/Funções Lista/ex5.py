import datetime
import time

def reserva(destino, dia, mês, ano, hora, passageiros):
    return (f'\nReserva realizada com sucesso para {destino} em {dia}/{mês}/{ano} as {hora} horas, com {passageiros} passageiros.\n')
while True:
    
    destino = str(input("Escolha uma destino: ")).lower()

    ano = int(input("\nEscolha o ano: "))
    mês = int(input("Escolha o mês (número): "))
    dia = int(input("Escolha o dia: "))
    hora = str(input("Escolha a hora: "))
    passageiros = int(input("Quantos passageiros? "))

    print(reserva(destino, dia, mês, ano, hora, passageiros))
    time.sleep(2)