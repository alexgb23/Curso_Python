from ORM_Base import BaseORM


class Autores(BaseORM):
    @property
    def tabla(self):
        return 'autores'

    def __init__(self):
        super().__init__()
        # Llenar la lista de libros al instanciar la clase
        self.autores = self.listar_todos()

    def __str__(self):
        return f"Autores: {self.autores}"  # Representación de la instancia


# Crear una instancia de autores
autores = Autores()

# Imprimir la instancia
print(autores)
