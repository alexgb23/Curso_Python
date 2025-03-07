import tkinter as tk
from tkinter import ttk
from tkinter import font
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
from modulos.metodos_basicos import *
from tkinter import messagebox
from clases.editoriales import Editoriales
from clases.autores import Autores
from modulos.metodos_basicos import *
import modulos.botones.btn_config as btn_config
import modulos.botones.btn_hover as btn_hover
import modulos.botones.definir_btns as definir_btns
import modulos.botones.btn_selected as btn_selected
import modulos.botones.btn_acciones as btn_acciones
import modulos.datos.datos_para_insertar as insert_data
import modulos.paneles.tabla as tabla
import modulos.paneles.panel_bienvenida as panel_bienvenida


class FormMaestro(tk.Tk):
    def __init__(self):
        super().__init__()

        self.configure_window() # Configuración de la ventana para que se muestre en el centro de la pantalla
        self.load_images() # Cargar las imagenes
        self.init_variables() # Inicializar las variables
        self.crear_frames() # Crear los frames que maquetan la ventana
        self.crear_menu_lateral() # Crear el menu lateral
        self.crear_barra_superior() # Crear el menu y la barra superior
        self.crear_panel_bienvenida() # Crear el panel de bienvenida


    def init_variables(self):
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
    
        
    # Configuración de la ventana para que se muestre en el centro de la pantalla
    def configure_window(self):
        util_ventana.config_window(self)

    # Cargar las imagenes
    def load_images(self):
        try:
            self.perfil = util_img.leer_imagen("image/eDe-Lib.png", (250, 250))
            self.exit = util_img.leer_imagen_con_transparencia("image/delete_exit_1195.png", (32, 32))
        except FileNotFoundError as e:
            print(f"Error: {e}")

    # Crear los frames que maquetan la ventana, el frame lateral, el frame superior y el cuerpo
    def crear_frames(self):
        self.menu_lateral = tk.Frame(self, bg=COLOR_MENU_LATERAL, width=300)
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

        self.barra_superior = tk.Frame(
            self, bg=COLOR_BARRA_SUPERIOR, height=200)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.cuerpo_principal = tk.Frame(self, bg=COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)

    # Crear el menu lateral
    def crear_menu_lateral(self):
        ancho_boton = 20 # Ancho del botóes del menu lateral
        alto_boton = 1   # Alto del botónes del menu lateral
        font_awesome = font.Font(family="FontAwesome", size=15)  # Fuente

        # label que encapsula el logo que es una imagen previamente cargada la cual es self.perfil
        self.labelLogo = tk.Label(
            self.menu_lateral, image=self.perfil, bg=COLOR_MENU_LATERAL)
        self.labelLogo.pack(side=tk.TOP, pady=10, padx=10, expand=False)

        # Crear los botones del menu lateral recorriendo la lista, aplicandoles una configuración personalizada
        # la cual se encuentra en el modulo btn_config, y luego marcar el botón Inicio con el metodo marcar_boton 
        # que se encuentra en el modulo btn_selected si el titulo del panel es Bienvenido a eDe-Lib
        # los botonres del panel lateralk tienen un comand instanciar y marcar que se encuentra en el modulo ...

        self.btn_info = definir_btns.definir_btn_menu_lateral(self) #lista de botones

        for btn in self.btn_info:
            boton = tk.Button(self.menu_lateral)
            btn_config.configuracion_btn_menu_lateral(self,
                boton, btn["text"], btn["icon"], font_awesome, ancho_boton, alto_boton, btn["activo"])
            boton.config(command=lambda b=boton,
                         btn=btn:  instanciar_y_marcar(self, b, btn))
           
            if btn["text"] == "Inicio" and not self.titulo_panel_administracion:
                btn["activo"] = True
                btn_selected.marcar_boton(self, boton, btn)
              

    def crear_barra_superior(self):
        ancho_boton = 15 # Ancho de los botónes superiores
        alto_boton = 1  # Alto de los botónes superiores
        font_awesome = font.Font(family="FontAwesome", size=12)

        #Titulo del panel superior
        self.labelTitulo = tk.Label(self.barra_superior, text="¡Bienvenido!")
        self.labelTitulo.config(fg="white", font=(
            "Time New Roman", 24, "bold"), bg=COLOR_BARRA_SUPERIOR, padx=10, pady=16)
        self.labelTitulo.pack(side=tk.LEFT, padx=15)

        #crear boton salir, el cual tiene el metodo de destruir la ventana cuando se presiona
        self.salir=tk.Button(self.barra_superior, image=self.exit )
        self.salir.pack(side=tk.RIGHT, padx=15)
        self.salir.config(command=self.destroy, bg="pink")


        # Crear los botones del menu Superior recorriendo la lista, aplicandoles una configuración personalizada
        # la cual se encuentra en el modulo btn_config, y luego marcar el botón Inicio con el metodo marcar_boton 
        # que se encuentra en el modulo btn_selected si el titulo del panel es Bienvenido a eDe-Lib
        # los botonres del panel lateralk tienen un comand instanciar y marcar que se encuentra en el modulo ...

        self.btn_info_sup = definir_btns.definir_btn_menu_superior(self) #lista de botones

        for btn in self.btn_info_sup:
            but = tk.Button(self.barra_superior)
            btn_config.configuracion_btn_menu_superior(self,
                but, btn["text"], btn["icon"], font_awesome, ancho_boton, alto_boton, btn["activo"])
            but.config(command=lambda b=but, btn=btn: acciones(
                self, b, btn))  # Asigna el comando
            
        # Configura el evento hover para el botón de salida el cual se encuentra en el modulo btn_hover    
        btn_hover.hover_event_Exit(self, self.salir)


    def crear_panel_bienvenida(self):
        panel_bienvenida.crear_panel_bienvenida(self)


    def cargarDatos(self, quepanel=None):
        # Esto lo hago para si clican en inicio al cargar el panel no se rompa el programa
        if quepanel == "Inicio" and self.titulo_panel_administracion != "Bienvenido a eDe-Lib":
            self.panel_datos.pack_forget()
            self.crear_panel_bienvenida()
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
                               command= lambda: btn_acciones.siguiente_registro(self))
            btnMas.pack(side="right", padx=20)
            btn_hover.hover_event_sup(self, btnMas)

            btnMenos = tk.Button(self.panel_cuerpo, text="Anterior", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                                 command= lambda: btn_acciones.anterior_registro(self))
            btnMenos.pack(side="right", padx=20)
            btn_hover.hover_event_sup(self, btnMenos)

            self.mostrar_registro()
            tabla.crear_tabla(self)

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
        self.panel_tabla.place(relwidth=1, height=270, y=410)

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

        btn_config.crear_boton_sub_panel(self, tipo_boton)
    

        # Forzar el ajuste del panel después de cargar los datos para que no sea visible
        self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))
      
    
    def cargarDatosParaInsertar(self, tipo_boton):
        tk.Label(self.panel_acciones_cuerpo, text=f"Panel para Insertar {self.titulo_panel_administracion}", bg=COLOR_PANEL_INFO, font=("Arial", 18, "bold")).pack(pady=5)
        self.campos_insertar = {}
        dat_filas=insert_data.datos_llenar_insertar(self, self.titulo_panel_administracion) 
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
                
        btn_config.crear_boton_sub_panel(self, tipo_boton)

        # Forzar el ajuste del panel después de cargar los datos para que no sea visible
        self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))

    """
    Metodos Necesarios dentro de la clase
    """
    # Metodo para obtener las coordenadas, tamaño y nombre de la ventana pequeña donde van los datos de la tabla, ya que esta se ajusta al contenido de la pantalla
    def posision_info(self, ventana):
        self.coordenadas = ventana.winfo_x(), ventana.winfo_y(), ventana.winfo_width(), ventana.winfo_height()

    # Metodo para la transicion entre los paneles pequeños paneles
    def transicion_paneles_if_true(self):
        if self.panel_cuerpo.winfo_y() == 70:
            transition.slide_out(self, self.panel_cuerpo)
            return
        elif self.panel_acciones_cuerpo.winfo_y() == 70:
            transition.slide_out(self, self.panel_acciones_cuerpo)
            return

    # Metodo para capturar el item seleccionado de la tabla
    def on_item_tabla_click(self, event):
        self.campo_selected_table = {}
        # Obtener el item seleccionado
        item = self.tabla.selection()
        if item:
            # Obtener los valores del item seleccionado
            self.campo_selected_table = {col: val for col, val in zip(
                self.tabla["columns"], self.tabla.item(item, "values"))}
            
    #Redimensionar la imagen de fondo del panel de bienvenida
    def redimensionar_imagen_fondo_panel_bienvenida(self, event=None):
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