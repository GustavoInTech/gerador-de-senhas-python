import random
import string
import tkinter as tk
from tkinter import messagebox

def gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""
    if usar_maiusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Nenhum tipo de caractere selecionado!"

    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

def gerar_varias_senhas():
    try:
        tamanho = int(entry_tamanho.get())
        quantidade = int(entry_quantidade.get())
        usar_maiusculas = var_maiusculas.get()
        usar_minusculas = var_minusculas.get()
        usar_numeros = var_numeros.get()
        usar_simbolos = var_simbolos.get()

        senhas = [gerar_senha(tamanho, usar_maiusculas, usar_minusculas, usar_numeros, usar_simbolos) for _ in range(quantidade)]
        
        with open("senhas_geradas.txt", "w") as arquivo:
            for senha in senhas:
                arquivo.write(senha + "\n")

        messagebox.showinfo("Senhas Geradas", "\n".join(senhas) + "\n\nAs senhas foram salvas em 'senhas_geradas.txt'.")
    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos.")

# Criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Senhas")

# Entrada para o comprimento da senha
tk.Label(janela, text="Comprimento da senha:").pack()
entry_tamanho = tk.Entry(janela)
entry_tamanho.pack()

# Entrada para a quantidade de senhas
tk.Label(janela, text="Quantidade de senhas:").pack()
entry_quantidade = tk.Entry(janela)
entry_quantidade.pack()

# Opções de tipos de caracteres
var_maiusculas = tk.BooleanVar()
var_minusculas = tk.BooleanVar()
var_numeros = tk.BooleanVar()
var_simbolos = tk.BooleanVar()

tk.Checkbutton(janela, text="Incluir letras maiúsculas", variable=var_maiusculas).pack()
tk.Checkbutton(janela, text="Incluir letras minúsculas", variable=var_minusculas).pack()
tk.Checkbutton(janela, text="Incluir números", variable=var_numeros).pack()
tk.Checkbutton(janela, text="Incluir símbolos", variable=var_simbolos).pack()

# Botão para gerar senhas
tk.Button(janela, text="Gerar Senhas", command=gerar_varias_senhas).pack()

# Iniciar a interface
janela.mainloop()
