import util.util_ventana as util_ventana
import tkinter as tk
from tkinter import ttk, messagebox
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
from clases.libros import Libros
from clases.autores import Autores
from clases.editoriales import Editoriales
from clases.autorlibro import AutorLibro
from tkinter import font


def config_window(self):
    self.title("eDe-Lib")
    self.iconbitmap("./image/books.ico")
    w, h = 1366, 768
    self.geometry("%dx%d+0+0" % (w, h))
    util_ventana.centrar_ventana(self, w, h)


def instanciar_y_marcar(self, boton, btn_info):
    # Llama a los métodos deseados
    marcar_boton(self, boton, btn_info)  # Marca el botón
    instanciar(self, btn_info["text"])   # Llama a instanciar

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
    
def acciones(self, buton, btn_info_sup):
    marcar_boton(self, buton, btn_info_sup, True)

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
        slide_in(self, self.panel_acciones_cuerpo)
    elif accion_texto == "Insertar":
        if self.titulo_panel_administracion == "Bienvenido a eDe-Lib": 
            messagebox.showinfo(
            "Error", "Debe seleccionar en el menu lateral que desea Insertar"
            )
            return
        self.transicion_paneles_if_true()      
        self.creacion_acciones_cuerpo_datos("Insertar")
        slide_in(self, self.panel_acciones_cuerpo)
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
        
        


def marcar_boton(self, boton, btn_info, es_superior=False):
    # Determinar el botón activo y la lista de botones según el tipo
    if es_superior:
        boton_activo = self.boton_activo_sup
        btn_info_lista = self.btn_info_sup
    else:
        boton_activo = self.boton_activo
        btn_info_lista = self.btn_info

    # Si hay un botón activo, restaurar su color
    if boton_activo:
        boton_activo.config(bg=COLOR_BTN)
        # Actualiza el estado del botón anterior
        for btn in btn_info_lista:
            if btn["text"] == boton_activo.cget("text").strip():
                btn["activo"] = False  # Desmarcar el botón anterior

    # Marca el botón seleccionado
    boton.config(bg=COLOR_MENU_CURSOR_ENCIMA)
    if es_superior:
        self.boton_activo_sup = boton  # Actualiza el botón activo superior
    else:
        self.boton_activo = boton  # Actualiza el botón activo lateral

    btn_info["activo"] = True  # Marca el botón actual como activo


def reset_btn_sup(self):
    if self.boton_activo_sup:
        self.boton_activo_sup.config(bg=COLOR_BTN)
        for btn in self.btn_info_sup:
            if btn["text"] == self.boton_activo_sup.cget("text").strip():
                btn["activo"] = False


def hover_event(self, boton):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo != boton:  # Evita hover en el botón activo
            boton.config(bg=COLOR_MENU_CURSOR_ENCIMA,
                         cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo != boton:  # Evita restaurar en el botón activo
            boton.config(bg=COLOR_BTN, fg="white")
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)


def hover_event_sup(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo_sup != boton_sup:  # Evita hover en el botón activo
            boton_sup.config(bg=COLOR_MENU_CURSOR_ENCIMA,
                             cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo_sup != boton_sup:  # Evita restaurar en el botón activo
            boton_sup.config(bg=COLOR_BTN, fg="white")
    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)

    




def hover_event_Exit(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo_sup != boton_sup:  # Evita hover en el botón activo
            boton_sup.config(bg="yellow",
                             cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo_sup != boton_sup:  # Evita restaurar en el botón activo
            boton_sup.config(bg="pink", fg="white")
    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)

    # def toggle(self, ventana):
    #     if self.ventanas.get(ventana) is None:
    #         # Guardar información detallada
    #         self.ventanas[ventana] = self.get_window_details(ventana)

    #     if self.visible:
    #         self.slide_out(ventana)
    #     else:
    #         self.slide_in(ventana)


def slide_out(self, ventana):
    def mover_ventana(i):
        if i <= 200:  # Continuar hasta que haya deslizado completamente
            # Mover hacia arriba
            ventana.place(x=ventana.winfo_x(), y=ventana.winfo_y() - i)
            self.update_idletasks()
            # Llama a sí mismo con el nuevo valor
            self.after(10, mover_ventana, i + 5)
        else:
            ventana.place_forget()  # Ocultar la ventana al final del movimiento
    # Iniciar el movimiento
    mover_ventana(0)



def slide_in(self, ventana, tiempo_espera=800):  # tiempo_espera en milisegundos
    original_x = self.coordenadas[0]
    original_y = self.coordenadas[1]
    original_width = self.ancho_cuerpo
    original_height = self.alto_cuerpo

    # Desactivar el ajuste automático de tamaño
    ventana.update_idletasks()  # Asegúrate de que el tamaño se calcule correctamente
    # Coloca la ventana fuera de la vista inicialmente
    ventana.place(x=original_x, y=original_y - original_height, width=original_width)

    # Función para mover la ventana hacia abajo
    def mover_ventana(i):
        if i <= original_height:
            ventana.place(x=original_x, y=original_y - original_height + i, width=original_width)
            self.update_idletasks()
            self.after(10, mover_ventana, i + 5)
        else:
            # Asegúrate de que esté en la posición original al final
            ventana.place(x=original_x, y=original_y, width=original_width, height=original_height)

    # Esperar antes de iniciar el movimiento
    self.after(tiempo_espera, mover_ventana, 0)



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
    reset_btn_sup(self)
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
            self.registros = autorlibro.autorlibrocompleto
            self.indice_actual = 0
            self.titulo_panel_administracion = "Autor-Libro"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar autorlibro: {e}")
    elif clase == "Inicio":
        self.cargarDatos("Inicio")
    else:
        print("No se encontró la clase")

    


def crear_boton_sub_panel(self, tipo_boton):
    # Definir el texto y el comando según el tipo de botón
    if tipo_boton == "Actualizar":
        texto = "Actualizar"
    elif tipo_boton == "Insertar":
        texto = "Insertar"
    elif tipo_boton == "Eliminar":
        texto = "Eliminar"
    else:
        return  # Si el tipo de botón no es válido, salir del método
    # Crear el botón
    buton = tk.Button(
        self.panel_acciones_cuerpo,
        text=texto,
        padx=20,
        bg=COLOR_BTN,
        font=("Arial", 12, "bold"),
        fg="white",
        command=lambda: acciones_botones_sub_panel(
            self, self.titulo_panel_administracion, buton)
    )

    # Empaquetar el botón
    buton.pack(side="right", padx=20)
    hover_event(self, buton)

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
       