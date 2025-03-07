from clases.baseorm import BaseORM

class Libros(BaseORM):
    tabla = "libros"

    def __init__(self):
        super().__init__()
        self.libros = self.listar_todos_libros()
        self.libros_con_autor_y_editorial = self.listar_libros_con_autor_y_editorial()

    def listar_todos_libros(self):
        """Obtiene todos los libros de la base de datos."""
        return super().listar_todos()

    def listar_libros_con_autor_y_editorial(self):
        """
        Obtiene todos los registros de la tabla libros, con nombre completo del autor y el nombre de la editorial.
        """
        consulta = """
        SELECT libros.id, libros.titulo, libros.anio, 
               CONCAT(autores.nombre, ' ', autores.apellido) AS autor, 
               editoriales.nombre AS editorial
        FROM libros
        LEFT JOIN autor_libro ON libros.id = autor_libro.id_libro
        LEFT JOIN autores ON autor_libro.id_autor = autores.id
        LEFT JOIN editoriales ON libros.id_editorial = editoriales.id
        """
        return self.ejecutar_consulta(consulta, fetch=True)

    def mostrar_libros(self):
        """Imprime la lista de libros en un formato legible."""
        for libro in self.libros:
            self.imprimir_libro(libro)

    def imprimir_libro(self, libro):
        """Imprime los detalles de un libro."""
        id = libro.get('id')
        titulo = libro.get('titulo')
        id_editorial = libro.get('id_editorial')
        print(f'ID: {id}, Título: {titulo}, ID Editorial: {id_editorial}')

