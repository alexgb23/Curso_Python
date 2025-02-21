from tkinter import *

root = Tk()

marco_principal = Frame(root)
marco_principal.grid(row=0, column=0, padx=10, pady=10)
marco_principal.config(width="150", height="150", bg="red")

marco_secundario = Frame(root)
marco_secundario.grid(row=1, column=1, padx=10, pady=10)
marco_secundario.config(width="150", height="150", bg="blue")

marco_tercero = Frame(root)
marco_tercero.grid(row=2, column=2, padx=10, pady=10)
marco_tercero.config(width="150", height="150", bg="green")

marco_cuarto = Frame(root)
marco_cuarto.grid(row=3, column=3, padx=10, pady=10)
marco_cuarto.config(width="150", height="150", bg="yellow")

marco_quinto = Frame(root)
marco_quinto.grid(row=2, column=1, padx=10, pady=10)
marco_quinto.config(width="150", height="150", bg="orange")

marco_sexto = Frame(root)
marco_sexto.grid(row=1, column=2, padx=10, pady=10)
marco_sexto.config(width="150", height="150", bg="purple")

marco_septimo = Frame(root)
marco_septimo.grid(row=0, column=3, padx=10, pady=10)
marco_septimo.config(width="150", height="150", bg="pink")

marco_octavo = Frame(root)
marco_octavo.grid(row=3, column=0, padx=10, pady=10)
marco_octavo.config(width="150", height="150", bg="brown")

boton_1 = Button(root, text="No presiones el boton",
                 bg="red", padx=100, pady=25)
boton_1.grid(row=0, column=4)


def presionar_boton():
    # Crear el Label y colocarlo en el marco_principal
    label = Label(marco_principal, text="Presionaste el boton", bg="red")
    label.pack(pady=10)  # Usa pack para que el Label se ajuste al marco


boton_2 = Button(root, text="Presiona el boton",
                 bg="green", command=presionar_boton)
boton_2.grid(row=1, column=4)

root.mainloop()
