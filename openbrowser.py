import webbrowser
from tkinter import *


def abrir(url):
    webbrowser.open(url)


janela = Tk()
janela.title("Abrir Sites")
janela.geometry("300x250")


texto = Label(janela, text="Escolha um site para abrir:")
texto.pack(pady=10)

# Botões para os sites
botao_google = Button(janela, text="Google", command=lambda: abrir("https://google.com"))
botao_google.pack(pady=5)

botao_youtube = Button(janela, text="YouTube", command=lambda: abrir("https://youtube.com"))
botao_youtube.pack(pady=5)

botao_github = Button(janela, text="GitHub", command=lambda: abrir("https://github.com"))
botao_github.pack(pady=5)

botao_climatempo = Button(janela, text="Climatempo", command=lambda: abrir("https://www.climatempo.com.br/"))
botao_climatempo.pack(pady=5)

botao_globo = Button(janela, text="Globo Esporte", command=lambda: abrir("https://ge.globo.com"))
botao_globo.pack(pady=5)


janela.mainloop()
