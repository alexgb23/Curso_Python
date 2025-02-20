import csv
leer_usuarios = "usuarios.csv"

"""Recuperar datos de un archivo CSV, línea a línea sin importsr csv"""

# try:
#     with open(leer_usuarios, mode="r", encoding="utf-8") as archivo:
#         # Leer la primera línea para obtener los encabezados
#         encabezados = archivo.readline().strip().split(",")

#         print(f"\nEl archivo tiene el siguiente contenido\n{'-'*40}")

#         # Comenzar en 2 porque ya leímos la primera línea
#         for numero, linea in enumerate(archivo, start=2):
#             print(f"Línea {numero}: {linea.strip()}")
#             campos = linea.strip().split(",")

#             for encabezado, campo in zip(encabezados, campos):
#                 print(f"{encabezado.strip()}: {campo.strip()}")
#             print()  # Línea en blanco para separar usuarios

# except FileNotFoundError:
#     print(f"El archivo {leer_usuarios} no existe")


"""Recuperar datos de un archivo CSV, linea a linea con import csv"""
lista_usuarios = []

try:
    with open(leer_usuarios, mode="r", encoding="utf-8") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            fila["Edad"] = int(fila["Edad"])
            lista_usuarios.append(fila)

    print("lita de usuarios")
    for usuario in lista_usuarios:
        print(usuario)
        print(f"Nombre: {usuario['Nombre']}")
        print(f"Edad: {usuario['Edad']}")
        print(f"Correo: {usuario['Correo']}")
        print()

except FileNotFoundError:
    print(f"El archivo {leer_usuarios} no existe")
