from tkinter import *
def clique():
    texto.configure(text="Botao Clicado!")
tela=Tk()
tela.geometry("200x100")

texto=Label(tela,text="Clique aqui!")
texto.pack()

botao=Button(tela,text="Clique",commando=clique)
botao.pack()


tela.mainloop()

