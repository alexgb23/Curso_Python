from tkinter import *

# Estilo para los Label
Label_style = {
    'font': ('Arial', 18),
    'padx': 14,
    'pady': 14,
    'bg': '#f0f0f0',
    'fg': 'black'  # Color de texto
}

Label1_style = {
    'font': ('Arial', 12),
    'padx': 14,
    'pady': 14,
    'bg': '#f0f0f0',
    'fg': 'black'  # Color de texto
}
root = Tk()

Label(root, text="Introduce tus datos", **
      Label_style).grid(row=0, column=0, columnspan=2)

Label(root, text="Introduce tu nombre", **Label1_style).grid(row=1, column=0)
entrada = Entry(root, bd=1, relief='solid')  # Borde sólido
entrada.grid(row=1, column=1, padx=10, pady=5)  # Gap alrededor

Label(root, text="Introduce tu contraseña", **Label1_style).grid(row=2, column=0)
entrada2 = Entry(root, show='*', bd=1, relief='solid')  # Borde sólido
entrada2.grid(row=2, column=1, padx=10, pady=5)  # Gap alrededor


def clicar_boton():
    textocapturado = entrada.get()
    contraseña = entrada2.get()
    entrada.delete(0, END)
    entrada2.delete(0, END)
    texto = Label(root, text="Se ah enviado Correctamente")
    texto.grid(row=3, column=0)
    texto1 = Label(root, text=textocapturado)
    texto1.grid(row=4, column=0)
    texto2 = Label(root, text=contraseña)
    texto2.grid(row=5, column=0)


boton1 = Button(root, text="Enviar", bg="green"
                , command=clicar_boton)
boton1.grid(row=6, column=0, columnspan=2, sticky='ew', padx=10, pady=10)

root.mainloop()
