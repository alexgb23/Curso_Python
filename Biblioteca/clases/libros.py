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
    
    def filtrar_libros(self, campos, busqueda):
        """
        Busca en la tabla libros por los campos dados, incluyendo el nombre del autor y la editorial.
        :param campos: Lista de campos en los que buscar (por ejemplo, 'titulo').
        :param busqueda: Cadena de búsqueda.
        :return: Resultados de la búsqueda con libro, autor y editorial.
        """
        # Construye la parte de la consulta para los campos
        condiciones = " OR ".join([f"libros.{campo} LIKE %s" for campo in campos])
        consulta = f"""
        SELECT libros.id, libros.titulo, libros.anio, 
            CONCAT(autores.nombre, ' ', autores.apellido) AS autor, 
            editoriales.nombre AS editorial
        FROM libros
        LEFT JOIN autor_libro ON libros.id = autor_libro.id_libro
        LEFT JOIN autores ON autor_libro.id_autor = autores.id
        LEFT JOIN editoriales ON libros.id_editorial = editoriales.id
        WHERE {condiciones}
        """
        
        valores = [f'%{busqueda}%' for _ in campos]
        return self.ejecutar_consulta(consulta, valores, fetch=True)

    def filtrar_libros_por_autor(self, busqueda):
        """
        Busca libros por el nombre o apellido del autor.
        :param busqueda: Nombre o apellido del autor.
        :return: Resultados de la búsqueda.
        """
        consulta = """
        SELECT libros.id, libros.titulo, libros.anio,
            CONCAT(autores.nombre, ' ', autores.apellido) AS autor, 
            editoriales.nombre AS editorial
        FROM libros
        LEFT JOIN autor_libro ON libros.id = autor_libro.id_libro
        LEFT JOIN autores ON autor_libro.id_autor = autores.id
        JOIN editoriales ON libros.id_editorial = editoriales.id
        WHERE (autores.nombre LIKE %s OR autores.apellido LIKE %s OR autores.id = %s)
        """
        
        if isinstance(busqueda, int):
            # Si la búsqueda es un ID, se pasa como tal
            valores = (busqueda, busqueda, busqueda)  # Tres valores para la consulta
        else:
            # Si la búsqueda es un string, se busca por nombre
            valores = (f'%{busqueda}%', f'%{busqueda}%', None)  # Usar None para el ID

        return self.ejecutar_consulta(consulta, valores, fetch=True)

    
    def filtrar_libros_por_editorial(self, busqueda):
    
        """
        Busca libros según el nombre o ID de la editorial.
        :param busqueda: Nombre o ID de la editorial.
        :return: Resultados de la búsqueda.
        """
        consulta = """
        SELECT libros.id, libros.titulo, libros.anio,
            CONCAT(autores.nombre, ' ', autores.apellido) AS autor, 
            editoriales.nombre AS editorial
        FROM libros
        LEFT JOIN autor_libro ON libros.id = autor_libro.id_libro
        LEFT JOIN autores ON autor_libro.id_autor = autores.id
        JOIN editoriales ON libros.id_editorial = editoriales.id
        WHERE (editoriales.nombre LIKE %s OR editoriales.id = %s)
        """
        
        if isinstance(busqueda, int):
            # Si la búsqueda es un ID, se pasa como tal
            valores = (busqueda, busqueda)
        else:
            # Si la búsqueda es un string, se busca por nombre
            valores = (f'%{busqueda}%', busqueda)
        
        return self.ejecutar_consulta(consulta, valores, fetch=True)


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

