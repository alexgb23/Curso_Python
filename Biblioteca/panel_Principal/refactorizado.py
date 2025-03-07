import tkinter as tk
from tkinter import ttk
from tkinter import font
from config.config import (
    COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL,
    COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
)
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from metodos_basicos.metodos_basicos import *
from clases.editoriales import Editoriales
from clases.autores import Autores


class FormMaestro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.init_variables()
        self.load_images()
        self.configure_window()
        self.create_panels()
        self.create_menu_controls()
        self.create_top_bar_controls()
        self.create_start_panel()

    def init_variables(self):
        self.boton_activo = None
        self.boton_activo_sup = None
        self.registros = []
        self.indice_actual = 0
        self.campo_selected_table = {}
        self.ancho_cuerpo = 600
        self.alto_cuerpo = 320
        self.visible = True
        self.titulo_panel_administracion = None

    def load_images(self):
        try:
            self.perfil = util_img.leer_imagen("image/eDe-Lib.png", (250, 250))
            self.exit = util_img.leer_imagen_con_transparencia("image/delete_exit_1195.png", (32, 32))
        except FileNotFoundError as e:
            print(f"Error: {e}")

    def configure_window(self):
        config_window(self)

    def create_panels(self):
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=300)
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=200)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)

    def create_start_panel(self):
        self.titulo_panel_administracion = "Bienvenido a eDe-Lib"
        self.panel_inicio = tk.Frame(self.cuerpo_principal, bg="white")
        self.panel_inicio.place(relwidth=1, relheight=1)

        self.canvas = tk.Canvas(self.panel_inicio, highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)

        self.redimensionar_imagen()
        self.panel_inicio.bind("<Configure>", self.redimensionar_imagen)

        self.label_inicio = ttk.Label(self.canvas, text=self.titulo_panel_administracion,
                                       foreground=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 36, "bold"))
        self.label_inicio.place(relx=0.5, y=15, anchor="n")

        self.label_info = ttk.Label(self.canvas, text="Plataforma de gestión de bibliotecas",
                                     foreground=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 16, "bold"))
        self.label_info.place(relx=0.5, y=80, anchor="n")

    def redimensionar_imagen(self, event=None):
        width = self.panel_inicio.winfo_width()
        height = self.panel_inicio.winfo_height()

        self.foto_fondo = util_img.leer_imagen("image/muebles-bibliotecas-estanteria-etiquetada.webp", (width, height))
        self.canvas.delete("all")
        self.canvas.create_image(0, 0, anchor="nw", image=self.foto_fondo)
        self.canvas.image = self.foto_fondo

    def create_top_bar_controls(self):
        self.labelTitulo = tk.Label(self.barra_superior, text="¡Bienvenido!", fg="white", font=("Time New Roman", 24, "bold"),
                                     bg=COLOR_BARRA_SUPERIOR, padx=10, pady=16)
        self.labelTitulo.pack(side=tk.LEFT, padx=15)

        self.salir = tk.Button(self.barra_superior, image=self.exit, command=self.destroy, bg="pink")
        self.salir.pack(side=tk.RIGHT, padx=15)

        self.btn_info_sup = [
            {"text": "Actualizar", "icon": "\uf021"},
            {"text": "Eliminar", "icon": "\uf2ed"},
            {"text": "Insertar", "icon": "\uf067"},
            {"text": "Buscar", "icon": "\uf002"},
        ]

        for btn in self.btn_info_sup:
            self.create_top_button(btn)

        hover_event_Exit(self, self.salir)

    def create_top_button(self, btn_info):
        but = tk.Button(self.barra_superior)
        self.configurar_btn_superior(but, btn_info["text"], btn_info["icon"])
        but.config(command=lambda b=but, btn=btn_info: acciones(self, b, btn))
        but.pack(side=tk.RIGHT, padx=15)

    def create_menu_controls(self):
        self.labelLogo = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelLogo.pack(side=tk.TOP, pady=10, padx=10)

        self.btn_info = [
            {"text": "Inicio", "icon": "\uf0e4"},
            {"text": "Libros", "icon": "\uf0f6"},
            {"text": "Autores", "icon": "\uf0f6"},
            {"text": "Editoriales", "icon": "\uf0f6"},
            {"text": "Usuarios", "icon": "\uf0f6"},
            {"text": "Crear Tabla", "icon": "\uf0f6"},
            {"text": "Autor-Libro", "icon": "\uf0f6"},
        ]

        for btn in self.btn_info:
            self.create_menu_button(btn)

    def create_menu_button(self, btn_info):
        boton = tk.Button(self.menu_lateral)
        self.configurar_btn_menu(boton, btn_info["text"], btn_info["icon"])
        boton.config(command=lambda b=boton, btn=btn_info: instanciar_y_marcar(self, b, btn))
        boton.pack(side=tk.TOP, pady=8)

        if btn_info["text"] == "Inicio" and not self.titulo_panel_administracion:
            btn_info["activo"] = True
            marcar_boton(self, boton, btn_info)

    def configurar_btn_superior(self, boton, text, icono):
        boton.config(
            text=f" {icono}  {text}",
            anchor="w",
            font=font.Font(family="FontAwesome", size=12),
            width=15,
            height=1,
            pady=5,
            bg=COLOR_BTN,
            fg="white",
            bd=1,
            relief="raised",
            highlightbackground=COLOR_BARRA_SUPERIOR,
            highlightcolor=COLOR_BARRA_SUPERIOR,
            highlightthickness=2
        )

    def configurar_btn_menu(self, boton, text, icono):
        boton.config(
            text=f" {icono}  {text}",
            anchor="w",
            font=font.Font(family="FontAwesome", size=15),
            width=20,
            height=1,
            pady=5,
            bg=COLOR_BTN,
            fg="white",
            bd=1,
            relief="raised",
            highlightbackground=COLOR_MENU_LATERAL,
            highlightcolor=COLOR_MENU_LATERAL,
            highlightthickness=2
        )
        if not self.boton_activo:
            hover_event(self, boton)
        else:
            self.boton_activo = boton

    def cargarDatos(self, quepanel=None):
        if quepanel == "Inicio" and self.titulo_panel_administracion != "Bienvenido a eDe-Lib":
            self.panel_datos.pack_forget()
            self.create_start_panel()
        elif quepanel != "Inicio":
            self.panel_inicio.pack_forget()
            self.create_data_body()

    def create_data_body(self):
        self.panel_datos = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.panel_datos.place(relwidth=1, relheight=1)

        self.panel_cuerpo = tk.Frame(self.panel_datos, bg=COLOR_PANEL_INFO)
        self.panel_cuerpo.pack(pady=10, fill="x")

        self.campos = {}
        self.columnas = list(self.registros[0].keys())
        etiquetas = {"anio": "Año"}

        for columna in self.columnas:
            self.create_data_row(columna, etiquetas)

        self.create_navigation_buttons()

    def create_data_row(self, columna, etiquetas):
        frame_fila = tk.Frame(self.panel_cuerpo, bg=COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")

        texto_label = etiquetas.get(columna, columna.title())
        tk.Label(frame_fila, text=texto_label, width=15,
                 anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)

        self.campos[columna] = ttk.Entry(frame_fila, font=("Arial", 14, "bold"))
        self.campos[columna].pack(side="left", expand=True, fill="x", padx=15)

    def create_navigation_buttons(self):
        btnMas = tk.Button(self.panel_cuerpo, text="Siguiente", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                           command=self.siguiente_registro)
        btnMas.pack(side="right", padx=20)
        hover_event_sup(self, btnMas)

        btnMenos = tk.Button(self.panel_cuerpo, text="Anterior", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                             command=self.anterior_registro)
        btnMenos.pack(side="right", padx=20)
        hover_event_sup(self, btnMenos)

        self.mostrar_registro()
        self.crear_tabla()

    def mostrar_registro(self):
        if not self.registros:
            return

        registro_actual = self.registros[self.indice_actual]
        for columna, campo in self.campos.items():
            campo.config(state="normal")
            campo.delete(0, tk.END)
            campo.insert(0, registro_actual[columna])
            campo.config(state="readonly")

    def siguiente_registro(self):
        if self.indice_actual < len(self.registros) - 1:
            self.indice_actual += 1
            self.mostrar_registro()

    def anterior_registro(self):
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_registro()

    def crear_tabla(self):
        self.columnas = list(self.registros[0].keys())
        style = ttk.Style()
        style.configure("Heading", background=COLOR_CABECERA_TABLA)
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))
        style.configure("Treeview", font=("Arial", 12), background=COLOR_PANEL_INFO)

        self.tabla = ttk.Treeview(self.panel_tabla, columns=self.columnas, show="headings", style="Treeview")
        for col in self.columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=200)

        for registro in self.registros:
            self.tabla.insert("", "end", values=[registro[col] for col in self.columnas])

        scrollbar = tk.Scrollbar(self.panel_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        self.tabla.grid(row=0, column=0, columnspan=4, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.panel_tabla.grid_rowconfigure(0, weight=1)
        self.panel_tabla.grid_columnconfigure(0, weight=1)
        self.tabla.bind("<ButtonRelease-1>", self.on_item_tabla_click)

    def on_item_tabla_click(self, event):
        self.campo_selected_table = {}
        item = self.tabla.selection()
        if item:
            self.campo_selected_table = {col: val for col, val in zip(self.tabla["columns"], self.tabla.item(item, "values"))}

    # Otros métodos se mantienen igual...
