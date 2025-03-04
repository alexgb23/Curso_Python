from clases.baseorm import BaseORM


class Autores(BaseORM):
    tabla = "autores"

    def __init__(self):
        super().__init__()
        self.autores = super().listar_todos()


    def listar_autores(self):
        for autor in self.autores:
            id = autor.get('id')
            nombre = autor.get('nombre')
            apellido = autor.get('apellido')
            print(f'ID: {id}, Nombre: {nombre}, Apellido: {apellido}',)
