import mysql.connector
from config_manager import ConfigManager

class Database:
    
    def __init__(self, tabla):
        self.config = ConfigManager().get_database_config()
        self.tabla = tabla
        self.conexion = self.conectar()
    
    def conectar(self):
        """
        Crea la conexión a MySQL.
        """
        try:
            conexion = mysql.connector.connect(**self.config)
            return conexion
        except mysql.connector.Error as err:
            print(f"Error de conexión: {err}")
            return None

    def ejecutar_consulta(self, consulta, valores=None, fetch=False, dictionary=True):
        """
        Ejecuta una consulta SQL genérica.
        """
        if not self.conexion:
            print("No hay conexión a la base de datos.")
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
                return cursor.lastrowid  # Retorna el ID del último registro insertado
        except mysql.connector.Error as err:
            print(f"Error en la consulta: {err}")
            return None
        finally:
            cursor.close()

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
    