'''Janela de boas-vindas'''
 
import tkinter as tk
 
# Função que gera a mensagem de boas-vindas
def saudacao():
    nome = entry_nome.get()                                                                                                         # Obtém o nome digitado
    if nome.strip():
        mensagem.config(text=f"Seja bem-vindo, {nome}.")                                                                            # Atualiza o rótulo com a mensagem
    else:
        mensagem.config(text="Por favor, digite um nome válido.")                                                                   # Mensagem de erro para nome vazio
 
# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Boas-vindas")                                                                                              # Título da janela
janela.geometry("400x250")                                                                                                          # Largura x Altura
 
# Título da aplicação
titulo = tk.Label(janela, text="Interface Gráfica com Python", font=("Arial", 16, "bold"))
titulo.pack(pady=10)                                                                                                                # Margem vertical
 
# Rótulo explicativo
rotulo = tk.Label(janela, text="Digite o seu nome abaixo", font=("Arial", 12))
 
# Campo de entrada para o nome
entry_nome = tk.Entry(janela, font=("Arial", 12), justify="center")                                                                 # Campo centralizado
entry_nome.pack(pady=5)
 
# Botão para gerar a mensagem de boas-vindas
botao = tk.Button(janela, text="Gerar Boas-vindas", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=saudacao)         # Comando do botão
botao.pack(pady=10)
 
# Rótulo para exibir a mensagem de boas-vindas
mensagem = tk.Label(janela, text="", font=("Arial", 12), fg="#1f75fe")                                                              # Rótulo para a mensagem
mensagem.pack(pady=10)
 
# muda o fundo
# janela.configure(bg="#ffffff")                                                                                                    # Cor de fundo da janela
 
# Inicia o loop principal da interface gráfica
janela.mainloop()