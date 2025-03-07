from tkinter import ttk
import tkinter as tk
import modulos.botones.btn_config as btn_config
from clases.editoriales import Editoriales


def crear_cuerpo_panel_actualizar_libros(self,dat_filas):  
    self.campos_actualizar = {}
    for columna, value in dat_filas.items():
        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=btn_config.COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")
        tk.Label(frame_fila, text=columna, width=15,
                 anchor="w", font=("Arial", 14, "bold"), bg=btn_config.COLOR_PANEL_INFO).pack(side="left", padx=5)
        
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
