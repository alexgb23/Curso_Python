from modulos.metodos_basicos import *
import modulos.botones.btn_config as btn_config


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