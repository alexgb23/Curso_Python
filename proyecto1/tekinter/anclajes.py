from tkinter import *

ventana = Tk()

titulo = Label(ventana, text="Noroeste")
titulo.pack(anchor=NW)

titulo = Label(ventana, text="Norte")
titulo.pack(anchor=N)

titulo = Label(ventana, text="Noreste")
titulo.pack(anchor=NE)

titulo = Label(ventana, text="Oeste")
titulo.pack(anchor=W)

titulo = Label(ventana, text="Centro")
titulo.pack(anchor=CENTER)

titulo = Label(ventana, text="Este")
titulo.pack(anchor=E)

titulo = Label(ventana, text="Suroeste")
titulo.pack(anchor=SW)

titulo = Label(ventana, text="Sur")
titulo.pack(anchor=S)

titulo = Label(ventana, text="Sudeste")
titulo.pack(anchor=SE)


ventana.mainloop()
