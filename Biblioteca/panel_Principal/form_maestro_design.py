import tkinter as tk
from tkinter import ttk 
from tkinter import font
from config.config import COLOR_BARRA_SUPERIOR, COLOR_MENU_LATERAL, COLOR_CUERPO_PRINCIPAL, COLOR_MENU_CURSOR_ENCIMA, COLOR_PANEL_INFO, COLOR_CABECERA_TABLA, COLOR_BTN
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
        self.ventanas = {}
        self.indice_actual = 0
        self.registros = None
        self.visible = True  # Estado del panel
        self.titulo_panel_administracion = None
        self.titulo="Bienvenido a eDe-Lib"
        self.config_window()
        self.paneles()
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

        self.crear_panel_inicio()


    def crear_panel_inicio(self):
        self.panel_inicio = tk.Frame(self.cuerpo_principal, bg="white", width=100, height=100)
        self.panel_inicio.place(relwidth=1, relheight=1)

        self.label_inicio = tk.Label(self.panel_inicio, text=self.titulo, bg="gray", fg=COLOR_MENU_CURSOR_ENCIMA, font=("Arial", 36, "bold"))
        self.label_inicio.place(relx=0.5, y=10, anchor="n" )



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
        if btn_info_sup["text"] == "Prueba":
            self.slide_in(self.panel_cuerpo)
        elif btn_info_sup["text"] == "Actualizar":
            self.slide_out(self.panel_cuerpo)
            self.creacion_acciones_cuerpo_datos()
            self.slide_in(self.panel_acciones_cuerpo)
            if self.titulo_panel_administracion == "Libros":
                print(self.item_values_selected_tabla)
            elif self.titulo_panel_administracion == "Autores":
                print(self.item_values_selected_tabla)
            elif self.titulo_panel_administracion == "Editoriales":
                print(self.item_values_selected_tabla)
            elif self.titulo_panel_administracion == "Autor-Libro":
                print(self.item_values_selected_tabla)
        
        

        

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
            try:
                libros=Libros()
                self.registros = libros.libros
                self.indice_actual = 0
                self.titulo_panel_administracion="Libros"
                self.cargarDatos()
            except Exception as e:
                print(f"Error al instanciar libros: {e}")           
        elif clase == "Autores":
            try:
                autores=Autores()
                self.registros = autores.autores
                self.indice_actual = 0
                self.titulo_panel_administracion="Autores"
                self.cargarDatos()
            except Exception as e:
                print(f"Error al instanciar autores: {e}")
        elif clase == "Editoriales":
            try:
                editoriales=Editoriales()
                self.registros = editoriales.editoriales
                self.indice_actual = 0
                self.titulo_panel_administracion="Editoriales"
                self.cargarDatos()
            except Exception as e:
                print(f"Error al instanciar editoriales: {e}")
        elif clase == "Autor-Libro":
            try:
                autorlibro=AutorLibro()
                self.registros = autorlibro.autorlibrocompleto
                self.indice_actual = 0
                self.titulo_panel_administracion="Autor-Libro"
                self.cargarDatos()
            except Exception as e:
                print(f"Error al instanciar autorlibro: {e}")
        elif clase == "Inicio":
            self.cargarDatos("Inicio")
        else:
            print("No se encontró la clase")
    


    """Accion para mostrar y ocultar ventana"""
    # def toggle(self, ventana):
    #     if self.ventanas.get(ventana) is None:
    #         # Guardar información detallada
    #         self.ventanas[ventana] = self.get_window_details(ventana)

    #     if self.visible:
    #         self.slide_out(ventana)
    #     else:
    #         self.slide_in(ventana)

    def slide_out(self, ventana):
        # Guardar información detallada si no se ha hecho ya
        if self.ventanas.get(ventana) is None:
            self.ventanas[ventana] = self.get_window_details(ventana)
            print(self.ventanas[ventana])

        # Función para mover la ventana hacia arriba
        def mover_ventana(i):
            if i <= 200:  # Continuar hasta que haya deslizado completamente
                ventana.place(x=ventana.winfo_x(), y=ventana.winfo_y() - i)  # Mover hacia arriba
                self.update_idletasks()
                self.after(10, mover_ventana, i + 5)  # Llama a sí mismo con el nuevo valor
            else:
                ventana.place_forget()  # Ocultar la ventana al final del movimiento
                self.visible = False

        # Iniciar el movimiento
        mover_ventana(0)


    def slide_in(self, ventana):
        detalles = self.ventanas[ventana]
        original_x = detalles['x']
        original_y = detalles['y']
        original_width = detalles['width']
        original_height = detalles['height']

        # Desactivar el ajuste automático de tamaño
        ventana.update_idletasks()  # Asegúrate de que el tamaño se calcule correctamente

        # Coloca la ventana fuera de la vista inicialmente
        ventana.place(x=original_x, y=original_y - original_height, width=original_width)

        # Función para mover la ventana hacia abajo
        def mover_ventana(i):
            if i <= original_height:
                ventana.place(x=original_x, y=original_y - original_height + i, width=original_width)
                self.update_idletasks()
                self.after(10, mover_ventana, i + 5)
            else:
                # Asegúrate de que esté en la posición original al final
                ventana.place(x=original_x, y=original_y, width=original_width, height=original_height)

        mover_ventana(0)
        self.visible = True





    def get_window_details(self, ventana):
        # Obtener las coordenadas, tamaño y nombre de la ventana
        x = ventana.winfo_x()
        y = ventana.winfo_y()
        width = ventana.winfo_width()
        height = ventana.winfo_height()
        name = ventana.__class__.__name__  # Esto obtendrá el nombre de la clase del panel

        return {
            'x': x,
            'y': y,
            'width': width,
            'height': height,
            'name': name
        }

    def grid_info(self, ventana):
        # Devuelve información del grid
        return {
            'row': ventana.grid_info().get('row', None),
            'column': ventana.grid_info().get('column', None)
        }



    def cargarDatos(self, quepanel=None):
        if quepanel == "Inicio":
            self.panel_datos.pack_forget()
            self.crear_panel_inicio()
        else:
            self.panel_inicio.pack_forget()
            self.creacion_cuerpo_datos()

            self.campos = {}
            self.columnas = list(self.registros[0].keys())

            for columna in self.columnas:
                # Contenedor de cada fila (etiqueta + campo)
                frame_fila = tk.Frame(self.panel_cuerpo, bg=COLOR_PANEL_INFO)
                frame_fila.pack(pady=10, fill="x")
                if columna.lower() != "id":
                    col = columna

                    tk.Label(frame_fila, text=col, width=15,
                              anchor="w", font=("Arial", 14, "bold"), bg=COLOR_PANEL_INFO).pack(side="left", padx=5)

                    self.campos[col] = tk.Entry(frame_fila , font=("Arial", 14, "bold"))
                    self.campos[col].pack(side="left", expand=True, fill="x", padx=15)


            self.mostrar_registro()

            btnMas=tk.Button(self.panel_cuerpo, text="Siguiente", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                command=self.siguiente_registro)
            btnMas.pack(side="right", padx=20)
            self.hover_event(btnMas)

            btnMenos= tk.Button(self.panel_cuerpo, text="Anterior", padx=20, bg=COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                command=self.anterior_registro)
            btnMenos.pack(side="right", padx=20)
            self.hover_event(btnMenos)

            self.crear_tabla()

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

    def creacion_cuerpo_datos(self):
        self.panel_datos = tk.Frame(self.cuerpo_principal, bg=COLOR_CUERPO_PRINCIPAL)
        self.panel_datos.place(relwidth=1, relheight=1)  # Usando place para ocupar todo el espacio

        # Definir dimensiones del panel_cuerpo
        ancho_cuerpo = 600
        alto_cuerpo = 250

        # Crear el panel cuerpo dentro de panel_datos
        self.panel_cuerpo = tk.Frame(self.panel_datos, bg=COLOR_PANEL_INFO)

        # Función para centrar el panel_cuerpo
        def ajustar_panel():
            # Obtener posiciones centradas
            x, y = util_ventana.centrar_panel(self.panel_datos, ancho_cuerpo, alto_cuerpo)
            
            # Coloca el panel_cuerpo centrado
            self.panel_cuerpo.place(width=ancho_cuerpo, height=alto_cuerpo, x=x, y=100)
          

        # Vincular el evento de configuración
        self.panel_datos.bind("<Configure>", lambda event: ajustar_panel())

        # Etiqueta para el título
        tk.Label(self.panel_datos, text=f"Panel de Administración de {self.titulo_panel_administracion}", 
                bg=COLOR_CUERPO_PRINCIPAL, fg=COLOR_BARRA_SUPERIOR, font=("Arial", 30, "bold")).place(relx=0.5, y=10, anchor="n")

        # Crear panel para la tabla
        self.panel_tabla = tk.Frame(self.panel_datos, bg="#FFFFFF")
        self.panel_tabla.place(relwidth=1, relheight=0.25, y=400)  # Ajusta la posición según sea necesario
       

    def creacion_acciones_cuerpo_datos(self):
        # Definir dimensiones del panel_cuerpo
        ancho_cuerpo = 600
        alto_cuerpo = 250

        # Crear el panel cuerpo dentro de panel_datos
        self.panel_acciones_cuerpo = tk.Frame(self.panel_datos, bg=COLOR_PANEL_INFO)
        self.panel_acciones_cuerpo.place(width=ancho_cuerpo, height=alto_cuerpo, relx=0.5, y=100)


        




    # Crear la tabla
    def crear_tabla(self):
        # Asegúrate de que self.registros no esté vacío
        if not self.registros:
            print("No hay registros para mostrar.")
            return

        # Obtener las columnas de los registros
        self.columnas = list(self.registros[0].keys())

        # Crear un estilo para la tabla
        style = ttk.Style()
        style.configure("Heading", background=COLOR_CABECERA_TABLA)
        style.configure("Treeview.Heading", font=("Arial", 14, "bold"))  # Cabeceras en 14 bold
        style.configure("Treeview", font=("Arial", 12), background=COLOR_PANEL_INFO)  # Contenido en 12

        # Crear la tabla
        self.tabla = ttk.Treeview(self.panel_tabla, columns=self.columnas, show="headings", style="Treeview")
        
        # Configurar las cabeceras de la tabla
        for col in self.columnas:
            self.tabla.heading(col, text=col)
            self.tabla.column(col, width=200)

        # Insertar los datos en la tabla
        for registro in self.registros:
            self.tabla.insert("", "end", values=[registro[col] for col in self.columnas])

        # Opcional: Agregar una barra de desplazamiento
        scrollbar = tk.Scrollbar(self.panel_tabla, orient="vertical", command=self.tabla.yview)
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
        # Obtener el item seleccionado
        item = self.tabla.selection()
        if item:
            # Obtener los valores del item seleccionado
            self.item_values_selected_tabla = self.tabla.item(item, "values")

            

