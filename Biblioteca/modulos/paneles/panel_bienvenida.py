from panel_Principal.form_maestro_design import *

def crear_panel_bienvenida(self):
        self.titulo_panel_administracion = "Bienvenido a eDe-Lib"
        
        # Crear el panel principal
        self.panel_inicio = tk.Frame(self.cuerpo_principal, bg="white")
        self.panel_inicio.place(relwidth=1, relheight=1)

        # Crear un Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.panel_inicio, highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)

        # Llamar a redimensionar_imagen para cargar la imagen inicialmente
        self.redimensionar_imagen_fondo_panel_bienvenida()

        # Vincular el evento de redimensionamiento 
        self.panel_inicio.bind("<Configure>", self.redimensionar_imagen_fondo_panel_bienvenida)

        # Crear el Label con texto
        self.label_inicio = ttk.Label(self.canvas, text=self.titulo_panel_administracion,
                                    foreground=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 36, "bold"))
        self.label_inicio.place(relx=0.5, y=15, anchor="n")

        self.label_info= ttk.Label(self.canvas, text="Plataforma de gestión de bibliotecas",
                                    foreground=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 16, "bold"))
        self.label_info.place(relx=0.5, y=80, anchor="n")

    #Metodo de redimensionamiento de imagen de fondo del panel de Biencenida
    #necesario en esta clase para que funcione
