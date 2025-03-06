from PIL import ImageTk, Image
#Para instalar pillow: pip install Pillow==11.1.0  

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

def leer_imagen_con_transparencia(path, size):
    # Cargar la imagen y convertirla a RGBA para manejar la transparencia
    imagen = Image.open(path).convert("RGBA")
    # Redimensionar la imagen
    imagen = imagen.resize(size, Image.ADAPTIVE)
    # Convertir a PhotoImage para usar en Tkinter
    return ImageTk.PhotoImage(imagen)