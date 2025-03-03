from tkinter import *
import mysql.connector


root = Tk()
root.title("Ventana principal")
root.geometry("400x400")

try:
    conexion = mysql.connector.connect(
        user="root",
        password="root",
        host="localhost",
        port=3306,
        database="prueba"
    )
    cursor = conexion.cursor()

    Label(root, text="Conexión exitosa a " +
          str(conexion.database + ".")).pack()
except mysql.connector.Error as e:
    print(f"Error al conectar a la base de datos: {e}").pack()


def crear_tabla():
    try:
        cursor.execute("""CREATE TABLE IF NOT EXISTS clientes (
                   id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
                   nombre VARCHAR(32) NOT NULL,
                   apellido VARCHAR(64) NOT NULL,
                   telefono VARCHAR(9) NOT NULL,
                   direccion VARCHAR(256) NOT NULL
                 )""")

        conexion.commit()
    except mysql.connector.Error as e:
        print(f"Error al crear la tabla: {e}")


def registrar_cliente():
    nombre = e_nombre.get()
    apellido = e_apellido.get()
    telefono = e_telefono.get()
    direccion = e_direccion.get()

    e_nombre.delete(0, END)
    e_apellido.delete(0, END)
    e_telefono.delete(0, END)
    e_direccion.delete(0, END)

    try:
        cursor.execute("INSERT INTO clientes (nombre, apellido, telefono, direccion) VALUES (%s, %s, %s, %s)",
                       (nombre, apellido, telefono, direccion))
        conexion.commit()
    except mysql.connector.Error as e:
        print(f"Error al registrar el cliente: {e}")


Label(root, text="Registro de clientes").pack()

Label(root, text="Nombre").pack()
e_nombre = Entry(root)
e_nombre.pack()

Label(root, text="Apellido").pack()
e_apellido = Entry(root)
e_apellido.pack()

Label(root, text="Telefono").pack()
e_telefono = Entry(root)
e_telefono.pack()

Label(root, text="Direccion").pack()
e_direccion = Entry(root)
e_direccion.pack()

boton = Button(root, text="Registrar", command=registrar_cliente)
boton.pack()

boton = Button(root, text="Crear tabla", command=crear_tabla)
boton.pack()

mainloop()
