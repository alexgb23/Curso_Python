from tkinter import *

root=Tk()

entrada = Entry(root)
entrada.grid(row=0, column=0)

def clicar_boton():
    textocapturado = entrada.get()
    entrada.delete(0, END)
    texto= Label(root, text="Se ah enviado Correctamente")
    texto.grid(row=2, column=0)
    texto1 = Label(root, text=textocapturado)
    texto1.grid(row=3, column=0)

boton1 = Button(root, text="Enviar",bg="green", padx=100, pady=25, command=clicar_boton)
boton1.grid(row=1, column=0)

root.mainloop()