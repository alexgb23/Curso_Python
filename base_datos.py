"""
Conexcion a base de datos
"""

# from mysql import connector as _mysql_connector

import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "passwd": "root",
    "database": "app"
}


"""
para el primer import se debe instalar el paquete mysql-connector-python
pip install mysql-connector-python
"""


def conectar():
    try:
        conexion = mysql.connector.connect(**config)
        return conexion
    except mysql.connector.Error as err:
        print(f'Error al conectar a la base de datos: {err}')
        return None


prueba = conectar()
if prueba:
    print('Conectado a la base de datos')
else:
    print('Error al conectar a la base de datos')


def leer_usuarios():
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as err:
            print(f'Error al leer usuarios: {err}')
        finally:
            cursor.close()
            db.close()


def leer_usuario(id):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            cursor.execute(f'SELECT * FROM usuarios WHERE id={id}')
            usuario = cursor.fetchone()
            return usuario
        except mysql.connector.Error as err:
            print(f'Error al leer usuario: {err}')
        finally:
            cursor.close()
            db.close()


def crear_usuario(nombre, edad, email):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "INSERT INTO usuarios (nombre, edad, email) VALUES (%s, %s, %s)"
            cursor.execute(sql, (nombre, edad, email))
            db.commit()
            print('Usuario creado correctamente')
        except mysql.connector.Error as err:
            print(f'Error al crear usuario: {err}')
        finally:
            cursor.close()
            db.close()


def actualizar_usuario(id, nombre, email):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "UPDATE usuarios SET nombre=%s, email=%s WHERE id=%s"
            cursor.execute(sql, (nombre, email, id))
            db.commit()
            print('Usuario actualizado correctamente')
        except mysql.connector.Error as err:
            print(f'Error al actualizar usuario: {err}')
        finally:
            cursor.close()
            db.close()


def eliminar_usuario(id):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "DELETE FROM usuarios WHERE id=%s"
            cursor.execute(sql, (id,))
            db.commit()
            print('Usuario eliminado correctamente')
        except mysql.connector.Error as err:
            print(f'Error al eliminar usuario: {err}')
        finally:
            cursor.close()
            db.close()


def buscar_usuarios(nombre):
    db = conectar()
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE nombre LIKE "%{nombre}%"')
    usuarios = cursor.fetchall()
    db.close()
    return usuarios


def buscar_usuario(id):
    db = conectar()
    cursor = db.cursor()
    cursor.execute(f'SELECT * FROM usuarios WHERE id={id}')
    usuario = cursor.fetchone()
    db.close()
    return usuario


print(leer_usuarios())
# crear_usuario('Pedro', 28, 'pedN@example.com')
