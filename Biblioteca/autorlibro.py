from baseorm import BaseORM

class AutorLibro(BaseORM):
    tabla = "autor_libro"

    def __init__(self):
        super().__init__()
        self.autorlibro = super().listar_todos()
        self.autorlibrocompleto = self.listar_autores_y_libros()
        
    def listar_autores_y_libros(self):
        """
        Obtiene todos los registros de la tabla autor_libro, con el nombre completo del autor y el título del libro.
        """
        consulta = """
        SELECT CONCAT(autores.nombre, ' ', autores.apellido) AS autor, 
            libros.titulo
        FROM autor_libro
        INNER JOIN autores ON autor_libro.id_autor = autores.id
        INNER JOIN libros ON autor_libro.id_libro = libros.id
        """
        return self.ejecutar_consulta(consulta, fetch=True)



