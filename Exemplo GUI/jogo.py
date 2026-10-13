'''Jogo em Python: JoKenPo'''
 
import tkinter as tk
import random
 
from tkinter import messagebox
 
# Função para jogar JoKenPo
def jogar(escolha_player):
    opcoes = ['🪨 Pedra', '🧾 Papel', '✂️ Tesoura']
    escolha_CPU = random.choice(opcoes)
   
    # Exibe o que cada jogador escolheu
    label_resultado.config(text=f"Você escolheu: {escolha_player}\nCPU escolheu: {escolha_CPU}")
   
    # Determina o vencedor
    if escolha_player == escolha_CPU:
        messagebox.showinfo("Resultado", "Empate.")
       
    elif (escolha_player == '🪨 Pedra' and escolha_CPU == '✂️ Tesoura') or \
         (escolha_player == '🧾 Papel' and escolha_CPU == '🪨 Pedra') or \
         (escolha_player == '✂️ Tesoura' and escolha_CPU == '🧾 Papel'):
        messagebox.showinfo("Resultado", "Você venceu.")
       
    else:
        messagebox.showinfo("Resultado", "CPU venceu.")
       
# Criação da janela principal
janela = tk.Tk()
janela.title("JoKenPo: Python Edition")
janela.geometry("400x250")
 
# Título principal da janela
titulo = tk.Label(janela, text="JoKenPo Pythônico", font=("Arial", 16, "bold"))
titulo.pack(pady=10)
 
# Instruções para o jogador & resultado
label_resultado = tk.Label(janela, text="Escolha uma das opções abaixo.", font=("Arial", 12))
label_resultado.pack(pady=20)
 
# Botões para as escolhas do jogador
frame_botoes = tk.Frame(janela, bg="#f0f0f0")
frame_botoes.pack(pady=10)
 
btn_pedra = tk.Button(frame_botoes, text="🪨 Pedra", font=("Arial", 12), width=10, command=lambda: jogar('🪨 Pedra'))
btn_pedra.grid(row=0, column=0, padx=5)
 
btn_papel = tk.Button(frame_botoes, text="🧾 Papel", font=("Arial", 12), width=10, command=lambda: jogar('🧾 Papel'))
btn_papel.grid(row=0, column=1, padx=5)
 
btn_tesoura = tk.Button(frame_botoes, text="✂️ Tesoura", font=("Arial", 12), width=10, command=lambda: jogar('✂️ Tesoura'))
btn_tesoura.grid(row=0, column=2, padx=5)
 
# Inicia o loop principal da interface gráfica
janela.mainloop()