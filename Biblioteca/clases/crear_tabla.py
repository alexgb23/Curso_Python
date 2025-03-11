from clases.baseorm import BaseORM

class Crear(BaseORM):
    tabla = None

    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla
    

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
