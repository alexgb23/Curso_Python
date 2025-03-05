from PIL import ImageTk, Image
#Para instalar pillow: pip install Pillow==11.1.0  

def leer_imagen(path, size):
    return ImageTk.PhotoImage(Image.open(path).resize(size, Image.ADAPTIVE))

