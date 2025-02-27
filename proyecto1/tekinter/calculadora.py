from tkinter import *
import math

# Función para agregar números y operadores al campo de entrada


def agregar_a_entrada(valor):
    entrada.insert(END, valor)


# Función para calcular el resultado

def convertir_negativo():
    entrada_texto = entrada.get()  # Obtiene el texto actual en la entrada
    if entrada_texto:  # Verifica que no esté vacío
        # Busca el último número en la cadena
        partes = entrada_texto.split()  # Divide por espacios (si hay)
        ultimo_numero = partes[-1]  # Toma el último número
        # Verifica si el último número ya es negativo
        if ultimo_numero.startswith("-"):
            # Si ya es negativo, lo convierte a positivo
            nuevo_numero = ultimo_numero[1:]  # Elimina el signo negativo
        else:
            # Si no es negativo, lo convierte a negativo
            nuevo_numero = "-" + ultimo_numero  # Agrega el signo negativo

        # Reemplaza el último número en la entrada
        partes[-1] = nuevo_numero  # Actualiza el último número
        nueva_entrada = " ".join(partes)  # Une las partes de nuevo
        entrada.delete(0, END)  # Limpia el Entry
        entrada.insert(END, nueva_entrada)  # Muestra la nueva entrada


def calcular():
    try:
        resultado = eval(entrada.get())  # Evalúa la expresión en el Entry
        entrada.delete(0, END)  # Limpia el Entry
        entrada.insert(END, str(resultado))  # Muestra el resultado
    except Exception:
        entrada.delete(0, END)
        entrada.insert(END, "Error")  # Muestra error si hay una excepción


def calculo_cientifico(operacion):
    try:
        if operacion == "math.log(" or operacion == "math.exp(" or operacion == "1/(":
            # Evalúa la expresión en el Entry
            resultado = eval(operacion+entrada.get()+")")
            entrada.delete(0, END)  # Limpia el Entry
            entrada.insert(END, str(resultado))  # Muestra el resultado
        else:
            resultado = eval(operacion+entrada.get()+"))")
            entrada.delete(0, END)  # Limpia el Entry
            entrada.insert(END, str(resultado))  # Muestra el resultado
            print(operacion+entrada.get()+")")
    except Exception:
        entrada.delete(0, END)
        entrada.insert(END, "Error")  # Muestra error si hay una excepción

# Función para limpiar el campo de entrada


def limpiar():
    entrada.delete(0, END)


def limpiar_ulitmo():
    entrada.delete(len(entrada.get())-1, END)


root = Tk()
root.title("Calculadora Científica")

# Campo de entrada
entrada = Entry(root, width=24, font=('Arial', 24),
                borderwidth=2, relief="solid")
entrada.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Estilo de botones
button_style = {
    'font': ('Arial', 15),
    'padx': 10,
    'pady': 10,
    'bg': '#f0f0f0',
    'activebackground': '#d0d0d0'
}

# Botones numéricos
for i in range(3):
    for j in range(3):
        boton = Button(root, text=str(i * 3 + j + 1), command=lambda x=i *
                       3 + j + 1: agregar_a_entrada(x), **button_style)
        boton.grid(row=i + 4, column=j, padx=10, pady=10, sticky="nsew")
        print(i+1, j)

# Botón Porciento
boton_porciento = Button(
    root, text="%", command=lambda: agregar_a_entrada("/100"), **button_style)
boton_porciento.grid(row=1, column=0, padx=5, pady=5)


boton_raiz = Button(
    root, text="√", command=lambda: agregar_a_entrada("**0.5"), **button_style)
boton_raiz.grid(row=1, column=1, padx=5, pady=5)

# Botón eliminar
boton_borrar = Button(
    root, text="<-", command=limpiar_ulitmo, **button_style)
boton_borrar.grid(row=1, column=3, padx=5, pady=5)

boton_seno = Button(
    root, text="sin", command=lambda: calculo_cientifico("math.sin(math.radians("), **button_style)
boton_seno.grid(row=2, column=0, padx=5, pady=5)

boton_coseno = Button(
    root, text="cos", command=lambda: calculo_cientifico("math.cos(math.radians("), **button_style)
boton_coseno.grid(row=2, column=1, padx=5, pady=5)

boton_tangente = Button(
    root, text="tan", command=lambda: calculo_cientifico("math.tan(math.radians("), **button_style)
boton_tangente.grid(row=2, column=2, padx=5, pady=5)

boton_fracciones = Button(
    root, text="1/x", command=lambda: calculo_cientifico("1/("), **button_style)
boton_fracciones.grid(row=2, column=3, padx=5, pady=5)

boton_logaritmo = Button(
    root, text="log", command=lambda: calculo_cientifico("math.log("), **button_style)
boton_logaritmo.grid(row=3, column=0, padx=5, pady=5)

boton_exponencial = Button(
    root, text="exp", command=lambda: calculo_cientifico("math.exp("), **button_style)
boton_exponencial.grid(row=3, column=1, padx=5, pady=5)

boton_mod = Button(
    root, text="mod", command=lambda: agregar_a_entrada("%"), **button_style)
boton_mod.grid(row=3, column=2, padx=5, pady=5)


boton_pos_neg = Button(
    root, text="+/-", command=convertir_negativo, **button_style)
boton_pos_neg.grid(row=7, column=0, padx=5, pady=5)
# Botón 0
boton_0 = Button(
    root, text="0", command=lambda: agregar_a_entrada(0), **button_style)
boton_0.grid(row=7, column=1, padx=5, pady=5)

boton_coma = Button(
    root, text=",", command=lambda: agregar_a_entrada("."), **button_style)
boton_coma.grid(row=7, column=2, padx=5, pady=5)

# Botones de operaciones básicas
boton_suma = Button(
    root, text="+", command=lambda: agregar_a_entrada("+"), **button_style)
boton_suma.grid(row=6, column=3, padx=5, pady=5)

boton_resta = Button(
    root, text="-", command=lambda: agregar_a_entrada("-"), **button_style)
boton_resta.grid(row=5, column=3, padx=5, pady=5)

boton_multiplicacion = Button(
    root, text="*", command=lambda: agregar_a_entrada("*"), **button_style)
boton_multiplicacion.grid(row=4, column=3, padx=5, pady=5)

boton_division = Button(
    root, text="/", command=lambda: agregar_a_entrada("/"), **button_style)
boton_division.grid(row=3, column=3, padx=5, pady=5)

# Botones de operaciones científicas


# Botón de igual
boton_igual = Button(root, text="=", command=calcular, **button_style)
boton_igual.grid(row=7, column=3, padx=5, pady=5)

# Botón de limpiar
boton_limpiar = Button(root, text="CE", command=limpiar, **button_style)
boton_limpiar.grid(row=1, column=2, padx=5, pady=5)

root.mainloop()
