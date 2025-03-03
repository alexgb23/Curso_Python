from ORM_Base import BaseORM


class Libro(BaseORM):
    @property
    def tabla(self):
        return 'libros'

    def __init__(self):
        super().__init__()
        # Llenar la lista de libros al instanciar la clase
        self.libros = self.listar_libros()

    def __str__(self):
        return f"Libros: {self.libros}"  # Representación de la instancia


# Crear una instancia de Libro
libro = Libro()

# Imprimir la instancia
print(libro)
