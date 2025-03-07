
def slide_out(self, ventana):
    def mover_ventana(i):
        if i <= 200:  # Continuar hasta que haya deslizado completamente
            # Mover hacia arriba
            ventana.place(x=ventana.winfo_x(), y=ventana.winfo_y() - i)
            self.update_idletasks()
            # Llama a sí mismo con el nuevo valor
            self.after(10, mover_ventana, i + 5)
        else:
            ventana.place_forget()  # Ocultar la ventana al final del movimiento
    # Iniciar el movimiento
    mover_ventana(0)



def slide_in(self, ventana, tiempo_espera=800):  # tiempo_espera en milisegundos
    original_x = self.coordenadas[0]
    original_y = self.coordenadas[1]
    original_width = self.ancho_cuerpo
    original_height = self.alto_cuerpo

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

    # Esperar antes de iniciar el movimiento
    self.after(tiempo_espera, mover_ventana, 0)
