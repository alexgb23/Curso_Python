from tkinter import *

ventana = Tk()


def actualiza(value):
    option_set.config(text=value)


titulo = Label(ventana, text="Selecciona una opcion")
titulo.pack()

opciones = [
    ["Color rojo", "rojo"],
    ["Color azul", "azul"],
    ["Color verde", "verde"],
    ["Color amarillo", "amarillo"]
]

colores = StringVar()
colores.set("rojo")

for opcion, valor in opciones:
    Radiobutton(ventana, text=opcion, variable=colores, value=valor).pack()

boton = Button(ventana, text="Enviar",
               command=lambda: actualiza(colores.get()))

boton.pack()

option_set = Label(ventana, text=colores.get())
option_set.pack()

ventana.mainloop()
