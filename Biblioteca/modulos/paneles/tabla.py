from panel_Principal.form_maestro_design import *

"""Creacion de la Tabla"""
def crear_tabla(self):
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
    #dicho evento se encuentra en form_maestro
    self.tabla.bind("<ButtonRelease-1>", self.on_item_tabla_click)
