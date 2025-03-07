import config.config as colores

def marcar_boton(self, boton, btn_info, es_superior=False):
    # Determinar el botón activo y la lista de botones según el tipo
    if es_superior:
        boton_activo = self.boton_activo_sup
        btn_info_lista = self.btn_info_sup
    else:
        boton_activo = self.boton_activo
        btn_info_lista = self.btn_info

    # Si hay un botón activo, restaurar su color
    if boton_activo:
        boton_activo.config(bg=colores.COLOR_BTN)
        # Actualiza el estado del botón anterior
        for btn in btn_info_lista:
            if btn["text"] == boton_activo.cget("text").strip():
                btn["activo"] = False  # Desmarcar el botón anterior

    # Marca el botón seleccionado
    boton.config(bg=colores.COLOR_MENU_CURSOR_ENCIMA)
    if es_superior:
        self.boton_activo_sup = boton  # Actualiza el botón activo superior
    else:
        self.boton_activo = boton  # Actualiza el botón activo lateral

    btn_info["activo"] = True  # Marca el botón actual como activo


def reset_btn_sup(self):
    if self.boton_activo_sup:
        self.boton_activo_sup.config(bg=colores.COLOR_BTN)
        for btn in self.btn_info_sup:
            if btn["text"] == self.boton_activo_sup.cget("text").strip():
                btn["activo"] = False


