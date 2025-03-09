import tkinter as ttk
import tkinter as tk
import config.config as colores
import modulos.paneles.tabla as tabla
import modulos.botones.btn_hover as btn_hover
from clases.libros import Libros
from clases.autores import Autores
from clases.editoriales import Editoriales
from clases.autorlibro import AutorLibro

def creacion_penel_buscar(self, tipo_boton):
    tk.Label(self.panel_acciones_cuerpo, text=f"Buscador de {self.titulo_panel_administracion}", 
             bg=colores.COLOR_PANEL_INFO, font=("Arial", 20, "bold"), fg="darkblue").pack(pady=15)
    
    self.label_lupa = tk.Label(self.panel_acciones_cuerpo, image=self.lupa, 
                                bg=colores.COLOR_PANEL_INFO, padx=10, pady=10)
    self.label_lupa.place(x=500, y=80, anchor="center", 
                          width=self.lupa.width(), height=self.lupa.height())
    self.label_lupa.lift()
  
    self.checkbox_vars=[]
    # Este método crea los checkboxes dependiendo del panel
    crear_checkboxes(self, self.titulo_panel_administracion)
    
    
    # Frame para el campo de búsqueda
    frame_fila = tk.Frame(self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
    frame_fila.pack(pady=30, fill="x")

    tk.Label(frame_fila, text="Texto a Buscar", width=12, anchor="w", 
             font=("Arial", 14, "bold"), bg=colores.COLOR_PANEL_INFO).pack(side="left", padx=5)

    self.campo_busqueda = tk.Entry(frame_fila, font=("Arial", 14, "bold"))
    self.campo_busqueda.pack(side="left", expand=True, fill="x", padx=20)

    # Este método crea los botones automáticos dependiendo del panel        
    boton = tk.Button(
        self.panel_acciones_cuerpo,
        text="Buscar",
        padx=20,
        bg=colores.COLOR_BTN,
        font=("Arial", 12, "bold"),
        fg="white",
        command= lambda: recolectar_datos_busqueda(self) # Aquí está la corrección
    )

    # Empaquetar el botón
    boton.pack(side="right", padx=20)
    btn_hover.hover_event(self, boton)
    
    # Forzar el ajuste del panel después de cargar los datos para que no sea visible
    self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))



# Este método crea los checkboxes dependiendo del panel 
def crear_checkboxes(self, tipo):
    opciones = {
        "Libros": ["id", "titulo", "año", "autor", "editorial"],
        "Autores": ["id", "nombre", "apellido", "nacionalidad"],
        "Editoriales": ["id", "nombre", "direccion", "telefono"],
        "Autor-Libro": ["nombre_del_autor", "titulo_del_libro"]
    }

    if tipo in opciones:
        # Frame para los primeros dos checkboxes
        frame_check1 = tk.Frame(self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
        frame_check1.pack(pady=10)

        # Frame para los últimos checkboxes
        frame_check2 = tk.Frame(self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
        frame_check2.pack(pady=15, fill="x")

        # Diccionario para almacenar variables de checkboxes
        self.checkbox_vars = {}

        for i, opcion in enumerate(opciones[tipo]):
            var = tk.IntVar()  # Crear una variable para el checkbox
            checkbox = tk.Checkbutton(frame_check1 if i < 2 else frame_check2, text=opcion, variable=var,
                                      bg=colores.COLOR_PANEL_INFO, font=("Arial", 12, "bold"))
            checkbox.pack(side="left", padx=10)  # Empaquetar a la izquierda
            
            # Guardar la variable en el diccionario con el nombre de la opción
            self.checkbox_vars[opcion] = var  

def obtener_valores(self):
    # Recoger y mostrar los valores de los checkboxes
    valores = {nombre: var.get() for nombre, var in self.checkbox_vars.items()}
    return valores


def recolectar_datos_busqueda(self):
    # Obtiene un diccionario con los valores de los checkboxes
    valores= obtener_valores(self)
    campos = []
    
    for campo, valor in valores.items():
        if valor == 1:
            campos.append(campo)

    # Cambiar "anio" a "anios" si está presente en los campos
    if "año" in campos:
        campos[campos.index("año")] = "anio"

    # Si no hay campos seleccionados, realizar la búsqueda por esto
    if not campos and self.titulo_panel_administracion == "Libros":
        campos = ["id", "titulo", "anio"]
    elif not campos and self.titulo_panel_administracion == "Autores":
        campos = ["id", "nombre", "apellido", "nacionalidad"]
    elif not campos and self.titulo_panel_administracion == "Editoriales":
        campos = ["id", "nombre","direccion","telefono"]
    elif not campos and self.titulo_panel_administracion == "AutorLibro":
        campos = ["id_libro", "id_autor"]

    # Actualizar la tabla con los resultados de la búsqueda
    busqueda_baseDatos(self, campos)


def busqueda_baseDatos(self , campos):
    busqueda = self.campo_busqueda.get()
    self.reg_busqueda=[]
    if self.titulo_panel_administracion == "Libros":
        self.reg_busqueda=busqueda_libros(self, campos, busqueda)
    elif self.titulo_panel_administracion == "Autores":
        autores = Autores()
        self.reg_busqueda=autores.filtrar(campos,busqueda)
    elif self.titulo_panel_administracion == "Editoriales":
        editoriales = Editoriales()
        self.reg_busqueda= editoriales.filtrar(campos,busqueda)
    # elif self.titulo_panel_administracion == "AutorLibro":
    #     autorlibro= AutorLibro()
    #     resultados = autorlibro.filtrar(campos,busqueda)
    #     self.busqueda=resultados
    
    tabla.actualizar_tabla(self, self.reg_busqueda)
    self.campo_selected_table = {}

def busqueda_libros(self, campos, busqueda):
    libros = Libros()
    if campos == ["editorial"]:
        resultados = libros.filtrar_libros_por_editorial(busqueda)
        return resultados
    elif campos == ["autor"]:
        resultados = libros.filtrar_libros_por_autor(busqueda)
        return resultados
    else:
        resultados = libros.filtrar_libros(campos, busqueda)
        if not resultados:
            resultados = libros.filtrar_libros_por_autor(busqueda)
            if not resultados:
                resultados = libros.filtrar_libros_por_editorial(busqueda)

        return resultados
