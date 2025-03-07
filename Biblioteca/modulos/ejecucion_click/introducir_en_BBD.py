from tkinter import messagebox
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
from clases.autorlibro import AutorLibro


def acciones_botones_sub_panel(self, tabla, boton):
    if boton['text'] == "Actualizar":
        if tabla == "Libros":
            nuevos_datos = {}
            id = self.campos_actualizar["id"].get()
            titulo = self.campos_actualizar["titulo"].get()
            anio = self.campos_actualizar["anio"].get()           
            campos_a_buscar = ['nombre']  # Reemplaza con los campos reales de tu tabla
            cadena_busqueda = self.campos_actualizar["editorial"].get()  
            edit = Editoriales()
            resul = edit.filtrar(campos_a_buscar, cadena_busqueda)
            id_editorial = resul[0]['id']

                    # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['titulo'] = titulo
            nuevos_datos['anio'] = anio
            nuevos_datos['id_editorial'] = id_editorial
            
            libro_actualizar = Libros()
            resultado=libro_actualizar.modificar_registro(id, nuevos_datos)

            if resultado is not None:
                messagebox.showinfo("Informacion","Libro actualizado correctamente")
            else:
                messagebox.showerror("Error","Error al actualizar el libro")

            return
        
        elif tabla == "Autores":
            nuevos_datos = {}
            id = self.campos_actualizar["id"].get()
            nombre = self.campos_actualizar["nombre"].get()
            apellido = self.campos_actualizar["apellido"].get()
            nacionalidad = self.campos_actualizar["nacionalidad"].get()

            # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['nombre'] = nombre
            nuevos_datos['apellido'] = apellido
            nuevos_datos['nacionalidad'] = nacionalidad

            autores= Autores()
            resultado=autores.modificar_registro(id, nuevos_datos)

            if resultado is not None:
                messagebox.showinfo("Informacion", "Autor actualizado correctamente")
            else:
                messagebox.showerror("Error" ,"Error al actualizar el Autor")

            return

        elif tabla == "Editoriales":
            nuevos_datos = {}
            id = self.campos_actualizar["id"].get()
            nombre = self.campos_actualizar["nombre"].get()
            direccion = self.campos_actualizar["direccion"].get()
            telefono = self.campos_actualizar["telefono"].get()

            # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['nombre'] = nombre
            nuevos_datos['direccion'] = direccion
            nuevos_datos['telefono'] = telefono

            editoriales = Editoriales()
            resultado=editoriales.modificar_registro(id, nuevos_datos)

            if resultado is not None:
                messagebox.showinfo("Informacion","Editorial actualizada correctamente")
            else:
                messagebox.showerror("Error","Error al actualizar la Editorial")

            return

        elif tabla == "Autor-Libro":
            nuevos_datos = {}

            return
        
    if boton['text'] == "Insertar":
        if tabla == "Libros":
            nuevos_datos = {}
            titulo = self.campos_insertar["titulo"].get()
            anio = self.campos_insertar["año"].get()           
            campos_a_buscar = ['nombre']  # Reemplaza con los campos reales de tu tabla
            cadena_busqueda = self.campos_insertar["editorial"].get()  
            edit = Editoriales()
            resul = edit.filtrar(campos_a_buscar, cadena_busqueda)
            id_editorial = resul[0]['id']

            # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['titulo'] = titulo
            nuevos_datos['anio'] = anio
            nuevos_datos['id_editorial'] = id_editorial
            
            nuevo_libro = Libros()
            resultado=nuevo_libro.crear_registro(nuevos_datos)

            if resultado is not None:
                messagebox.showinfo("Informacion", f"Libro creado correctamente con id: {resultado}")
            else:
                messagebox.showerror("Error","Error al crear el libro")

            return

        elif tabla == "Autores":
            nuevos_datos = {}
            nombre = self.campos_insertar["nombre"].get()
            apellido = self.campos_insertar["apellido"].get()
            nacionalidad = self.campos_insertar["nacionalidad"].get()

            # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['nombre'] = nombre
            nuevos_datos['apellido'] = apellido
            nuevos_datos['nacionalidad'] = nacionalidad

            nuevo_autor = Autores()
            resultado=nuevo_autor.crear_registro(nuevos_datos)

            if resultado is not None:
                messagebox.showinfo("Informacion", f"Autor creado correctamente con id: {resultado}")
            else:
                messagebox.showerror("Error", "Error al crear el autor")

            return
            
        elif tabla == "Editoriales":
            nuevos_datos = {}
            nombre = self.campos_insertar["nombre"].get()
            ciudad = self.campos_insertar["direccion"].get()
            pais = self.campos_insertar["telefono"].get()

            # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['nombre'] = nombre
            nuevos_datos['direccion'] = ciudad
            nuevos_datos['telefono'] = pais

            nueva_editorial = Editoriales()
            resultado=nueva_editorial.crear_registro(nuevos_datos)

            if resultado is not None:
                messagebox.showinfo("Informacion", f"Editorial creada correctamente con id: {resultado}")
            else:
                messagebox.showerror("Error", "Error al crear la editorial")

            return

        elif tabla == "Autor-Libro":
            nuevos_datos = {}

            return

  