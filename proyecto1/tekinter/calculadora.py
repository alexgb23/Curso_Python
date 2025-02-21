from tkinter import *

# Función para agregar números y operadores al campo de entrada


def agregar_a_entrada(valor):
    entrada.insert(END, valor)

# Función para calcular el resultado


def calcular():
    try:
        resultado = eval(entrada.get())  # Evalúa la expresión en el Entry
        entrada.delete(0, END)  # Limpia el Entry
        entrada.insert(END, str(resultado))  # Muestra el resultado
    except Exception:
        entrada.delete(0, END)
        entrada.insert(END, "Error")  # Muestra error si hay una excepción

# Función para limpiar el campo de entrada


def limpiar():
    entrada.delete(0, END)


root = Tk()
root.title("Calculadora")

# Campo de entrada
entrada = Entry(root, width=16, font=('Arial', 24),
                borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Estilo de botones
button_style = {
    'font': ('Arial', 18),
    'padx': 14,
    'pady': 14,
    'bg': '#f0f0f0',
    'activebackground': '#d0d0d0'
}

# Botones numéricos
for i in range(3):
    for j in range(3):
        boton = Button(root, text=str(i * 3 + j + 1), command=lambda x=i *
                       3 + j + 1: agregar_a_entrada(x), **button_style)
        boton.grid(row=i + 1, column=j, padx=5, pady=5)

# Botón 0
boton_0 = Button(
    root, text="0", command=lambda: agregar_a_entrada(0), **button_style)
boton_0.grid(row=4, column=1, padx=5, pady=5)

# Botones de operaciones
boton_suma = Button(
    root, text="+", command=lambda: agregar_a_entrada("+"), **button_style)
boton_suma.grid(row=1, column=3, padx=5, pady=5)

boton_resta = Button(
    root, text="-", command=lambda: agregar_a_entrada("-"), **button_style)
boton_resta.grid(row=2, column=3, padx=5, pady=5)

boton_multiplicacion = Button(
    root, text="*", command=lambda: agregar_a_entrada("*"), **button_style)
boton_multiplicacion.grid(row=3, column=3, padx=5, pady=5)

boton_division = Button(
    root, text="/", command=lambda: agregar_a_entrada("/"), **button_style)
boton_division.grid(row=4, column=3, padx=5, pady=5)

# Botón de igual
boton_igual = Button(root, text="=", command=calcular, **button_style)
boton_igual.grid(row=4, column=2, padx=5, pady=5)

# Botón de limpiar
boton_limpiar = Button(root, text="C", command=limpiar, **button_style)
boton_limpiar.grid(row=4, column=0, padx=5, pady=5)

root.mainloop()
