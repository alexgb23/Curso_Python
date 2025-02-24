from tkinter import *
from tkinter.messagebox import *

ventana = Tk()

ventana.title("Este es el titulo de la ventana principal")


def muestra_ventana():
    # showinfo("Titulo de la ventana emergente", "Esto es una ventana emergente")
    # showwarning("Titulo de la ventana emergente", "Esto es una ventana emergente")
    # showerror("Titulo de la ventana emergente", "Esto es una ventana emergente")
    askquestion(title="Pregunta",
                message="Deberia dejar de programar y salir a la calle")
    # askyesno(title="Pregunta", message="Deberia dejar de programar y salir a la calle")
    # askyesnocancel(title="Pregunta", message="Deberia dejar de programar y salir a la calle")
    # askokcancel(title="Pregunta", message="Deberia dejar de programar y salir a la calle")
    # askretrycancel(title="Pregunta", message="Deberia dejar de programar y salir a la calle")

    if askquestion == "no":
        showinfo(title="!! A seguir programando !!",
                 message="Deberia dejar de programar y salir a la calle")
    else:
        respuesta2 = askretrycancel(title="Boton Equivocado",
                                    message="Haz clic en reintentar para seguir programando")
        if respuesta2:
            showinfo(title="!! A seguir programando !!",
                     message="estupendo has elegido reintentar")
        else:
            showinfo(title="!! deja ya de programar !!",
                     message="Vete a la calle")


boton = Button(ventana, text="Mostrar ventana emergente",
               command=muestra_ventana, width=75)
boton.pack()

ventana.mainloop()
