archivo_txt = "texto_usuario.txt"


"""Leer todo el contenido del archivo"""
# try:
#     with open(archivo_txt, mode="r", encoding="utf-8") as archivo:
#         contenido = archivo.read()

#     print(
#         f"\nEl archivo tiene el siguiente contenido\n{'-'*40}\n{contenido}\n{'-'*40}")

# except FileNotFoundError:
#     print(f"El archivo {archivo_txt} no existe")


"""Leer por lineas"""

try:
    with open(archivo_txt, mode="r", encoding="utf-8") as archivo:
        print(
            f"\nEl archivo tiene el siguiente contenido\n{'-'*40}")

        for numero, linea in enumerate(archivo, start=1):
            print(f"{numero}: {linea.strip()}")

    print(f"\n{'-'*40}")

except FileNotFoundError:
    print(f"El archivo {archivo_txt} no existe")
