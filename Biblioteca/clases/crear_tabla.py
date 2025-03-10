from clases.baseorm import BaseORM

class Crear(BaseORM):
    tabla = None

    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla
    

