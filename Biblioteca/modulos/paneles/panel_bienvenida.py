from tkinter import ttk
import tkinter as tk
import config.config as colores
import modulos.botones.btn_hover as btn_hover


def crear_panel_bienvenida(self):
        self.titulo_panel_administracion = "Bienvenido a eDe-Lib"
        
        # Crear el panel principal
        self.panel_inicio = tk.Frame(self.cuerpo_principal, bg="white")
        self.panel_inicio.place(relwidth=1, relheight=1)

        # Crear un Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.panel_inicio, highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)

        # Llamar a redimensionar_imagen para cargar la imagen inicialmente
        #el metodo redimensionamiento de la imagen de fondo se encuentra en form_maestro 
        self.redimensionar_imagen_fondo_panel_bienvenida()

        # Vincular el evento de redimensionamiento 
        self.panel_inicio.bind("<Configure>", self.redimensionar_imagen_fondo_panel_bienvenida)

        # Crear el Label con texto
        self.label_inicio = ttk.Label(self.canvas, text=self.titulo_panel_administracion,
                                    foreground=colores.COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 36, "bold"))
        self.label_inicio.place(relx=0.5, y=15, anchor="n")

        self.label_info= ttk.Label(self.canvas, text="Plataforma de gestión de bibliotecas",
                                    foreground=colores.COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 16, "bold"))
        self.label_info.place(relx=0.5, y=80, anchor="n")

        self.label_autor = ttk.Label(self.canvas, text="Desarrollado por Alexander Galvez",
                                foreground=colores.COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 10, "bold"))
        self.label_autor.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-110)

        self.label_telefono = ttk.Label(self.canvas, text="Teléfono: +34 688 872 515",
                                        foreground=colores.COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 10, "bold"))
        self.label_telefono.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-90) 

        self.label_correo = ttk.Label(self.canvas, text="Correo: alexandergalvez880208@gmail.com",
                                foreground=colores.COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 10, "bold"))
        self.label_correo.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-70)  

        self.label_cpyright = ttk.Label(self.canvas, text="© 2025 eDe-Lib. Todos los derechos reservados.",
                                        foreground=colores.COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 10, "bold"))
        self.label_cpyright.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-30) 

        btn_hover.hover_event_label(self, self.label_telefono)
        btn_hover.hover_event_label(self, self.label_correo)


