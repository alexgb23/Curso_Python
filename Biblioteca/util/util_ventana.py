def centrar_ventana(ventana, aplicacion_ancho, aplicacion_largo):
    pantall_ancho = ventana.winfo_screenwidth()
    pantall_largo = ventana.winfo_screenheight()
    x= int((pantall_ancho/2)-(aplicacion_ancho/2))
    y= int((pantall_largo/2)-(aplicacion_largo/2))
    return ventana.geometry(f'{aplicacion_ancho}x{aplicacion_largo}+{x}+{y}')

def centrar_panel(panel_contenedor, panel_ancho, panel_alto):
    # Obtener las dimensiones del panel contenedor después de que se haya mostrado
    ancho_contenedor = panel_contenedor.winfo_width()
    alto_contenedor = panel_contenedor.winfo_height()
    
    # Calcular las posiciones x e y para centrar el panel
    x = (ancho_contenedor - panel_ancho) / 2
    y = 70
    
    return x, y
