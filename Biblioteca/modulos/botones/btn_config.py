from panel_Principal.form_maestro_design import *
import modulos.botones.btn_hover as btn_hover
from modulos.metodos_basicos import *

def configuracion_btn_menu_lateral(self, boton, text, icono, font_awesome, ancho_boton, alto_boton, activo):
    """Configura los parámetros del botón en el menú lateral."""
    boton.config(
        text=f" {icono}  {text}",
        anchor="w",
        font=font_awesome,
        width=ancho_boton,
        height=alto_boton,
        pady=5,
        bg=COLOR_BTN,
        fg="white",
        bd=1,
        relief="raised",
        highlightbackground=COLOR_MENU_LATERAL,
        highlightcolor=COLOR_MENU_LATERAL,
        highlightthickness=2
    )
    boton.pack(side=tk.TOP, pady=8)
    if not activo:
        btn_hover.hover_event(self, boton)
    else:
        self.boton_activo = boton


def configuracion_btn_menu_superior(self, boton, text, icono, font_awesome, ancho_boton, alto_boton, activo):
    """Configura los parámetros del botón en el menú superior."""
    boton.config(
        text=f" {icono}  {text}",
        anchor="w",
        font=font_awesome,
        width=ancho_boton,
        height=alto_boton,
        pady=5,
        bg=COLOR_BTN,
        fg="white",
        bd=1,
        relief="raised",
        highlightbackground=COLOR_BARRA_SUPERIOR,
        highlightcolor=COLOR_BARRA_SUPERIOR,
        highlightthickness=2
    )
    boton.pack(side=tk.RIGHT, padx=15)
    btn_hover.hover_event_sup(self, boton)


def crear_boton_sub_panel(self, tipo_boton):
    """Crea un botón en el subpanel según el tipo especificado."""
    texto = {
        "Actualizar": "Actualizar",
        "Insertar": "Insertar"
    }.get(tipo_boton)

    if not texto:
        return  # Si el tipo de botón no es válido, salir del método

    # Crear el botón
    boton = tk.Button(
        self.panel_acciones_cuerpo,
        text=texto,
        padx=20,
        bg=COLOR_BTN,
        font=("Arial", 12, "bold"),
        fg="white",
        command=lambda: acciones_botones_sub_panel(
            self, self.titulo_panel_administracion, boton)
    )

    # Empaquetar el botón
    boton.pack(side="right", padx=20)
    btn_hover.hover_event(self, boton)
