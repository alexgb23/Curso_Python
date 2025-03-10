import tkinter as tk
from tkinter import ttk
from clases.crear_tabla import Crear
import config.config as colores
import util.util_ventana as util_ventana
import modulos.botones.btn_hover as btn_hover


def nueva_tabla_Base_Datos(self):
    if self.titulo_panel_administracion == "Bienvenido a eDe-Lib":
        self.panel_inicio.pack_forget()
    else:
        self.panel_datos.pack_forget()

    self.panel_nueva_tabla = tk.Frame(self.cuerpo_principal, bg=colores.COLOR_CUERPO_PRINCIPAL)
    self.panel_nueva_tabla.place(relwidth=1, relheight=1)

    self.titulo_panel_administracion = "Nueva Tabla en la Base de Datos"

    ancho= 1024
    alto= 600

    self.panel_cuerpo_tabla = tk.Frame(self.panel_nueva_tabla, bg=colores.COLOR_PANEL_INFO)

    #Metodo para centrar el panel_cuerpo
    def ajustar_panel():
        x, y = util_ventana.centrar_panel(self.panel_nueva_tabla, ancho, alto)
        self.panel_cuerpo_tabla.place(width=ancho, height=alto, x=x, y=y)
        self.coordenadas = [x, y, ancho, alto]

    
    tk.Label(self.panel_cuerpo_tabla, text="Para Crear una nueva Tabla en la Base de Datos, por favor ingrese los datos solicitados",
              bg=colores.COLOR_PANEL_INFO, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 16, "bold")).place(relx=0.5, y=10, anchor="n")
    
    
    self.primeraFila = tk.Frame(self.panel_cuerpo_tabla, bg=colores.COLOR_PANEL_INFO)
    self.primeraFila.place(relx=0.5, y=70, anchor="n")
    tk.Label(self.primeraFila, text="Ingrese el Nombre de la Tabla", 
             bg=colores.COLOR_PANEL_INFO, 
             fg=colores.COLOR_BARRA_SUPERIOR, 
             font=("Arial", 12, "bold")).pack(side="left", padx=10)
    self.input_nombre_tabla = tk.Entry(self.primeraFila, bg=colores.COLOR_PANEL_INFO, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))
    self.input_nombre_tabla.pack(side="left", padx=5)
    self.boton_agregar_campo = tk.Button(self.primeraFila, 
                                         text="Agregar Campo", 
                                         command=lambda: agregar_campo(self), 
                                         bg=colores.COLOR_BARRA_SUPERIOR, fg="white", font=("Arial", 12, "bold"))
    self.boton_agregar_campo.pack(side="left", padx=30)


    self.cuerpo_campos = tk.Frame(self.panel_cuerpo_tabla, bg="gray")
    self.cuerpo_campos.place(relx=0.5, y=120, anchor="n")
    self.cuerpo_campos.grid_rowconfigure(0, weight=1)  # Permite que la fila 0 crezca
    self.cuerpo_campos.grid_columnconfigure(0, weight=1)  # Permite que la columna 0 crezca
 


    
    self.chekked=tk.IntVar()

    # Llama a ajustar_panel al configurar panel_datos
    self.panel_nueva_tabla.bind("<Configure>", lambda event: ajustar_panel())

    ajustar_panel()
    btn_hover.hover_event(self, self.boton_agregar_campo)

def agregar_campo(self):
    # Crear campos de forma más compacta
    crear_campo(self, "Nombre:", tk.Entry, None)
    crear_campo(self, "Tipo:", ttk.Combobox, ["INT", "VARCHAR", "TEXT", "DATE"])
    crear_campo(self, "Predeterminado:", ttk.Combobox, ["NULL", "NOT NULL"])
    crear_campo(self, "A/I:", tk.Checkbutton, None, variable=self.chekked)
    crear_campo(self, "Indice:", ttk.Combobox, ["NONE", "PRIMARY KEY", "FOREIGN KEY"])

def crear_campo(self, label_text, widget_type, values=None, **kwargs):
    """Crea un campo con un label y un widget."""
    sub_panel_cuerpo = tk.Frame(self.cuerpo_campos, bg=colores.COLOR_PANEL_INFO)
    sub_panel_cuerpo.grid(row=self.contador_filas, column=0, rowspan=5, columnspan=5,  padx=10, pady=10)

    self.contador_filas += 1

    frame_campo = tk.Frame(sub_panel_cuerpo, bg=colores.COLOR_PANEL_INFO)
    frame_campo.pack(side="left", pady=10, padx=10)


    label = tk.Label(frame_campo, text=label_text, bg=colores.COLOR_PANEL_INFO, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))
    label.pack(side=tk.TOP)

    if widget_type == tk.Entry:
        widget = widget_type(frame_campo, **kwargs, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))
    elif widget_type == ttk.Combobox:
        widget = widget_type(frame_campo, values=values, **kwargs, background=colores.COLOR_PANEL_INFO, foreground=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))
    elif widget_type == tk.Checkbutton:
        widget = widget_type(
            frame_campo,
            **kwargs,
            bg=colores.COLOR_PANEL_INFO,
            fg=colores.COLOR_BARRA_SUPERIOR,
            font=("Arial", 12, "bold"),
            highlightbackground=colores.COLOR_PANEL_INFO,  # Mantener el fondo sin cambios
            activebackground=colores.COLOR_PANEL_INFO  # Color de fondo al hacer clic
        )

    widget.pack(side=tk.BOTTOM)
