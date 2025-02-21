from tkinter import *

root = Tk()

# for i in range(3):
#     for j in range(3):
#         Button(root, text=f"Boton {i}{j}").grid(row=i, column=j)

etiqueta = Label(root, text="Esta es la primera etiqueta")
etiqueta2 = Label(root, text="Esta es la segunda etiqueta")
etiqueta.grid(row=0, column=1)
etiqueta2.grid(row=0, column=0)

marco_principal = Frame()
marco_principal.grid(row=1, column=0)
marco_principal.config(width="800", height="600", bg="red")

root.mainloop()
