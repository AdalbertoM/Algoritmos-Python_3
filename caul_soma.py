from tkinter import *

janela = Tk()
janela.title("Cauculadora soma")

def bt_click():

    if(str(n1.get()).isnumeric() and str(n2.get()).isnumeric()):
        nu1 = int(n1.get())
        nu2 = int(n2.get())

        lb["text"] = nu1 + nu2
    else:
        lb["text"] = "Valores invalidos!!!"

n1 = Entry(janela)
n1.place(x=100, y=100)
n2 = Entry(janela)
n2.place(x=100, y=140)

bt = Button(janela, text="Soma", width=20, command=bt_click)
bt.place(x=90, y=160)

lb = Label(janela, text="Resultado:")
lb.place(x=100, y=200)

janela.geometry("400x300+200+200")
janela.mainloop()
