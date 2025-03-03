import subprocess
import sys
def check_and_install_mysql():
    try:
        import mysql.connector
    except ImportError:
        print("mysql.connector no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "mysql-connector-python"])
    else:
        print("mysql.connector ya está instalado.")

def check_and_install_pillow():
    try:
        import PIL
    except ImportError:
        print("Pillow no está instalado. Instalando...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "Pillow==11.1.0"])
    else:
        print("Pillow ya está instalado.")


