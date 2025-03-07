import tkinter as ttk
import tkinter as tk
import config.config as colores
import modulos.paneles.tabla as tabla

import modulos.botones.btn_acciones as btn_acciones
import modulos.botones.btn_config as btn_config


# este metodo se encarga de cargar los datos cuando se hace click en uno de los botones laterales 
# llenando el panel cuerpo donde estan los botones mas y menos para ir visualizando los elementos
# ademas llama a mostrar registro y crea la tabla 

def creacion_penel_buscar(self, tipo_boton, ):

    tk.Label(self.panel_acciones_cuerpo, text=f"Buscador de {self.titulo_panel_administracion}", bg=colores.COLOR_PANEL_INFO, font=("Arial", 20, "bold"), fg="darkblue").pack(pady=15)
    
    self.label_lupa = tk.Label(self.panel_acciones_cuerpo, image=self.lupa, bg=colores.COLOR_PANEL_INFO, padx=10, pady=10)
    self.label_lupa.place(x=500, y=80, anchor="center", width=self.lupa.width(), height=self.lupa.height())
    self.label_lupa.lift()


    # Inicializar las variables
    check_id = tk.IntVar()
    check_titulo = tk.IntVar()
    check_anio = tk.IntVar()
    check_edit = tk.IntVar()

    # Crear los checkboxes
   # Frame para los primeros dos checkboxes
    frame_check1 = tk.Frame(self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
    frame_check1.pack(pady=10, )

    op1 = tk.Checkbutton(frame_check1, text="Buscar por ID", variable=check_id, onvalue=1, offvalue=0, 
                         bg=colores.COLOR_PANEL_INFO, font=("Arial", 12, "bold"))
    op1.pack(side="left", padx=20)

    op2 = tk.Checkbutton(frame_check1, text="Buscar por Titulo", variable=check_titulo, onvalue=1, offvalue=0, 
                         bg=colores.COLOR_PANEL_INFO, font=("Arial", 12, "bold"))
    op2.pack(side="left", padx=20)

    # Frame para los últimos dos checkboxes
    frame_check2 = tk.Frame(self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
    frame_check2.pack(pady=15)

    op3 = tk.Checkbutton(frame_check2, text="Buscar por Año", variable=check_anio, onvalue=1, offvalue=0, 
                         bg=colores.COLOR_PANEL_INFO, font=("Arial", 12, "bold"))
    op3.pack(side="left", padx=60)

    op4 = tk.Checkbutton(frame_check2, text="Buscar por Editorial", variable=check_edit, onvalue=1, offvalue=0, 
                         bg=colores.COLOR_PANEL_INFO, font=("Arial", 12, "bold"))
    op4.pack(side="left")


        # Frame para el campo de búsqueda
    frame_fila = tk.Frame(self.panel_acciones_cuerpo, bg=colores.COLOR_PANEL_INFO)
    frame_fila.pack(pady=30, fill="x")

    tk.Label(frame_fila, text="Texto a Buscar", width=12, anchor="w", 
             font=("Arial", 14, "bold"), bg=colores.COLOR_PANEL_INFO).pack(side="left", padx=5)

    self.campo_busqueda = tk.Entry(frame_fila, font=("Arial", 14, "bold"))
    self.campo_busqueda.pack(side="left", expand=True, fill="x", padx=20)

        #este metodo crea los botones automaticos dependiendo del panel        
    btn_config.crear_boton_sub_panel(self, tipo_boton)
    
    # Forzar el ajuste del panel después de cargar los datos para que no sea visible
    self.panel_cuerpo.after(10, lambda: self.panel_acciones_cuerpo.place(y=-400))

   

