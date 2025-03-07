from panel_Principal.form_maestro_design import *
import modulos.botones.btn_hover as btn_hover
from modulos.metodos_basicos import *

def configuracion_btn_menu_lateral(self, boton, text, icono, font_awesome, ancho_boton, alto_boton, activo):
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
    # Definir el texto y el comando según el tipo de botón
    if tipo_boton == "Actualizar":
        texto = "Actualizar"
    elif tipo_boton == "Insertar":
        texto = "Insertar"
    elif tipo_boton == "Eliminar":
        texto = "Eliminar"
    else:
        return  # Si el tipo de botón no es válido, salir del método
    # Crear el botón
    buton = tk.Button(
        self.panel_acciones_cuerpo,
        text=texto,
        padx=20,
        bg=COLOR_BTN,
        font=("Arial", 12, "bold"),
        fg="white",
        command=lambda: acciones_botones_sub_panel(
            self, self.titulo_panel_administracion, buton)
    )

    # Empaquetar el botón
    buton.pack(side="right", padx=20)
    btn_hover.hover_event(self, buton)


