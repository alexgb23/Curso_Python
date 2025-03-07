from clases.baseorm import BaseORM

class Autores(BaseORM):
    tabla = "autores"

    def __init__(self):
        super().__init__()
        self.autores = self.listar_todos_autores()

    def listar_todos_autores(self):
        """Lista todos los autores desde la base de datos."""
        return super().listar_todos()

    def mostrar_autores(self):
        """Imprime la lista de autores en un formato legible."""
        for autor in self.autores:
            self.imprimir_autor(autor)

    def imprimir_autor(self, autor):
        """Imprime los detalles de un autor."""
        id = autor.get('id')
        nombre = autor.get('nombre')
        apellido = autor.get('apellido')
        print(f'ID: {id}, Nombre: {nombre}, Apellido: {apellido}')
