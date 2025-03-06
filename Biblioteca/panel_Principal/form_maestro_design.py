import tkinter as tk
from tkinter import ttk
from tkinter import font
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from metodos_basicos.metodos_basicos import *
from clases.editoriales import Editoriales
from clases.autores import Autores


class FormMaestro(tk.Tk):
    def __init__(self):
        super().__init__()

        try:
            self.perfil = util_img.leer_imagen("image/eDe-Lib.png", (250, 250))
            self.exit= util_img.leer_imagen_con_transparencia("image/delete_exit_1195.png", (32, 32))
        except FileNotFoundError as e:
            print(f"Error: {e}")

        self.boton_activo = None  # Botón activo
        self.boton_activo_sup = None
        self.registros = []
        self.indice_actual = 0
        self.campo_selected_table = {}
        self.registros = None
        self.ancho_cuerpo = 600
        self.alto_cuerpo = 320
        self.coordenadas = None
        self.visible = True  # Estado del panel
        self.titulo_panel_administracion = None
        config_window(self)
        self.paneles()
        self.controles_menu_lateral()
        self.controles_barra_superior()
        self.crear_panel_inicio()
        

    def paneles(self):
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=300)
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=200)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)

        ## Ocultar la barra de título y los botones
        # self.cuerpo_principal.winfo_toplevel().overrideredirect(True)

     

    def crear_panel_inicio(self):
        self.titulo_panel_administracion = "Bienvenido a eDe-Lib"
        
        # Crear el panel principal
        self.panel_inicio = tk.Frame(self.cuerpo_principal, bg="white")
        self.panel_inicio.place(relwidth=1, relheight=1)

        # Crear un Canvas para la imagen de fondo
        self.canvas = tk.Canvas(self.panel_inicio, highlightthickness=0)
        self.canvas.place(relwidth=1, relheight=1)

        # Llamar a redimensionar_imagen para cargar la imagen inicialmente
        self.redimensionar_imagen()

        # Vincular el evento de redimensionamiento
        self.panel_inicio.bind("<Configure>", self.redimensionar_imagen)

        # Crear el Label con texto
        self.label_inicio = ttk.Label(self.canvas, text=self.titulo_panel_administracion,
                                    foreground=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 36, "bold"))
        self.label_inicio.place(relx=0.5, y=15, anchor="n")

        self.label_info= ttk.Label(self.canvas, text="Plataforma de gestión de bibliotecas",
                                    foreground=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 16, "bold"))
        self.label_info.place(relx=0.5, y=80, anchor="n")

    def redimensionar_imagen(self, event=None):
        width = self.panel_inicio.winfo_width()
        height = self.panel_inicio.winfo_height()

        # Configurar la imagen de fondo en el Canvas
        self.foto_fondo = util_img.leer_imagen("image/muebles-bibliotecas-estanteria-etiquetada.webp", (width, height))
        

     # Limpiar el Canvas antes de agregar la nueva imagen
        self.canvas.delete("all")

    # Configurar la imagen de fondo en el Canvas
        self.canvas.create_image(0, 0, anchor="nw", image=self.foto_fondo)

    # Mantener la referencia de la imagen
        self.canvas.image = self.foto_fondo


    def controles_barra_superior(self):
        ancho_op = 15
        alto_op = 1
        font_awesome = font.Font(family="FontAwesome", size=12)

        self.labelTitulo = tk.Label(self.barra_superior, text="¡Bienvenido!")
        self.labelTitulo.config(fg="white", font=(
            "Time New Roman", 24, "bold"), bg=COLOR_BARRA_SUPERIOR, padx=10, pady=16)
        self.labelTitulo.pack(side=tk.LEFT, padx=15)

        self.salir=tk.Button(self.barra_superior, image=self.exit )
        self.salir.pack(side=tk.RIGHT, padx=15)
        self.salir.config(command=self.destroy, bg="pink")


        self.btn_info_sup = [  # Inicializa la lista de botones superiores
            {"text": "Actualizar", "icon": "\uf021", "activo": False},
            {"text": "Eliminar", "icon": "\uf2ed", "activo": False},
            {"text": "Insertar", "icon": "\uf067", "activo": False},
            {"text": "Buscar", "icon": "\uf002", "activo": False},
        ]

        for btn in self.btn_info_sup:
            but = tk.Button(self.barra_superior)
            self.configurar_btn_superior(
                but, btn["text"], btn["icon"], font_awesome, ancho_op, alto_op, btn["activo"])
            but.config(command=lambda b=but, btn=btn: acciones(
                self, b, btn))  # Asigna el comando
            
        hover_event_Exit(self, self.salir)

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
        boton.pack(side=tk.RIGHT, padx=15)
        hover_event_sup(self, boton)

    def controles_menu_lateral(self):
        ancho_menu = 20
        alto_menu = 1
        font_awesome = font.Font(family="FontAwesome", size=15)

        self.labelLogo = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
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
            self.configurar_btn_menu(
                boton, btn["text"], btn["icon"], font_awesome, ancho_menu, alto_menu, btn["activo"])
            boton.config(command=lambda b=boton,
                         btn=btn:  instanciar_y_marcar(self, b, btn))
           
            if btn["text"] == "Inicio" and not self.titulo_panel_administracion:
                btn["activo"] = True
                marcar_boton(self, boton, btn)
              
                
            

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
            hover_event(self, boton)
        else:
            self.boton_activo = boton


    def cargarDatos(self, quepanel=None):
        # Esto lo hago para si clican en inicio al cargar el panel no se rompa el programa
        if quepanel == "Inicio" and self.titulo_panel_administracion != "Bienvenido a eDe-Lib":
            self.panel_datos.pack_forget()
            self.crear_panel_inicio()
        elif quepanel == "Inicio" and self.titulo_panel_administracion == "Bienvenido a eDe-Lib":
            return
        else:
            self.panel_inicio.pack_forget()
            self.creacion_cuerpo_datos()

            self.campos = {}
            self.columnas = list(self.registros[0].keys())
              # Diccionario para mapear columnas a sus etiquetas
            etiquetas = {
            "anio": "Año"
            }
            
            for columna in self.columnas:
                # Contenedor de cada fila (etiqueta + campo)
                frame_fila = tk.Frame(self.panel_cuerpo, bg=COLOR_PANEL_INFO)
                frame_fila.pack(pady=10, fill="x")

                 # Obtener la etiqueta correspondiente, o usar la columna en sí
                texto_label = etiquetas.get(columna, columna.title())
              
                self.label = tk.Label(frame_fila, text=texto_label, width=15,
                        anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
                
                self.campos[columna] = ttk.Entry(
                    frame_fila, font=("Arial", 14, "bold"))
                self.campos[columna].pack(
                    side="left", expand=True, fill="x", padx=15)
            
                 
            btnMas = tk.Button(self.panel_cuerpo, text="Siguiente", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                               command=self.siguiente_registro)
            btnMas.pack(side="right", padx=20)
            hover_event_sup(self, btnMas)

            btnMenos = tk.Button(self.panel_cuerpo, text="Anterior", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                                 command=self.anterior_registro)
            btnMenos.pack(side="right", padx=20)
            hover_event_sup(self, btnMenos)


            self.mostrar_registro()
            self.crear_tabla()

    def mostrar_registro(self):
        """ Muestra el registro actual en los campos de texto """
        if not self.registros:
            return

        registro_actual = self.registros[self.indice_actual]

        for columna, campo in self.campos.items():
            campo.config(state="normal")
            campo.delete(0, tk.END)
            campo.insert(0, registro_actual[columna])
            campo.config(state="readonly")

            


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



    def creacion_cuerpo_datos(self):
        self.panel_datos = tk.Frame(
            self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.panel_datos.place(relwidth=1, relheight=1)

        self.panel_cuerpo = tk.Frame(self.panel_datos, bg=COLOR_PANEL_INFO)

        # Función para centrar el panel_cuerpo
        def ajustar_panel():
            x, y = util_ventana.centrar_panel(
                self.panel_datos, self.ancho_cuerpo, self.alto_cuerpo)

            self.panel_cuerpo.place(
                width=self.ancho_cuerpo, height=self.alto_cuerpo, x=x, y=y)
            
            self.coordenadas = [x, y, self.ancho_cuerpo, self.alto_cuerpo]
            

        # Llama a ajustar_panel al configurar panel_datos
        self.panel_datos.bind("<Configure>", lambda event: ajustar_panel())

        tk.Label(self.panel_datos, text=f"Panel de Administración de {self.titulo_panel_administracion}",
                bg=COLOR_CUERPO_PRINCIPAL, fg=COLOR_BARRA_SUPERIOR, font=("Arial", 30, "bold")).place(relx=0.5, y=10, anchor="n")

        # Crear panel para la tabla
        self.panel_tabla = tk.Frame(self.panel_datos, bg="#FFFFFF")
        self.panel_tabla.place(relwidth=1, height=250, y=410)

        ajustar_panel()


    def creacion_acciones_cuerpo_datos(self, tipo_boton):
        # Crear el panel cuerpo dentro de panel_datos
        self.panel_acciones_cuerpo = tk.Frame(
            self.panel_datos, bg=COLOR_PANEL_INFO)

        def ajustar_panel():
            x, y = util_ventana.centrar_panel(
                self.panel_datos, self.ancho_cuerpo, self.alto_cuerpo)
            self.panel_acciones_cuerpo.place(
                width=self.ancho_cuerpo, height=self.alto_cuerpo, x=x, y=-400)
                
        self.panel_cuerpo.bind("<Configure>", lambda event: ajustar_panel())
        
        ajustar_panel()

        if tipo_boton == "Insertar":
        
            self.cargarDatosParaInsertar(tipo_boton)
        else:    
            self.cargarDatosParaActualizar(tipo_boton)


    def cargarDatosParaActualizar(self, tipo_boton):        
        tk.Label(self.panel_acciones_cuerpo, text=f"Panel para Actualizar {self.titulo_panel_administracion}", bg=COLOR_PANEL_INFO, font=("Arial", 18, "bold")).pack(pady=5)
        self.campos_actualizar = {}
        if self.titulo_panel_administracion == "Libros":
            crear_cuerpo_actualizar_libros(self, self.campo_selected_table)
        elif self.titulo_panel_administracion == "Autor-Libro":
            crear_cuerpo_actualizar_autor_libro(self, self.campo_selected_table)
        else:
           for columna, value in self.campo_selected_table.items():
            frame_fila = tk.Frame(
                self.panel_acciones_cuerpo, bg=COLOR_PANEL_INFO)
            frame_fila.pack(pady=10, fill="x")
            tk.Label(frame_fila, text=columna, width=15,
                     anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
            self.campos_actualizar[columna] = tk.Entry(
                frame_fila, font=("Arial", 14, "bold"))
            self.campos_actualizar[columna].insert(0, value)
            self.campos_actualizar[columna].pack(
                side="left", expand=True, fill="x", padx=15)

            if columna == "id":
                self.campos_actualizar[columna].config(state="readonly", fg="darkgrey")

        crear_boton_sub_panel(self, tipo_boton)
    

        # Forzar el ajuste del panel después de cargar los datos para que no sea visible
        self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))
      
    
    def cargarDatosParaInsertar(self, tipo_boton):
        tk.Label(self.panel_acciones_cuerpo, text=f"Panel para Insertar {self.titulo_panel_administracion}", bg=COLOR_PANEL_INFO, font=("Arial", 18, "bold")).pack(pady=5)
        self.campos_insertar = {}
        dat_filas=datos_llenar_insertar(self, self.titulo_panel_administracion) 
        if "titulo" and "año" and "autor" and "editorial" in dat_filas:
            crear_cuerpo_insertar_libros(self,dat_filas)
        elif "libro" and "autor" in dat_filas:
            crear_cuerpo_insertar_autor_libro(self,dat_filas)
        else:
            for columna in dat_filas:
                frame_fila = tk.Frame(
                    self.panel_acciones_cuerpo, bg=COLOR_PANEL_INFO)
                frame_fila.pack(pady=10, fill="x")
                tk.Label(frame_fila, text=columna, width=15,
                        anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)
                self.campos_insertar[columna] = tk.Entry(
                        frame_fila, font=("Arial", 14, "bold"))
                self.campos_insertar[columna].pack(
                        side="left", expand=True, fill="x", padx=15)
                
        crear_boton_sub_panel(self, tipo_boton)

        # Forzar el ajuste del panel después de cargar los datos para que no sea visible
        self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))
      

    """Creacion de la Tabla"""
    def crear_tabla(self):
        print(len(self.registros)) 
        self.columnas = list(self.registros[0].keys())

        # Crear un estilo para la tabla
        style = ttk.Style()
        style.configure("Heading", background=COLOR_CABECERA_TABLA)
        style.configure("Treeview.Heading", font=(
            "Arial", 14, "bold"))  # Cabeceras en 14 bold
        style.configure("Treeview", font=("Arial", 12),
                        background=COLOR_PANEL_INFO)  # Contenido en 12

        # Crear la tabla
        self.tabla = ttk.Treeview(
            self.panel_tabla, columns=self.columnas, show="headings", style="Treeview")

        # Configurar las cabeceras de la tabla
        for col in self.columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=200)

        # Insertar los datos en la tabla
        for registro in self.registros:
            self.tabla.insert("", "end", values=[
                              registro[col] for col in self.columnas])

        # Opcional: Agregar una barra de desplazamiento
        scrollbar = tk.Scrollbar(
            self.panel_tabla, orient="vertical", command=self.tabla.yview)
        self.tabla.configure(yscroll=scrollbar.set)

        # Usar grid para la tabla y el scrollbar
        self.tabla.grid(row=0, column=0, columnspan=4, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        # Configurar la expansión del grid
        self.panel_tabla.grid_rowconfigure(0, weight=1)
        self.panel_tabla.grid_columnconfigure(0, weight=1)

        # Asociar el evento de clic a la tabla
        self.tabla.bind("<ButtonRelease-1>", self.on_item_tabla_click)

    def on_item_tabla_click(self, event):
        self.campo_selected_table = {}
        # Obtener el item seleccionado
        item = self.tabla.selection()
        if item:
            # Obtener los valores del item seleccionado
            self.campo_selected_table = {col: val for col, val in zip(
                self.tabla["columns"], self.tabla.item(item, "values"))}

    """
    Metodos Necesarios dentro del codigo
    """
# Metodo para obtener las coordenadas, tamaño y nombre de la ventana pequeña donde van los datos de la tabla, ya que esta se ajusta al contenido de la pantalla
    def posision_info(self, ventana):
        self.coordenadas = ventana.winfo_x(), ventana.winfo_y(), ventana.winfo_width(), ventana.winfo_height()

# Metodo para la transicion entre los paneles pequeños paneles
    def transicion_paneles_if_true(self):
        if self.panel_cuerpo.winfo_y() == 70:
            slide_out(self, self.panel_cuerpo)
            return
        elif self.panel_acciones_cuerpo.winfo_y() == 70:
            slide_out(self, self.panel_acciones_cuerpo)
            return