import tkinter as tk
import modulos.botones.btn_config as btn_config
import config.config as colores
import modulos.paneles.ccp_actualizar_libro as actualizar_libro
import modulos.paneles.ccp_actualizar_autorlibro as actualizar_autorlibro


def cargarDatosParaActualizar(self, tipo_boton):  
    #titulo del panel      
    tk.Label(self.panel_acciones_cuerpo, text=f"Panel para Actualizar {self.titulo_panel_administracion}", bg=colores.COLOR_PANEL_INFO, font=("Arial", 18, "bold")).pack(pady=5)
    self.campos_actualizar = {}

    #condicion para el tipo de panel que se va a crear dependiendo si es Libros o Autor-Libro
    if self.titulo_panel_administracion == "Libros":
        actualizar_libro.crear_cuerpo_panel_actualizar_libros(self, self.campo_selected_table)

    elif self.titulo_panel_administracion == "Autor-Libro":
        actualizar_autorlibro.crear_cuerpo_panel_actualizar_autor_libro(self, self.campo_selected_table)

    else:
       for columna, value in self.campo_selected_table.items():

        frame_fila = tk.Frame(
            self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
        frame_fila.pack(pady=10, fill="x")

        tk.Label(frame_fila, text=columna, width=15,
                 anchor="w", font=("Arial", 14, "bold"), bg=colores.COLOR_PANEL_INFO).pack(side="left", padx=5)
        
        self.campos_actualizar[columna] = tk.Entry(
            frame_fila, font=("Arial", 14, "bold"))
        self.campos_actualizar[columna].insert(0, value)
        self.campos_actualizar[columna].pack(
            side="left", expand=True, fill="x", padx=15)
        
        # condicion para si el input es id que no se pueda modificar
        if columna == "id":
            self.campos_actualizar[columna].config(state="readonly", fg="darkgrey")
    btn_config.crear_boton_sub_panel(self, tipo_boton)

    # Forzar el ajuste del panel después de cargar los datos para que no sea visible
    self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))