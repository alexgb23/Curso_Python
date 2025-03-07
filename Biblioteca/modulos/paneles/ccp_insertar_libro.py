from tkinter import ttk
import tkinter as tk
import config.config as colores
from clases.autores import Autores
from clases.editoriales import Editoriales



def crear_cuerpo_panel_insertar_libros(self,dat_filas):  
    self.campos_insertar = {} 
    for columna in dat_filas:
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                anchor="w", font=("Arial", 14, "bold"), bg=colores.COLOR_PANEL_INFO).pack(side="left", padx=5)
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
                    