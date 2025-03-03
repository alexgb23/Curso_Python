from abc import ABC, abstractmethod
from DataBase import Database


class BaseORM(ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    def __init__(self):
        self.conexion = Database(tabla=self.tabla).conectar()
        self.exept = Database(tabla=self.tabla).exepcion

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
        except self.exept as err:
            print(f"Error en la consulta: {err}")
            return None
        finally:
            cursor.close()
            self.conexion.close()

    def crear_registro(self, datos):
        """
        Inserta un nuevo registro en la tabla.
        datos: Diccionario con los valores a insertar. Ejemplo:
        {"nombre": "Juan Pérez", "edad": 30, "email": "juan@email.com"}
        """
        columnas = ", ".join(datos.keys())
        valores = tuple(datos.values())
        marcadores = ", ".join(["%s"] * len(datos))

        consulta = f"INSERT INTO {self.tabla} ({columnas}) VALUES ({marcadores})"
        return self.ejecutar_consulta(consulta, valores)

    def listar_todos(self):
        """
        Obtiene todos los registros de la tabla.
        """
        consulta = f"SELECT * FROM {self.tabla}"
        return self.ejecutar_consulta(consulta, fetch=True)

    def buscar_por_id(self, id):
        """
        Busca un registro por ID.
        """
        consulta = f"SELECT * FROM {self.tabla} WHERE id = %s"
        resultado = self.ejecutar_consulta(consulta, (id,), fetch=True)

        return resultado[0] if resultado else None

    def modificar_registro(self, id, nuevos_datos):
        """
        Modifica un registro existente.
        nuevos_datos: Diccionario con los valores a actualizar. Ejemplo:
        {"nombre": "Nuevo Nombre", "edad": 35}
        """
        columnas = ", ".join([f"{col} = %s" for col in nuevos_datos.keys()])
        valores = tuple(nuevos_datos.values()) + (id,)

        consulta = f"UPDATE {self.tabla} SET {columnas} WHERE id = %s"
        return self.ejecutar_consulta(consulta, valores)

    def eliminar_registro(self, id):
        """
        Elimina un registro por ID.
        """
        consulta = f"DELETE FROM {self.tabla} WHERE id = %s"
        return self.ejecutar_consulta(consulta, (id,))

    def cerrar_conexion(self):
        """
        Cierra la conexión con la base de datos.
        """
        if self.conexion:
            self.conexion.close()
            print("Conexión cerrada.")
