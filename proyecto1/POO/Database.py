import mysql.connector


class Database:

    def __init__(self, host, user, password, database, tabla):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.tabla = tabla
        self.conexion = self.connectar()

    def connectar(self):
        try:
            conexion = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
                # use_pure=True en algunos casos para evitar errores y conectar usando el controlador puro de Python
            )
            return conexion
        except mysql.connector.Error as err:
            print(f'Error al conectar a la base de datos: {err}')
            return None

    def ejecutar_consulta(self, consulta, valores=None, fetch=False, dictionary=True):
        if not self.conexion:
            print('No hay conexion a la base de datos')
            return None
        cursor = self.conexion.cursor(dictionary=dictionary)
        try:
            if valores:
                cursor.execute(consulta, valores)
            else:
                cursor.execute(consulta)
            if fetch:
                resultado = cursor.fetchall()
                return resultado
            else:
                self.conexion.commit()
                return cursor.lastrowid
        except mysql.connector.Error as err:
            print(f'Error al ejecutar consulta: {err}')
            return None
        finally:
            cursor.close()

    def crear_registro(self, datos):
        columnas = ','.join(datos.keys())
        valores = tuple(datos.values())
        marcadores = ','.join(['%s']*len(datos))
        consulta = f'INSERT INTO {self.tabla} ({columnas}) VALUES ({marcadores})'
        return self.ejecutar_consulta(consulta, valores)

    def listar_todos(self):
        consulta = f'SELECT * FROM {self.tabla}'
        return self.ejecutar_consulta(consulta, fetch=True)

    def buscar_por_id(self, id):
        consulta = f'SELECT * FROM {self.tabla} WHERE id=%s'
        resultado = self.ejecutar_consulta(consulta, (id,), fetch=True)
        return resultado[0] if resultado else None

    def modificar_registro(self, id, nuevos_datos):
        columnas = ", ".join([f'{col}=%s' for col in nuevos_datos.keys()])
        valores = tuple(nuevos_datos.values()) + (id,)
        consulta = f'UPDATE {self.tabla} SET {columnas} WHERE id=%s'
        return self.ejecutar_consulta(consulta, valores)

    def eliminar_registro(self, id):
        consulta = f'DELETE FROM {self.tabla} WHERE id=%s'
        return self.ejecutar_consulta(consulta, (id,))

    def cerrar_conexion(self):
        if self.conexion:
            self.conexion.close()
            print('Conexion cerrada')

