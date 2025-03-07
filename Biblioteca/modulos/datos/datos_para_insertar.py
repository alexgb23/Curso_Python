def datos_llenar_insertar(self, tipo_panel):
    insertar_libro="titulo","año","autor", "editorial"
    insertar_editorial="nombre", "direccion", "telefono"
    insertar_autor="nombre", "apellido", "nacionalidad"
    cambio_autor_libro="libro", "autor"
    if tipo_panel == "Libros":
        return insertar_libro
    elif tipo_panel == "Editoriales":
        return insertar_editorial
    elif tipo_panel == "Autores":
        return insertar_autor
    else:
        return cambio_autor_libro