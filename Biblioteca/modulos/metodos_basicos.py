
import tkinter as tk
from tkinter import ttk
# from panel_Principal.form_maestro_design import *
from tkinter import messagebox
import modulos.botones.btn_selected as btn_selected
from clases.libros import Libros
from clases.editoriales import Editoriales
from clases.autores import Autores
from clases.autorlibro import AutorLibro
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
import modulos.efectos_visuales.transisiones as transition
import modulos.paneles.crear_panel_admin as crear_panel_admin


  


    

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
       