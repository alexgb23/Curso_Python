import tkinter as tk
import modulos.botones.btn_hover as btn_hover
import modulos.botones.btn_config as btn_config
import config.config as colores
from tkinter import font
import modulos.ejecucion_click.click_btn_insertData_BD as ejecutar

def configuracion_btn_menu_lateral(self, boton, text, icono, activo):
    """Configura los parámetros del botón en el menú lateral."""
    boton.config(
        text=f" {icono}  {text}",
        anchor="w",
        font=font.Font(family="FontAwesome", size=15),
        width=20,
        height=1,
        pady=5,
        bg=colores.COLOR_BTN,
        fg="white",
        bd=1,
        relief="raised",
        highlightbackground=colores.COLOR_MENU_LATERAL,
        highlightcolor=colores.COLOR_MENU_LATERAL,
        highlightthickness=2
    )
    boton.pack(side=tk.TOP, pady=8)
    if not activo:
        btn_hover.hover_event(self, boton)
    else:
        self.boton_activo = boton


def configuracion_btn_menu_superior(self, boton, text, icono, activo):
    """Configura los parámetros del botón en el menú superior."""
    boton.config(
        text=f" {icono}  {text}",
        anchor="w",
        font= font.Font(family="FontAwesome", size=12),
        width=15,
        height=1,
        pady=5,
        bg=colores.COLOR_BTN,
        fg="white",
        bd=1,
        relief="raised",
        highlightbackground=colores.COLOR_BARRA_SUPERIOR,
        highlightcolor=colores.COLOR_BARRA_SUPERIOR,
        highlightthickness=2
    )
    boton.pack(side=tk.RIGHT, padx=15)
    btn_hover.hover_event_sup(self, boton)


def crear_boton_sub_panel(self, tipo_boton):
    """Crea un botón en el subpanel según el tipo especificado."""
    texto = {
        "Actualizar": "Actualizar",
        "Insertar": "Insertar", 
        "Buscar": "Buscar"
    }.get(tipo_boton)

    if not texto:
        return  # Si el tipo de botón no es válido, salir del método

    # Crear el botón
    boton = tk.Button(
        self.panel_acciones_cuerpo,
        text=texto,
        padx=20,
        bg=colores.COLOR_BTN,
        font=("Arial", 12, "bold"),
        fg="white",
        
        #este metodo se ejecutara cuando se presione el boton
        #Necesario aquiya que los botones se crean automaticamente
        command=lambda: ejecutar.acciones_botones_sub_panel(
            self, self.titulo_panel_administracion, boton)  
    )

    # Empaquetar el botón
    boton.pack(side="right", padx=20)
    btn_hover.hover_event(self, boton)
