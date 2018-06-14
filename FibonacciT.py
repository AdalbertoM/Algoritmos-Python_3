from tkinter import *

janela = Tk()
janela.title("Sequencia de fibonacci")

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))

def bt_click():
    sequencia = []
    for i in range(0, 19):
        sequencia.insert(i, fibonacci(i))
    lb["text"] = sequencia

bt = Button(janela, text="Iniciar sequencia", width=20, command=bt_click)
bt.place(x=100, y=150)

lb = Label(janela, text=" ")
lb.place(x=100, y=200)

janela.geometry("800x300+200+200")
janela.mainloop()
