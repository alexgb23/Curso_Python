from abc import ABC, abstractmethod
from clases.DataBase import Database

class BaseORM (ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    def __init__(self):
          self.ejecutar_consulta = Database(self.tabla).ejecutar_consulta
       
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


    def filtrar(self, campos, busqueda):
        """
        Busca en la tabla especificada por los campos dados.
        :param tabla: Nombre de la tabla a buscar.
        :param campos: Lista de campos en los que buscar.
        :param busqueda: Cadena de búsqueda.
        :return: Resultados de la búsqueda.
        """
        # Construye la parte de la consulta para los campos
        condiciones = " OR ".join([f"{campo} LIKE %s" for campo in campos])
        consulta = f"SELECT * FROM {self.tabla} WHERE {condiciones}"
        valores = [f'%{busqueda}%' for _ in campos]
        return self.ejecutar_consulta(consulta, valores, fetch=True)
    
    def crear_tabla(self, columnas):
        """
        Crea una nueva tabla en la base de datos si no existe.

        :param columnas: Diccionario con el nombre de la columna como clave y el tipo de dato como valor.
        """
        columnas_sql = ", ".join([f"{nombre} {tipo}" for nombre, tipo in columnas.items()])
        consulta = f"CREATE TABLE IF NOT EXISTS {self.tabla} ({columnas_sql});"
        
        # Usar el método ejecutar_consulta de la clase Database
        resultado = self.ejecutar_consulta(consulta)
        
        if resultado is not None:
            print(f"Tabla '{self.tabla}' creada exitosamente o ya existe.")
        else:
            print(f"Error al crear la tabla '{self.tabla}'.")
