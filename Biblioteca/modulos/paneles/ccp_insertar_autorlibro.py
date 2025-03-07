from tkinter import ttk
import tkinter as tk
import modulos.botones.btn_config as btn_config
from clases.autores import Autores
from clases.libros import Libros



def crear_cuerpo_panel_insertar_autor_libro(self,dat_filas):
    self.campos_insertar = {} 
    for columna in dat_filas:
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=btn_config.COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                anchor="w", font=("Arial", 14, "bold"), bg=btn_config.COLOR_PANEL_INFO).pack(side="left", padx=5)
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
        

