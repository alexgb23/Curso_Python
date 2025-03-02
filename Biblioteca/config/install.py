import subprocess
import sys

# Función para verificar si Pillow está instalado
def check_and_install_pillow():
    try:
        import PIL
    except ImportError:
        print("Pillow no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow==11.1.0"])
    else:
        print("Pillow ya está instalado.")

# Llamar a la función
check_and_install_pillow()

# Resto de tu código aquí
