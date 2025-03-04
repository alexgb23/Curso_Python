import util.util_ventana as util_ventana
import tkinter as tk
from tkinter import ttk, messagebox
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
from clases.libros import Libros
from clases.autores import Autores
from clases.editoriales import Editoriales
from clases.autorlibro import AutorLibro


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


def acciones(self, buton, btn_info_sup):
    marcar_boton_sup(self, buton, btn_info_sup)

    # Verificar si hay una fila seleccionada antes de procesar otras acciones
    if not self.campo_selected_table:
        messagebox.showinfo(
            "Error", "Seleccione una fila en la tabla para actualizar")
        return  # Salir de la función si no hay selección

    # Manejo de acciones según el texto del botón
    accion_texto = btn_info_sup["text"]

    if accion_texto == "Prueba":
        slide_in(self, self.panel_cuerpo)
    elif accion_texto == "Actualizar":
        slide_out(self, self.panel_cuerpo)
        self.creacion_acciones_cuerpo_datos("Actualizar")
        self.mostrar_panel_Actualizar(self.panel_acciones_cuerpo)
    elif accion_texto == "Insertar":
        slide_out(self, self.panel_cuerpo)
        self.creacion_acciones_cuerpo_datos("Insertar")
        self.mostrar_panel_Actualizar(self.panel_acciones_cuerpo)
    elif accion_texto == "Eliminar":
        messagebox.showinfo("Eliminar", "Eliminar")


def marcar_boton(self, boton, btn_info):
    # Si hay un botón activo, restaurar su color
    if self.boton_activo:
        # Restaura el color original
        self.boton_activo.config(bg=COLOR_BTN)
        # Actualiza el estado del botón anterior
        for btn in self.btn_info:
            if btn["text"] == self.boton_activo.cget("text").strip():
                btn["activo"] = False

    # Marca el botón seleccionado
    # Cambia el color del botón activo
    boton.config(bg=COLOR_MENU_CURSOR_ENCIMA)
    self.boton_activo = boton  # Actualiza el botón activo
    # Actualiza el estado del botón actual
    btn_info["activo"] = True


def marcar_boton_sup(self, buton, btn_info_sup):
    # Si hay un botón activo, restaurar su color
    if self.boton_activo_sup:
        # Restaura el color original
        self.boton_activo_sup.config(bg=COLOR_BTN)
        # Actualiza el estado del botón anterior
        for btn in self.btn_info:  # Usa self.btn_info_sup aquí
            if btn["text"] == self.boton_activo_sup.cget("text").strip():
                btn["activo"] = False
    # Marca el botón seleccionado
    # Cambia el color del botón activo
    buton.config(bg=COLOR_MENU_CURSOR_ENCIMA)
    self.boton_activo_sup = buton  # Actualiza el botón activo
    # Actualiza el estado del botón actual
    btn_info_sup["activo"] = True


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

    def toggle(self, ventana):
        if self.ventanas.get(ventana) is None:
            # Guardar información detallada
            self.ventanas[ventana] = self.get_window_details(ventana)

        if self.visible:
            self.slide_out(ventana)
        else:
            self.slide_in(ventana)


def slide_out(self, ventana):
    # Guardar información detallada si no se ha hecho ya
    if self.ventanas.get(ventana) is None:
        self.ventanas[ventana] = self.get_window_details(ventana)
        print(self.ventanas[ventana])
    # Función para mover la ventana hacia arriba

    def mover_ventana(i):
        if i <= 200:  # Continuar hasta que haya deslizado completamente
            # Mover hacia arriba
            ventana.place(x=ventana.winfo_x(), y=ventana.winfo_y() - i)
            self.update_idletasks()
            # Llama a sí mismo con el nuevo valor
            self.after(10, mover_ventana, i + 5)
        else:
            ventana.place_forget()  # Ocultar la ventana al final del movimiento
            self.visible = False
    # Iniciar el movimiento
    mover_ventana(0)


def slide_in(self, ventana):
    detalles = self.ventanas[ventana]
    original_x = detalles['x']
    original_y = detalles['y']
    original_width = detalles['width']
    original_height = detalles['height']
    # Desactivar el ajuste automático de tamaño
    ventana.update_idletasks()  # Asegúrate de que el tamaño se calcule correctamente
    # Coloca la ventana fuera de la vista inicialmente
    ventana.place(x=original_x, y=original_y -
                  original_height, width=original_width)
    # Función para mover la ventana hacia abajo

    def mover_ventana(i):
        if i <= original_height:
            ventana.place(x=original_x, y=original_y -
                          original_height + i, width=original_width)
            self.update_idletasks()
            self.after(10, mover_ventana, i + 5)
        else:
            # Asegúrate de que esté en la posición original al final
            ventana.place(x=original_x, y=original_y,
                          width=original_width, height=original_height)
    mover_ventana(0)
    self.visible = True


def acciones_botones_panel_top(self, campos_actualizar, tabla, boton):
    datos_actualizados = {}

    # Recoger los datos de los campos
    for columna, entry in campos_actualizar.items():
        datos_actualizados[columna] = entry.get()
        print(datos_actualizados)

    # Asegurarte de que el ID se obtiene correctamente
    if tabla == "Libros":
        # Suponiendo que tienes un campo específico para el ID
        # Cambia "id" por el nombre del campo que contiene el ID
        id = campos_actualizar["id"].get()
        print(id)

        # Llamar al método para modificar el registro
        # resultado = Libros.modificar_registro(id, datos_actualizados)

        # Manejar el resultado (opcional)
        # if resultado:
        #     messagebox.showinfo("Éxito", "Registro actualizado correctamente.")
        # else:
        #     messagebox.showerror("Error", "No se pudo actualizar el registro.")


def instanciar(self, clase):
    if clase == "Libros":
        try:
            libros = Libros()
            self.registros = libros.libros_con_autor_y_editorial
            self.indice_actual = 0
            self.titulo_panel_administracion = "Libros"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar libros: {e}")
    elif clase == "Autores":
        try:
            autores = Autores()
            self.registros = autores.autores
            self.indice_actual = 0
            self.titulo_panel_administracion = "Autores"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar autores: {e}")
    elif clase == "Editoriales":
        try:
            editoriales = Editoriales()
            self.registros = editoriales.editoriales
            self.indice_actual = 0
            self.titulo_panel_administracion = "Editoriales"
            self.cargarDatos()
        except Exception as e:
            print(f"Error al instanciar editoriales: {e}")
    elif clase == "Autor-Libro":
        try:
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


def crear_boton(self, tipo_boton):
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
    boton = tk.Button(
        self.panel_acciones_cuerpo,
        text=texto,
        padx=20,
        bg=COLOR_BTN,
        font=("Arial", 12, "bold"),
        fg="white",
        command=lambda: acciones_botones_panel_top(
            self, self.campos_actualizar, self.titulo_panel_administracion, boton)
    )

    # Empaquetar el botón
    boton.pack(side="right", padx=20)
    hover_event(self, boton)
