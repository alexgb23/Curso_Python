import config.config as colores

def hover_event(self, boton):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo != boton:  # Evita hover en el botón activo
            boton.config(bg=colores.COLOR_MENU_CURSOR_ENCIMA,
                         cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo != boton:  # Evita restaurar en el botón activo
            boton.config(bg=colores.COLOR_BTN, fg="white")
    boton.bind("<Enter>", on_enter)
    boton.bind("<Leave>", on_leave)


def hover_event_sup(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.boton_activo_sup != boton_sup:  # Evita hover en el botón activo
            boton_sup.config(bg=colores.COLOR_MENU_CURSOR_ENCIMA,
                             cursor="hand2", fg="white")

    def on_leave(e):
        if self.boton_activo_sup != boton_sup:  # Evita restaurar en el botón activo
            boton_sup.config(bg=colores.COLOR_BTN, fg="white")
    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)

    

def hover_event_Exit(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        boton_sup.config(cursor="hand2")
        boton_sup.config(image=self.exit2)

    def on_leave(e):
        boton_sup.config(cursor="arrow")
        boton_sup.config(image=self.exit)

    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)

def hover_event_minimizar(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        boton_sup.config(cursor="hand2")
        boton_sup.config(image=self.min2)

    def on_leave(e):
        boton_sup.config(cursor="arrow")
        boton_sup.config(image=self.min)

    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)


def hover_event_maximizar(self, boton_sup):
    # Verifica si el botón es el activo para aplicar hover
    def on_enter(e):
        if self.winfo_toplevel().state() == "zoomed" and self.winfo_toplevel().overrideredirect():
            boton_sup.config(image=self.max)
            boton_sup.config(cursor="hand2")
        else:
            boton_sup.config(image=self.maxmax)
            boton_sup.config(cursor="hand2")


    def on_leave(e):
        if self.winfo_toplevel().state() == "zoomed" and self.winfo_toplevel().overrideredirect():
            boton_sup.config(image=self.maxmax)
            boton_sup.config(cursor="arrow")
        else:
            boton_sup.config(image=self.max)
            boton_sup.config(cursor="arrow")

    boton_sup.bind("<Enter>", on_enter)
    boton_sup.bind("<Leave>", on_leave)



def hover_event_label(self, label):
    def on_enter(e):
        label.configure(cursor="hand2", foreground="red")

    def on_leave(e):
        label.configure(foreground=colores.COLOR_MENU_CURSOR_ENCIMA,)

    label.bind("<Enter>", on_enter)
    label.bind("<Leave>", on_leave)
