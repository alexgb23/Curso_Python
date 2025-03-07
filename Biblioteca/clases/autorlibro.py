from clases.baseorm import BaseORM

class AutorLibro(BaseORM):
    tabla = "autor_libro"

    def __init__(self):
        super().__init__()
        self.autor_libros = self.listar_autores_y_libros()

    def listar_autores_y_libros(self):
        """
        Obtiene todos los registros de la tabla autor_libro, con el nombre completo del autor y el título del libro.
        """
        consulta = """
        SELECT CONCAT(autores.nombre, ' ', autores.apellido) AS autor, 
               libros.titulo AS libro
        FROM autor_libro
        LEFT JOIN autores ON autor_libro.id_autor = autores.id
        LEFT JOIN libros ON autor_libro.id_libro = libros.id
        """
        return self.ejecutar_consulta(consulta, fetch=True)

    def mostrar_autor_libros(self):
        """Imprime la lista de autores y sus libros en un formato legible."""
        for autor_libro in self.autor_libros:
            self.imprimir_autor_libro(autor_libro)

    def imprimir_autor_libro(self, autor_libro):
        """Imprime los detalles de un autor y su libro."""
        autor = autor_libro.get('autor')
        libro = autor_libro.get('libro')
        print(f'Autor: {autor}, Libro: {libro}')
