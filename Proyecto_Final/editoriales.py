from ORM_Base import BaseORM


class Editoriales(BaseORM):
    @property
    def tabla(self):
        return 'editoriales'

    def __init__(self):
        super().__init__()
        # Llenar la lista de libros al instanciar la clase
        self.editoriales = self.listar_todos()

    def __str__(self):
        # Representación de la instancia
        return f"Editoriales: {self.editoriales}"


# Crear una instancia de Editoriales
editorial = Editoriales()

# Imprimir la instancia
print(editorial)
