from tkinter import ttk
import tkinter as tk
import modulos.botones.btn_config as btn_config
from clases.libros import Libros
from clases.autores import Autores


def crear_cuerpo_panel_actualizar_autor_libro(self,dat_filas):  
    self.campos_actualizar = {}
    for columna, value in dat_filas.items():
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=btn_config.COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                 anchor="w", font=("Arial", 14, "bold"), bg=btn_config.COLOR_PANEL_INFO).pack(side="left", padx=5)
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
       