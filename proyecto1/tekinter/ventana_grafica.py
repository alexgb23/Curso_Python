# import tkinter as tk
from tkinter import *

# root=tk.Tk()
root = Tk()

etiqueta = Label(root, text="Bienvenido a la ventana grafica")
etiqueta.pack()

marco_principal = Frame()
marco_principal.pack()
marco_principal.config(width="400", height="400")
marco_principal.config(bg="red")

texto=Label(root, text="Capitulo 1")
texto.pack()

marco_principal2 = Frame()
marco_principal2.pack()
marco_principal2.config(width="400", height="400")
marco_principal2.config(bg="blue")

root.mainloop()


# marco_principal = Frame(root)
# marco_principal.pack()

# boton_1 = Button(marco_principal, text="Boton 1")
# boton_1.pack(side=LEFT)

# boton_2 = Button(marco_principal, text="Boton 2")
# boton_2.pack(side=LEFT)

# boton_3 = Button(marco_principal, text="Boton 3")
# boton_3.pack(side=LEFT)
