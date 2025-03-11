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

    ancho = 1024
    alto = 600
    self.panel_cuerpo_tabla = tk.Frame(self.panel_nueva_tabla, bg=colores.COLOR_PANEL_INFO)

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

    self.cuerpo_campos = tk.Frame(self.panel_cuerpo_tabla, bg=colores.COLOR_PANEL_INFO)
    self.cuerpo_campos.place(relx=0.5, y=120, anchor="n")
    self.sub_cuerpo_campos = tk.Frame(self.cuerpo_campos, bg=colores.COLOR_PANEL_INFO)
    self.sub_cuerpo_campos.grid(row=0, column=0, columnspan=6)

    # Botón para imprimir datos
    self.boton_imprimir = tk.Button(self.panel_cuerpo_tabla, 
                                     text="Imprimir Datos", 
                                     command=lambda: imprimir_datos(self), 
                                     bg=colores.COLOR_BARRA_SUPERIOR, fg="white", font=("Arial", 12, "bold"))
    self.boton_imprimir.place(relx=0.5, y=500, anchor="center")

    self.contador_filas = 0
    self.contador_columnas = 0
    self.check_vars = []  # Lista para almacenar las variables de control

    

    self.panel_nueva_tabla.bind("<Configure>", lambda event: ajustar_panel())
    ajustar_panel()
    btn_hover.hover_event(self, self.boton_agregar_campo)

def agregar_campo(self):
    # Crear una nueva variable para el Checkbutton
    check_var = tk.IntVar()
    self.check_vars.append(check_var)  # Agregar a la lista

    # Crear los campos
    crear_campo(self, "Nombre:", tk.Entry)
    tipo_widget = crear_campo(self, "Tipo:", ttk.Combobox, ["INT", "VARCHAR", "TEXT", "DATE"])
    longitud_widget = crear_campo(self, "Longitud:", tk.Entry)
    predeterminado_widget = crear_campo(self, "Predeterminado:", ttk.Combobox, ["NULL", "NOT NULL"])
    
    # Crear el Checkbutton
    ai_widget = crear_campo(self, "A/I:", tk.Checkbutton, None, variable=check_var)
    
    # Crear el Combobox para el índice
    indice_widget = crear_campo(self, "Indice:", ttk.Combobox, ["NONE", "PRIMARY KEY", "FOREIGN KEY"])
    
    # Asociar el método para habilitar/deshabilitar
    check_var.trace_add("write", lambda *args: actualizar_estado_campos(self, check_var, tipo_widget, indice_widget))

def crear_campo(self, label_text, widget_type, values=None, **kwargs):
    frame_campo = tk.Frame(self.sub_cuerpo_campos, bg=colores.COLOR_PANEL_INFO)
    frame_campo.grid(row=self.contador_filas, column=self.contador_columnas, padx=10, pady=5, sticky="w")
    
    self.contador_columnas += 1
    if self.contador_columnas >= 6:
        self.contador_columnas = 0
        self.contador_filas += 1

    tk.Label(frame_campo, text=label_text, bg=colores.COLOR_PANEL_INFO, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold")).pack(side=tk.TOP)

    if widget_type == tk.Entry:
        widget = widget_type(frame_campo, **kwargs, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))
    elif widget_type == ttk.Combobox:
        widget = widget_type(frame_campo, values=values, **kwargs, background=colores.COLOR_PANEL_INFO, foreground=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))
    elif widget_type == tk.Checkbutton:
        widget = widget_type(frame_campo, **kwargs, bg=colores.COLOR_PANEL_INFO, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 12, "bold"))

    widget.pack(side=tk.BOTTOM)
    return widget  # Asegúrate de devolver el widget creado

def actualizar_estado_campos(self, check_var, tipo_widget, indice_widget):
    if check_var.get():  # Si el Checkbutton está activado
        tipo_widget.set("INT")  # Establecer tipo como INT
        tipo_widget.configure(state='disabled')  # deshabilitar edición
        indice_widget.set("PRIMARY KEY")  # Establecer índice como PRIMARY KEY
        indice_widget.configure(state='disabled')  # deshabilitar edición
    else:
        tipo_widget.configure(state='normal')  # Habilitar edición
        indice_widget.configure(state='normal')  # Habilitar edición


def imprimir_datos(self):
    datos = []
    nombre_tabla = self.input_nombre_tabla.get()
    datos.append(f"Nombre de la Tabla: {nombre_tabla}")
    
    checkbutton_index = 0  # Contador para los Checkbuttons
    for widget in self.sub_cuerpo_campos.winfo_children():
        if isinstance(widget, tk.Frame):
            label_text = ""
            # Buscar el Label en el Frame
            for child in widget.winfo_children():
                if isinstance(child, tk.Label):
                    label_text = child.cget("text")  # Obtener el texto del Label
                elif isinstance(child, tk.Entry):
                    datos.append(f"{label_text}: {child.get()}")
                elif isinstance(child, ttk.Combobox):
                    datos.append(f"{label_text}: {child.get()}")
                elif isinstance(child, tk.Checkbutton):
                    estado = "Activado" if self.check_vars[checkbutton_index].get() else "Desactivado"
                    datos.append(f"{label_text}: {estado}")
                    checkbutton_index += 1  # Incrementar solo cuando se imprime un Checkbutton

    print("\n".join(datos))

