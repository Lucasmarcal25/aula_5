from tkinter import *
janela=Tk()
janela.iconbitmap('C:\PROJETO/download.ico/')
janela.title("aula 5")
janela.geometry ("500x500") #larguraxaltura + dist esquerda + dist topo
janela.wm_resizable(width=False,height=False)

texto = Label(janela,text= "login")
texto.pack()
txtlogin = Entry()
txtlogin.pack()
texto = Label (janela,text="senha")
texto.pack()
txtsenha = Entry()
txtsenha.pack()

btentrar = Button(janela,text="Entrar",command="")
btentrar.pack()
janela.mainloop()
