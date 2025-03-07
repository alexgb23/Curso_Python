def datos_llenar_insertar(self, tipo_panel):
    """Devuelve los campos a llenar según el tipo de panel especificado."""
    campos = {
        "Libros": ("titulo", "año", "autor", "editorial"),
        "Editoriales": ("nombre", "direccion", "telefono"),
        "Autores": ("nombre", "apellido", "nacionalidad"),
        "CambioAutorLibro": ("libro", "autor")
    }

    return campos.get(tipo_panel, campos["CambioAutorLibro"])
