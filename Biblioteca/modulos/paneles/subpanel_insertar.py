import tkinter as tk
import modulos.botones.btn_config as btn_config
import modulos.datos.datos_para_insertar as insert_data
import modulos.paneles.ccp_insertar_libro as insertar_libro
import modulos.paneles.ccp_insertar_autorlibro as insertar_autorlibro


def cargarDatosParaInsertar(self, tipo_boton):
    #titulo del panel 
    tk.Label(self.panel_acciones_cuerpo, text=f"Panel para Insertar {self.titulo_panel_administracion}", bg=btn_config.COLOR_PANEL_INFO, font=("Arial", 18, "bold")).pack(pady=5)
    self.campos_insertar = {}

    #buscar los datos a insertar en el panel y aplicar la condicion dependiendo de los datos
    #para crear la estructura del tipo de panel
    dat_filas=insert_data.datos_llenar_insertar(self, self.titulo_panel_administracion) 
    
    if "titulo" and "año" and "autor" and "editorial" in dat_filas:
        insertar_libro.crear_cuerpo_panel_insertar_libros(self,dat_filas)

    elif "libro" and "autor" in dat_filas:
        insertar_autorlibro.crear_cuerpo_panel_insertar_autor_libro(self,dat_filas)

    else:
        for columna in dat_filas:

            frame_fila = tk.Frame(
                self.panel_acciones_cuerpo, bg=btn_config.COLOR_PANEL_INFO)
            frame_fila.pack(pady=10, fill="x")

            tk.Label(frame_fila, text=columna, width=15,
                    anchor="w", font=("Arial", 14, "bold"), bg=btn_config.COLOR_PANEL_INFO).pack(side="left", padx=5)
            
            self.campos_insertar[columna] = tk.Entry(
                    frame_fila, font=("Arial", 14, "bold"))
            self.campos_insertar[columna].pack(
                    side="left", expand=True, fill="x", padx=15)
            
            
    #este metodo crea los botones automaticos dependiendo del panel        
    btn_config.crear_boton_sub_panel(self, tipo_boton)
    
    # Forzar el ajuste del panel después de cargar los datos para que no sea visible
    self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))