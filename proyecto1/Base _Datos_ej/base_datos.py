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
            cursor = db.cursor(dictionary=True)
            cursor.execute('SELECT * FROM usuarios')
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as err:
            print(f'Error al leer usuarios: {err}')
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
            nuevo_id = cursor.lastrowid
            return nuevo_id
        except mysql.connector.Error as err:
            print(f'Error al crear usuario: {err}')
        finally:
            cursor.close()
            db.close()


def actualizar_usuario(id, nombre, edad, email):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "UPDATE usuarios SET nombre=%s, edad=%s, email=%s WHERE id=%s"
            cursor.execute(sql, (nombre, edad, email, id))
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


def buscar_usuarios_nombre(nombre):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM usuarios WHERE nombre LIKE %s"
            cursor.execute(sql, (f"%{nombre}%",))
            usuarios = cursor.fetchall()
            return usuarios
        except mysql.connector.Error as err:
            print(f'Error al buscar usuarios: {err}')
        finally:
            cursor.close()
            db.close()


def buscar_usuarios_id(id):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM usuarios WHERE id=%s"
            cursor.execute(sql, (id,))
            usuario = cursor.fetchone()
            return usuario
        except mysql.connector.Error as err:
            print(f'Error al buscar usuario: {err}')
        finally:
            cursor.close()
            db.close()


def buscar_usuarios_email(email):
    db = conectar()
    if db:
        try:
            cursor = db.cursor()
            sql = "SELECT * FROM usuarios WHERE email=%s"
            cursor.execute(sql, (email,))
            usuario = cursor.fetchone()
            return usuario
        except mysql.connector.Error as err:
            print(f'Error al buscar usuario: {err}')
        finally:
            cursor.close()
            db.close()


# for i, user in enumerate(leer_usuarios()):
#     print(f'{i+1}: {user}')

# print(buscar_usuarios_nombre('a'))

# nuevo_usuario_id = crear_usuario('Manuel', 28, 'manu_el@example.com')
# print(f'Nuevo usuario creado con id: {nuevo_usuario_id}')


def menu():
    while True:
        print("\nMenu de opciones del Crud de Usuarios")
        print('1. Leer usuarios')
        print('2. Crear usuario')
        print('3. Actualizar usuario')
        print('4. Eliminar usuario')
        print('5. Buscar usuario por nombre')
        print('6. Buscar usuario por ID')
        print('7. Buscar usuario por email')
        print('8. Salir')
        opcion = int(input('Ingrese una opcion: '))
        if opcion == 1:
            for i, user in enumerate(leer_usuarios()):
                print(f'{i+1}: {user}')
                continue
        if opcion == 2:
            nombre = input('Ingrese el nombre del usuario: ')
            edad = int(input('Ingrese la edad del usuario: '))
            email = input('Ingrese el email del usuario: ')
            crear_usuario(nombre, edad, email)
        elif opcion == 3:
            id = int(input('Ingrese el ID del usuario a actualizar: '))
            nombre = input('Ingrese el nombre del usuario: ')
            edad = int(input('Ingrese la edad del usuario: '))
            email = input('Ingrese el email del usuario: ')
            actualizar_usuario(id, nombre, edad, email)
        elif opcion == 4:
            id = int(input('Ingrese el ID del usuario: '))
            eliminar_usuario(id)
        elif opcion == 5:
            nombre = input('Ingrese el nombre del usuario: ')
            print(buscar_usuarios_nombre(nombre))
        elif opcion == 6:
            id = int(input('Ingrese el ID del usuario: '))
            print(buscar_usuarios_id(id))
        elif opcion == 7:
            email = input('Ingrese el email del usuario: ')
            print(buscar_usuarios_email(email))
        elif opcion == 8:
            break
        else:
            print('Opcion no valida, intente de nuevo')


if __name__ == '__main__':
    menu()
