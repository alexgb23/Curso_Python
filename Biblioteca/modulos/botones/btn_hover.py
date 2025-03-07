from panel_Principal.form_maestro_design import *
import modulos.botones.btn_config as btn_config

def hover_event(self, boton):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo != boton:  # Evita hover en el botón activo
            boton.config(bg=btn_config.COLOR_MENU_CURSOR_ENCIMA,
                         cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo != boton:  # Evita restaurar en el botón activo
            boton.config(bg=btn_config.COLOR_BTN, fg="white")
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)


def hover_event_sup(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo_sup != boton_sup:  # Evita hover en el botón activo
            boton_sup.config(bg=btn_config.COLOR_MENU_CURSOR_ENCIMA,
                             cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo_sup != boton_sup:  # Evita restaurar en el botón activo
            boton_sup.config(bg=btn_config.COLOR_BTN, fg="white")
    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)

    

def hover_event_Exit(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo_sup != boton_sup:  # Evita hover en el botón activo
            boton_sup.config(bg="yellow",
                             cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo_sup != boton_sup:  # Evita restaurar en el botón activo
            boton_sup.config(bg="pink", fg="white")
    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)
