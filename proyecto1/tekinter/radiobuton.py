from tkinter import *

ventana = Tk()

x = IntVar()
# seleccionar la primera opcion
x.set(1)

option_set = Label(ventana, text=x.get())
option_set.grid(row=5)


def click_select():
    option_set = Label(ventana, text=x.get())
    option_set.grid(row=5)


opcion1 = Radiobutton(ventana, text="Opcion 1",
                      variable=x, value=1,)
opcion1.grid(row=1)
opcion2 = Radiobutton(ventana, text="Opcion 2",
                      variable=x, value=2,)
opcion2.grid(row=2)
opcion3 = Radiobutton(ventana, text="Opcion 3",
                      variable=x, value=3,)
opcion3.grid(row=3)

boton = Button(ventana, text="Seleccionar", command=click_select)
boton.grid(row=4)

ventana.mainloop()
