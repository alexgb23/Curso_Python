import tkinter as tk
from tkinter import font
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_BTN
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from clases.libros import Libros
from clases.autores import Autores
from clases.editoriales import Editoriales
from clases.autorlibro import AutorLibro



class FormMaestro(tk.Tk):
    def __init__(self):
        super().__init__()
        try:
            self.perfil = util_img.leer_imagen("image/eDe-Lib.png", (250, 250))
        except FileNotFoundError as e:
            print(f"Error: {e}")
        
        self.boton_activo = None  # Botón activo
        self.boton_activo_sup = None
        self.registros = []
        self.indice_actual = 0
        self.registros = None
        self.titulo="Bienvenido a eDe-Lib"
        self.config_window()
        self.paneles()
        self.panelInicio()
        self.controles_barra_superior()
        self.controles_menu_lateral()

    
    def config_window(self):
        self.title("eDe-Lib")
        self.iconbitmap("./image/books.ico")
        w, h = 1360, 768
        self.geometry("%dx%d+0+0" % (w, h))
        util_ventana.centrar_ventana(self, w, h)

    def paneles(self):
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=300)
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

        self.barra_superior = tk.Frame(self, bg=COLOR_BARRA_SUPERIOR, height=200)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)

        self.panel_datos = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.panel_datos.pack(side=tk.TOP, fill="both", expand=True)

    def controles_barra_superior(self):
        ancho_op = 15
        alto_op = 1
        font_awesome = font.Font(family="FontAwesome", size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="¡Bienvenido!")
        self.labelTitulo.config(fg="white", font=("Time New Roman", 24, "bold"), bg=COLOR_BARRA_SUPERIOR, padx=10, pady=16)
        self.labelTitulo.pack(side=tk.LEFT, padx=15)

        self.btn_info_sup = [  # Inicializa la lista de botones superiores
            {"text": "Actualizar", "icon": "\uf021", "activo": False},
            {"text": "Eliminar", "icon": "\uf2ed", "activo": False},
            {"text": "Insertar", "icon": "\uf067", "activo": False},
            {"text": "Buscar", "icon": "\uf002", "activo": False},
            {"text": "Prueba", "icon": "\uf0f6", "activo": False},
        ]

        for btn in self.btn_info_sup:
            but = tk.Button(self.barra_superior)
            self.configurar_btn_superior(but, btn["text"], btn["icon"], font_awesome, ancho_op, alto_op, btn["activo"])
            but.config(command=lambda b=but, btn=btn: self.acciones(b, btn))  # Asigna el comando
            self.hover_event_sup(but)

    def acciones(self, buton, btn_info_sup):
        self.marcar_boton_sup(buton, btn_info_sup)
        if btn_info_sup["text"] == "Prueba":
            print(btn_info_sup["text"])
            self.toogle()

        

    def configurar_btn_superior(self, boton, text, icono, font_awesome, ancho_op, alto_op, activo):
        boton.config(
            text=f" {icono}  {text}",
            anchor="w",
            font=font_awesome,
            width=ancho_op,
            height=alto_op,
            pady=5,
            bg=COLOR_BTN,
            fg="white",
            bd=1,
            relief="raised",
            highlightbackground=COLOR_BARRA_SUPERIOR,
            highlightcolor=COLOR_BARRA_SUPERIOR,
            highlightthickness=2
        )
        boton.pack(side=tk.RIGHT, padx=10)



    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 1
        font_awesome = font.Font(family="FontAwesome", size=15)

        self.labelLogo = tk.Label(self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)  
        self.labelLogo.pack(side=tk.TOP, pady=10, padx=10, expand=False)

        # Agregar estado activo a cada botón
        self.btn_info = [
            {"text": "Inicio", "icon": "\uf0e4", "activo": False},
            {"text": "Libros", "icon": "\uf0f6", "activo": False},
            {"text": "Autores", "icon": "\uf0f6", "activo": False},
            {"text": "Editoriales", "icon": "\uf0f6", "activo": False},
            {"text": "Usuarios", "icon": "\uf0f6", "activo": False},
            {"text": "Crear Tabla", "icon": "\uf0f6", "activo": False},
            {"text": "Autor-Libro", "icon": "\uf0f6", "activo": False},
        ]
        
     

                
        for btn in self.btn_info:
            boton = tk.Button(self.menu_lateral)
            self.configurar_btn_menu(boton, btn["text"], btn["icon"], font_awesome, ancho_menu, alto_menu, btn["activo"])
            boton.config(command=lambda b=boton, btn=btn: self.instanciar_y_marcar(b, btn))

    def instanciar_y_marcar(self, boton, btn_info):
        # Llama a los métodos deseados
        self.marcar_boton(boton, btn_info)  # Marca el botón
        self.instanciar(btn_info["text"])   # Llama a instanciar  

    def configurar_btn_menu(self, boton, text, icono, font_awesome, ancho_menu, alto_menu, activo):
        boton.config(
            text=f" {icono}  {text}",
            anchor="w",
            font=font_awesome,
            width=ancho_menu,
            height=alto_menu,
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
            self.hover_event(boton)
        else:
            self.boton_activo = boton

    def panelInicio(self):
        label_cuerpo = tk.Label(self.cuerpo_principal, text=self.titulo, bg=COLOR_CUERPO_PRINCIPAL, fg="red", font=("Arial", 36, "bold"))
        label_cuerpo.place(x=0, y=150, relwidth=1, relheight=0.1)

        self.panel_cuerpo = tk.Frame(self.cuerpo_principal, bg="gray", width=100, height=100)
        self.panel_cuerpo.pack(side=tk.TOP, fill="both", expand=False)


    def marcar_boton(self, boton, btn_info):
        # Si hay un botón activo, restaurar su color
        if self.boton_activo:
            self.boton_activo.config(bg=COLOR_BTN)  # Restaura el color original
            # Actualiza el estado del botón anterior
            for btn in self.btn_info:
                if btn["text"] == self.boton_activo.cget("text").strip():
                    btn["activo"] = False

        # Marca el botón seleccionado
        boton.config(bg=COLOR_MENU_CURSOR_ENCIMA)  # Cambia el color del botón activo
        self.boton_activo = boton  # Actualiza el botón activo
        # Actualiza el estado del botón actual
        btn_info["activo"] = True
        print(boton, btn_info)

    def marcar_boton_sup(self, buton, btn_info_sup):
        # Si hay un botón activo, restaurar su color
        if self.boton_activo_sup:
            self.boton_activo_sup.config(bg=COLOR_BTN)  # Restaura el color original
            # Actualiza el estado del botón anterior
            for btn in self.btn_info:  # Usa self.btn_info_sup aquí
                if btn["text"] == self.boton_activo_sup.cget("text").strip():
                    btn["activo"] = False
                    

        # Marca el botón seleccionado
        buton.config(bg=COLOR_MENU_CURSOR_ENCIMA)  # Cambia el color del botón activo
        self.boton_activo_sup = buton  # Actualiza el botón activo
        # Actualiza el estado del botón actual
        btn_info_sup["activo"] = True


    def hover_event(self, boton):
        # Verifica si el botón es el activo para aplicar hover
        def on_enter(e):
            if self.boton_activo != boton:  # Evita hover en el botón activo
                boton.config(bg=COLOR_MENU_CURSOR_ENCIMA, cursor="hand2", fg="white")

        def on_leave(e):
            if self.boton_activo != boton:  # Evita restaurar en el botón activo
                boton.config(bg=COLOR_BTN, fg="white")

        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

    def hover_event_sup(self, boton_sup):
        # Verifica si el botón es el activo para aplicar hover
        def on_enter(e):
            if self.boton_activo_sup != boton_sup:  # Evita hover en el botón activo
                boton_sup.config(bg=COLOR_MENU_CURSOR_ENCIMA, cursor="hand2", fg="white")

        def on_leave(e):
            if self.boton_activo_sup != boton_sup:  # Evita restaurar en el botón activo
                boton_sup.config(bg=COLOR_BTN, fg="white")

        boton_sup.bind("<Enter>", on_enter)
        boton_sup.bind("<Leave>", on_leave)

    def instanciar(self, clase):
        if clase == "Libros":
            libros=Libros()
            self.registros = libros.libros_con_autor_y_editorial
            self.indice_actual = 0
            self.cargarDatos()
        elif clase == "Autores":
            autores=Autores()
            self.registros = autores.autores
            self.indice_actual = 0
            self.cargarDatos()
        elif clase == "Editoriales":
            editoriales=Editoriales()
            self.registros = editoriales.editoriales
            self.indice_actual = 0
            self.cargarDatos()
        elif clase == "Autor-Libro":
            autorlibro=AutorLibro()
            self.registros = autorlibro.autorlibro
            self.indice_actual = 0
            self.cargarDatos()
        elif clase == "Inicio":
            self.cargarDatos("Inicio")
        else:
            print("No se encontró la clase")
    
    def toogle(self):
        if self.panel_cuerpo.winfo_ismapped():
            self.panel_cuerpo.pack_forget()
        else:
            self.panel_cuerpo.pack(side=tk.TOP, fill="x")


    def cargarDatos(self, quepanel=None):
        self.panel_datos.destroy()
        self.panel_cuerpo.destroy()
        if quepanel == "Inicio":
            self.panelInicio()
        else:
            self.panel_datos = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
            self.panel_datos.pack(side=tk.TOP, fill="both", expand=True)

            self.campos = {}
            self.columnas = list(self.registros[0].keys())

            for columna in self.columnas:
                # Contenedor de cada fila (etiqueta + campo)
                frame_fila = tk.Frame(self.panel_datos)
                frame_fila.pack(pady=5, fill="x")
                if columna.lower() != "id":
                    col = columna

                    tk.Label(frame_fila, text=col, width=15,
                              anchor="w").pack(side="left", padx=5)

                    self.campos[col] = tk.Entry(frame_fila)
                    self.campos[col].pack(side="left", expand=True, fill="x")
                    print (frame_fila)


            self.mostrar_registro()

            btnMenos= tk.Button(self.panel_datos, text="Anterior", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                command=self.anterior_registro)
            btnMenos.pack(side="left", padx=20)
            self.hover_event(btnMenos)

            btnMas=tk.Button(self.panel_datos, text="Siguiente", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                command=self.siguiente_registro)
            btnMas.pack(side="left", padx=20)
            self.hover_event(btnMas)


    def mostrar_registro(self):
        """ Muestra el registro actual en los campos de texto """
        if not self.registros:
            return
        
        registro_actual = self.registros[self.indice_actual]
    
        for columna, campo in self.campos.items():
            campo.delete(0, tk.END)
            campo.insert(0, registro_actual[columna])

    def siguiente_registro(self):
        """ Muestra el siguiente registro """
        if self.indice_actual < len(self.registros) - 1:
            self.indice_actual += 1
            self.mostrar_registro()

    def anterior_registro(self):
        """ Muestra el registro anterior """
        if self.indice_actual > 0:
            self.indice_actual -= 1
            self.mostrar_registro()