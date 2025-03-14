import tkinter as ttk
import tkinter as tk
import modulos.paneles.tabla as tabla
import modulos.botones.btn_hover as btn_hover
import config.config as colores


# este metodo se encarga de cargar los datos cuando se hace click en uno de los botones laterales 
# llenando el panel cuerpo donde estan los botones mas y menos para ir visualizando los elementos
# ademas llama a mostrar registro y crea la tabla 

def cargarDatos(self, quepanel=None):
    # Esto lo hago para si clican en inicio al cargar el panel no se rompa el programa
    if quepanel == "Inicio" and self.titulo_panel_administracion != "Bienvenido a eDe-Lib":
        if self.titulo_panel_administracion == "Nueva Tabla en la Base de Datos":
            self.panel_nueva_tabla.pack_forget()
            self.crear_panel_bienvenida()
        else:
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
            frame_fila = tk.Frame(self.panel_cuerpo, bg=colores.COLOR_PANEL_INFO)
            frame_fila.pack(pady=10, fill="x")

             # Obtener la etiqueta correspondiente, o usar la columna en sí
            texto_label = etiquetas.get(columna, columna.title())
          
            self.label = tk.Label(frame_fila, text=texto_label, width=15,
                    anchor="w", font=("Arial", 14, "bold"), bg=colores.COLOR_PANEL_INFO).pack(side="left", padx=5)
            
            self.campos[columna] = ttk.Entry(
                frame_fila, font=("Arial", 14, "bold"))
            self.campos[columna].pack(
                side="left", expand=True, fill="x", padx=15)
        
             
        btnMas = tk.Button(self.panel_cuerpo, text="Siguiente", padx=20, bg=colores.COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                           command= lambda: 
                           siguiente_registro(self))
        btnMas.pack(side="right", padx=20)
        btn_hover.hover_event_sup(self, btnMas)
        btnMenos = tk.Button(self.panel_cuerpo, text="Anterior", padx=20, bg=colores.COLOR_BTN, font=("Arial", 12, "bold"), fg="white",
                             command= lambda: 
                             anterior_registro(self))
        btnMenos.pack(side="right", padx=20)
        btn_hover.hover_event_sup(self, btnMenos)

        mostrar_registro(self)
        tabla.crear_tabla(self)

def mostrar_registro(self):
    """ Muestra el registro actual en los campos de texto """
    if not self.registros or self.indice_actual >= len(self.registros):
        return

    registro_actual = self.registros[self.indice_actual]
    
    for columna, campo in self.campos.items():
        campo.config(state="normal")
        campo.delete(0, tk.END)
        
        # Verifica si el campo está vacío antes de insertar
        valor = registro_actual.get(columna, "")  # Usa get para evitar KeyError
        campo.insert(0, valor if valor else "")  # Inserta un valor vacío si no hay
        campo.config(state="readonly")


def siguiente_registro(self):
    """ Muestra el siguiente registro """
    if self.indice_actual < len(self.registros) - 1:
        self.indice_actual += 1
        mostrar_registro(self)

def anterior_registro(self):
    """ Muestra el registro anterior """
    if self.indice_actual > 0:
        self.indice_actual -= 1
        mostrar_registro(self)


