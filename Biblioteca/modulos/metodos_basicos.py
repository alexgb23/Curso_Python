import tkinter as tk
from tkinter import ttk
from panel_Principal.form_maestro_design import *
from tkinter import messagebox
import modulos.botones.btn_selected as btn_selected
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
from clases.autorlibro import AutorLibro
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
import modulos.efectos_visuales.transisiones as transition



def instanciar_y_marcar(self, boton, btn_info):
    # Llama a los métodos deseados
    btn_selected.marcar_boton(self, boton, btn_info)  # Marca el botón
    instanciar(self, btn_info["text"])   # Llama a instanciar


    
def acciones(self, buton, btn_info_sup):
    btn_selected.marcar_boton(self, buton, btn_info_sup, True)

    # Manejo de acciones según el texto del botón
    accion_texto = btn_info_sup["text"]

    if accion_texto == "Buscar":
        pass
    elif accion_texto == "Actualizar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib":  
            messagebox.showinfo(
                "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        # Verificar si hay una fila seleccionada antes de procesar otras acciones
        if not self.campo_selected_table:
            messagebox.showinfo(
            "Error", "Seleccione una fila en la tabla para actualizar")
            return  # Salir de la función si no hay selección
        self.transicion_paneles_if_true() 
        self.creacion_acciones_cuerpo_datos("Actualizar")
        transition.slide_in(self, self.panel_acciones_cuerpo)
    elif accion_texto == "Insertar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib": 
            messagebox.showinfo(
            "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        self.transicion_paneles_if_true()      
        self.creacion_acciones_cuerpo_datos("Insertar")
        transition.slide_in(self, self.panel_acciones_cuerpo)
    elif accion_texto == "Eliminar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib": 
            messagebox.showinfo(
                "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        # Verificar si hay una fila seleccionada antes de procesar otras acciones
        if not self.campo_selected_table:
            messagebox.showinfo(
            "Error", "Seleccione una fila en la tabla para actualizar")
            return  # Salir de la función si no hay selección
        eliminar_registro(self)
        

def eliminar_registro(self):
    if self.titulo_panel_administracion == "Libros":
        libro_eliminado = Libros()
        respuesta= libro_eliminado.eliminar_registro(self.campo_selected_table["id"])
        if respuesta is not None:
            messagebox.showinfo("Informacion","Libro eliminado correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar el libro")

    elif self.titulo_panel_administracion == "Editoriales":
        editorial_eliminada = Editoriales()
        espuesta= editorial_eliminada.eliminar_registro(self.campo_selected_table["id"])
        if espuesta is not None:
            messagebox.showinfo("Informacion","Editorial eliminada correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar la editorial")

    elif self.titulo_panel_administracion == "Autores":
        autor_eliminado = Autores()
        respuesta= autor_eliminado.eliminar_registro(self.campo_selected_table["id"])
        if respuesta is not None:
            messagebox.showinfo("Informacion","Autor eliminado correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar el autor")
    else:
        AutorLibro = AutorLibro()
        respuesta= AutorLibro.eliminar_registro(self.campo_selected_table["id"])
        if respuesta is not None:
            messagebox.showinfo("Informacion","AutorLibro eliminado correctamente")
        else:
            messagebox.showerror("Error","Error al eliminar el AutorLibro")
        

    # def toggle(self, ventana):
    #     if self.ventanas.get(ventana) is None:
    #         # Guardar información detallada
    #         self.ventanas[ventana] = self.get_window_details(ventana)

    #     if self.visible:
    #         self.slide_out(ventana)
    #     else:
    #         self.slide_in(ventana)




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
            nuevos_datos['ciudad'] = direccion
            nuevos_datos['pais'] = telefono

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
            ciudad = self.campos_insertar["ciudad"].get()
            pais = self.campos_insertar["pais"].get()

            # Asignar los datos al diccionario, excluyendo el ID
            nuevos_datos['nombre'] = nombre
            nuevos_datos['ciudad'] = ciudad
            nuevos_datos['pais'] = pais

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

  
            


def instanciar(self, clase):
    btn_selected.reset_btn_sup(self)
    self.campo_selected_table = {}
    if clase == "Libros":
        try:
            self.registros = None
            libros = Libros()
            self.registros = libros.libros_con_autor_y_editorial
            self.indice_actual = 0
            self.titulo_panel_administracion = "Libros"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar libros: {e}")
    elif clase == "Autores":
        try:
            self.registros = None
            autores = Autores()
            self.registros = autores.autores
            self.indice_actual = 0
            self.titulo_panel_administracion = "Autores"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar autores: {e}")
    elif clase == "Editoriales":
        try:
            self.registros = None
            editoriales = Editoriales()
            self.registros = editoriales.editoriales
            self.indice_actual = 0
            self.titulo_panel_administracion = "Editoriales"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar editoriales: {e}")
    elif clase == "Autor-Libro":
        try:
            self.registros = None
            autorlibro = AutorLibro()
            self.registros = autorlibro.autor_libros
            self.indice_actual = 0
            self.titulo_panel_administracion = "Autor-Libro"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar autorlibro: {e}")
    elif clase == "Inicio":
        self.cargarDatos("Inicio")
    else:
        print("No se encontró la clase")

    

def crear_cuerpo_insertar_libros(self,dat_filas):  
    self.campos_insertar = {} 
    for columna in dat_filas:
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
        if columna == "titulo" or columna == "año":
            self.campos_insertar[columna] = tk.Entry(
                frame_fila, font=("Arial", 14, "bold"))
            self.campos_insertar[columna].pack(
                side="left", expand=True, fill="x", padx=15)
        if columna == "autor" or columna == "editorial":
            editoriales = Editoriales()
            autores = Autores()
            editorialesNombre = [
                editorial["nombre"] for editorial in editoriales.editoriales]
            autoresNombres = [
                f"{autor["nombre"]} {autor["apellido"]}" for autor in autores.autores]
            # Lista de opciones para el autor o editorial
            opcionesEditoriales = editorialesNombre
            opcionesAutores = autoresNombres
            # Establece la opción por defecto
            if columna == "autor":
                self.campos_insertar[columna] = ttk.Combobox(
                    frame_fila, values=opcionesAutores, font=("Arial", 14, "bold"))
                self.campos_insertar[columna].set(
                    autoresNombres[0])
            elif columna == "editorial":
                self.campos_insertar[columna] = ttk.Combobox(
                    frame_fila, values=opcionesEditoriales, font=("Arial", 14, "bold"))
                self.campos_insertar[columna].set(
                    editorialesNombre[0])
            self.campos_insertar[columna].pack(
                side="left", expand=True, fill="x", padx=15)
                    
def crear_cuerpo_insertar_autor_libro(self,dat_filas):
    self.campos_insertar = {} 
    for columna in dat_filas:
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
        if columna == "autor":
            autores = Autores()
            self.autoresNombres = [
                f"{autor["nombre"]} {autor["apellido"]}" for autor in autores.autores]
            # Lista de opciones para el autor o editorial
            opcionesAutores = self.autoresNombres
            self.campos_insertar[columna] = ttk.Combobox(
                frame_fila, values=opcionesAutores, font=("Arial", 14, "bold"))
            self.campos_insertar[columna].set(
                self.autoresNombres[0])
        if columna == "libro":
            libros = Libros()
            self.librosNombres = [
                libro["titulo"] for libro in libros.libros]
            # Lista de opciones para el autor o editorial
            opcionesLibros = self.librosNombres
            self.campos_insertar[columna] = ttk.Combobox(
                frame_fila, values=opcionesLibros, font=("Arial", 14, "bold"))
            self.campos_insertar[columna].set(
                self.librosNombres[0])
        self.campos_insertar[columna].pack(
            side="left", expand=True, fill="x", padx=15)
        
def crear_cuerpo_actualizar_libros(self,dat_filas):  
    self.campos_actualizar = {}
    for columna, value in dat_filas.items():
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                 anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
        
        if columna == "editorial":
            editoriales = Editoriales()
            self.editorialesNombre = [
                editorial["nombre"] for editorial in editoriales.editoriales]
            # Lista de opciones para el autor o editorial
            opcionesEditoriales = self.editorialesNombre
            self.campos_actualizar[columna] = ttk.Combobox(
                frame_fila, values=opcionesEditoriales, font=("Arial", 14, "bold"))
            self.campos_actualizar[columna].set(
                self.editorialesNombre[0])
            self.campos_actualizar[columna].pack(
                side="left", expand=True, fill="x", padx=15)
        else:    
            self.campos_actualizar[columna] = tk.Entry(
                frame_fila, font=("Arial", 14, "bold"))
            self.campos_actualizar[columna].insert(0, value)
            self.campos_actualizar[columna].pack(
                side="left", expand=True, fill="x", padx=15)
            
        if "id" in columna or "autor" in columna:
            self.campos_actualizar[columna].config(state="readonly", fg="darkgrey")

def crear_cuerpo_actualizar_autor_libro(self,dat_filas):  
    self.campos_actualizar = {}
    for columna, value in dat_filas.items():
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                 anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
        if columna=="libro":
            libros = Libros()
            self.librosNombres = [
                libro["titulo"] for libro in libros.libros]
            # Lista de opciones para el autor o editorial
            opcionesLibros = self.librosNombres
            self.campos_actualizar[columna] = ttk.Combobox(
                frame_fila, values=opcionesLibros, font=("Arial", 14, "bold"))
            self.campos_actualizar[columna].set(
                self.librosNombres[0])
            self.campos_actualizar[columna].pack(
                side="left", expand=True, fill="x", padx=15)
        if columna == "autor":
            autores = Autores()
            self.autoresNombres = [
                f"{autor['nombre']} {autor['apellido']}" for autor in autores.autores]
            # Lista de opciones para el autor o editorial
            opcionesAutores = self.autoresNombres
            self.campos_actualizar[columna] = ttk.Combobox(
                frame_fila, values=opcionesAutores, font=("Arial", 14, "bold"))
            self.campos_actualizar[columna].set(
                self.autoresNombres[0])
            self.campos_actualizar[columna].pack(
                side="left", expand=True, fill="x", padx=15)
       