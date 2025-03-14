import tkinter as tk
from tkinter import ttk
import util.util_ventana as util_ventana
import util.util_imagenes as util_img
import config.config as colores
import modulos.botones.btn_config as btn_config
import modulos.botones.btn_hover as btn_hover
import modulos.datos.definir_btns as definir_btns
import modulos.botones.btn_selected as btn_selected
import modulos.paneles.panel_bienvenida as panel_bienvenida
import modulos.paneles.subpanel_actualizar as cargarPanelActualizar
import modulos.paneles.subpanel_insertar as cargarPanelInsertar
import modulos.efectos_visuales.transisiones as transition
import modulos.ejecucion_click.click_btn_menu_lateral as click_btn_menu_lateral
import modulos.ejecucion_click.click_btn_menu_sup as click_btn_menu_sup
import modulos.paneles.subpanel_buscar as subpanel_buscar





class FormMaestro(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure_window()  # Configuración de la ventana para que se muestre en el centro de la pantalla
        self.load_images()  # Cargar las imagenes
        self.init_variables()  # Inicializar las variables
        self.crear_frames()  # Crear los frames que maquetan la ventana
        self.crear_menu_lateral()  # Crear el menu lateral
        self.crear_barra_superior()  # Crear el menu y la barra superior
        self.crear_panel_bienvenida()  # Crear el panel de bienvenida

    def init_variables(self):
        self.boton_activo = None  # Botón activo
        self.boton_activo_sup = None
        self.registros = []
        self.indice_actual = 0
        self.campo_selected_table = {}
        self.registros = None
        self.reg_busqueda=[]
        self.ancho_cuerpo = 600
        self.alto_cuerpo = 320
        self.coordenadas = None
        self.visible = True  # Estado del panel
        self.titulo_panel_administracion = None
        self.tit_panel_actualizar= None
        self.contador_filas = 0
        self.contador_columnas = 0

    # Configuración de la ventana para que se muestre en el centro de la pantalla
    def configure_window(self):
        util_ventana.config_window(self)

    # Cargar las imagenes
    def load_images(self):
        try:
            self.perfil = util_img.leer_imagen("image/eDe-Lib.png", (250, 250))
            self.exit = util_img.leer_imagen_con_transparencia("image/delete_exit_1195.png", (32, 32))
            self.exit2 = util_img.leer_imagen_con_transparencia("image/exit2.png", (32, 32))
            self.max = util_img.leer_imagen_con_transparencia("image/icons8-minimizar-64.png", (32, 32))
            self.maxmax= util_img.leer_imagen_con_transparencia("image/icons8-expandir-50.png", (32, 32))
            self.min = util_img.leer_imagen_con_transparencia("image/minimizar.png", (32, 32))
            self.min2 = util_img.leer_imagen_con_transparencia("image/minimizar2.png", (32, 32))
            self.lupa = util_img.leer_imagen_con_transparencia("image/glass-2025715_640.png", (64, 64))
        except FileNotFoundError as e:
            print(f"Error: {e}")

    # Crear los frames que maquetan la ventana, el frame lateral, el frame superior y el cuerpo
    def crear_frames(self):
        self.menu_lateral = tk.Frame(self, bg=colores.COLOR_MENU_LATERAL, width=300)
        self.menu_lateral.pack(side=tk.LEFT, fill=tk.Y)

        self.barra_superior = tk.Frame(self, bg=colores.COLOR_BARRA_SUPERIOR, height=200)
        self.barra_superior.pack(side=tk.TOP, fill=tk.X)

        self.cuerpo_principal = tk.Frame(self, bg=colores.COLOR_CUERPO_PRINCIPAL)
        self.cuerpo_principal.pack(side=tk.RIGHT, fill="both", expand=True)

    # Crear el menu lateral
    def crear_menu_lateral(self):
        # label que encapsula el logo que es una imagen previamente cargada la cual es self.perfil
        self.labelLogo = tk.Label(self.menu_lateral, image=self.perfil, bg=colores.COLOR_MENU_LATERAL)
        self.labelLogo.pack(side=tk.TOP, pady=10, padx=10, expand=False)

        # Crear los botones del menu lateral recorriendo la lista, aplicandoles una configuración personalizada
        self.btn_info = definir_btns.definir_btn_menu_lateral(self)  # lista de botones

        for btn in self.btn_info:
            boton = tk.Button(self.menu_lateral)
            btn_config.configuracion_btn_menu_lateral(self, boton, btn["text"], btn["icon"], btn["activo"])
            boton.config(command=lambda b=boton, btn=btn: click_btn_menu_lateral.instanciar_y_marcar(self, b, btn))

            # Marcar el botón Inicio cuando carga el programa tpmndo como parametro si el titulo del panel es Bienvenido a eDe-Lib
            if btn["text"] == "Inicio" and not self.titulo_panel_administracion:
                btn["activo"] = True
                btn_selected.marcar_boton(self, boton, btn)

    def crear_barra_superior(self):
        # Titulo del panel superior
        self.labelTitulo = tk.Label(self.barra_superior, text="¡Bienvenido!")
        self.labelTitulo.config(fg="white", font=("Time New Roman", 24, "bold"), bg=colores.COLOR_BARRA_SUPERIOR, padx=10, pady=16)
        self.labelTitulo.pack(side=tk.LEFT, padx=15)

        #Botones de comando
        # crear boton salir, el cual tiene el metodo de destruir la ventana cuando se presiona
        self.salir = tk.Button(self.barra_superior, image=self.exit)
        self.salir.pack(side=tk.RIGHT)
        self.salir.config(command=self.destroy, bg=colores.COLOR_BARRA_SUPERIOR, bd=0)

        self.maximizar = tk.Button(self.barra_superior)
        self.maximizar.pack(side=tk.RIGHT)
        self.maximizar.config(command=self.maximizar_ventana, bg=colores.COLOR_BARRA_SUPERIOR, bd=0, image=self.maxmax if self.winfo_toplevel().state() == "zoomed" and self.winfo_toplevel().overrideredirect()
        else self.maximizar.config(image=self.max))


        self.minimizar = tk.Button(self.barra_superior, image=self.min)
        self.minimizar.pack(side=tk.RIGHT)
        self.minimizar.config(command=self.minimizar_ventana, bg=colores.COLOR_BARRA_SUPERIOR, bd=0)
      
        # Crear los botones del menu Superior recorriendo la lista, aplicandoles una configuración personalizada
        self.btn_info_sup = definir_btns.definir_btn_menu_superior(self)  # lista de botones

        for btn in self.btn_info_sup:
            but = tk.Button(self.barra_superior)
            btn_config.configuracion_btn_menu_superior(self, but, btn["text"], btn["icon"], btn["activo"])
            but.config(command=lambda b=but, btn=btn: click_btn_menu_sup.acciones(self, b, btn))  # Asigna el comando


        # Configura el evento hover para el botón de salida el cual se encuentra en el modulo btn_hover    
        btn_hover.hover_event_Exit(self, self.salir)
        btn_hover.hover_event_minimizar(self, self.minimizar)
        btn_hover.hover_event_maximizar(self, self.maximizar)


    def crear_panel_bienvenida(self):
        panel_bienvenida.crear_panel_bienvenida(self)



    def maximizar_ventana(self):
        if self.winfo_toplevel().state() == "zoomed" and self.winfo_toplevel().overrideredirect():
            self.winfo_toplevel().state("normal")
            self.winfo_toplevel().overrideredirect(False)
            self.configure_window()
            return
        else:
            self.winfo_toplevel().state("zoomed")
            self.winfo_toplevel().overrideredirect(True)

    def minimizar_ventana(self):
        self.winfo_toplevel().state("icon")


    def creacion_cuerpo_datos(self):
        self.panel_datos = tk.Frame(self.cuerpo_principal, bg=colores.COLOR_CUERPO_PRINCIPAL)
        self.panel_datos.place(relwidth=1, relheight=1)
        
        self.panel_cuerpo = tk.Frame(self.panel_datos, bg=colores.COLOR_PANEL_INFO)

        # Metodo para centrar el panel_cuerpo
        def ajustar_panel():
            x, y = util_ventana.centrar_panel(self.panel_datos, self.ancho_cuerpo, self.alto_cuerpo)
            self.panel_cuerpo.place(width=self.ancho_cuerpo, height=self.alto_cuerpo, x=x, y=y)
            self.coordenadas = [x, y, self.ancho_cuerpo, self.alto_cuerpo]

        # Llama a ajustar_panel al configurar panel_datos
        self.panel_datos.bind("<Configure>", lambda event: ajustar_panel())

        tk.Label(self.panel_datos, text=f"Panel de Administración de {self.titulo_panel_administracion}",
                 bg=colores.COLOR_CUERPO_PRINCIPAL, fg=colores.COLOR_BARRA_SUPERIOR, font=("Arial", 30, "bold")).place(relx=0.5, y=10, anchor="n")

        # Crear panel para la tabla
        self.panel_tabla = tk.Frame(self.panel_datos, bg="#FFFFFF")
        self.panel_tabla.place(relwidth=1, height=270, y=410)

        ajustar_panel()


    def creacion_acciones_cuerpo_datos(self, tipo_boton):
        # Crear el panel cuerpo dentro de panel_datos
        self.panel_acciones_cuerpo = tk.Frame(self.panel_datos, bg=colores.COLOR_PANEL_INFO)

        def ajustar_panel():
            x, y = util_ventana.centrar_panel(self.panel_datos, self.ancho_cuerpo, self.alto_cuerpo)
            self.panel_acciones_cuerpo.place(width=self.ancho_cuerpo, height=self.alto_cuerpo, x=x, y=-400)

        self.panel_cuerpo.bind("<Configure>", lambda event: ajustar_panel())
        ajustar_panel()

        if tipo_boton == "Insertar":
            cargarPanelInsertar.cargarDatosParaInsertar(self, tipo_boton)
        elif tipo_boton == "Buscar":
            subpanel_buscar.creacion_penel_buscar(self, tipo_boton)
        else:
            cargarPanelActualizar.cargarDatosParaActualizar(self, tipo_boton)

    """
    Metodos Necesarios dentro de la clase
    """
    # # Metodo para obtener las coordenadas, tamaño y nombre de la ventana pequeña donde van los datos de la tabla, ya que esta se ajusta al contenido de la pantalla
    # def posision_info(self, ventana):
    #     self.coordenadas = ventana.winfo_x(), ventana.winfo_y(), ventana.winfo_width(), ventana.winfo_height()

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
            self.campo_selected_table = {col: val for col, val in zip(self.tabla["columns"], self.tabla.item(item, "values"))}
            print(self.campo_selected_table)
        if item and self.tit_panel_actualizar == "Panel para Actualizar":
        # Cambiar los campos de entrada con los valores del item seleccionado 
            cargarPanelActualizar.actualizar_campos_actualizar(self,self.campo_selected_table)


    # Metodo de redimensionamiento de imagen de fondo del panel de Bienvenida
    # necesario en esta clase para que funcione
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


        
