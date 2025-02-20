import csv
# Lista de diccionarios con datos de usuarios
usuarios = [
    {"Nombre": "Juan Pérez", "Edad": 30, "Correo": "juan.perez@email.com"},
    {"Nombre": "María López", "Edad": 25, "Correo": "maria.lopez@email.com"},
    {"Nombre": "Carlos García", "Edad": 40, "Correo": "carlos.garcia@email.com"},
    {"Nombre": "Ana Torres", "Edad": 35, "Correo": "ana.torres@email.com"},
    {"Nombre": "Pedro Sánchez", "Edad": 28, "Correo": "pedro.sanchez@email.com"},
    {"Nombre": "Lucía Ramírez", "Edad": 22, "Correo": "lucia.ramirez@email.com"},
    {"Nombre": "Javier Muñoz", "Edad": 33, "Correo": "javier.munoz@email.com"},
    {"Nombre": "Elena Díaz", "Edad": 27, "Correo": "elena.diaz@email.com"},
    {"Nombre": "Roberto Gómez", "Edad": 45, "Correo": "roberto.gomez@email.com"},
    {"Nombre": "Sofía Herrera", "Edad": 29, "Correo": "sofia.herrera@email.com"},
    {"Nombre": "Martín Ortega", "Edad": 31, "Correo": "martin.ortega@email.com"},
    {"Nombre": "Gabriela Castro", "Edad": 26, "Correo": "gabriela.castro@email.com"},
    {"Nombre": "Fernando Ruiz", "Edad": 38, "Correo": "fernando.ruiz@email.com"},
    {"Nombre": "Patricia Mendez", "Edad": 24, "Correo": "patricia.mendez@email.com"},
    {"Nombre": "Ricardo Fernández", "Edad": 37, "Correo": "ricardo.fernandez@email.com"},
    {"Nombre": "Beatriz Soto", "Edad": 34, "Correo": "beatriz.soto@email.com"},
    {"Nombre": "Alberto Reyes", "Edad": 39, "Correo": "alberto.reyes@email.com"},
    {"Nombre": "Daniela Vázquez", "Edad": 32, "Correo": "daniela.vazquez@email.com"},
    {"Nombre": "Hugo Salazar", "Edad": 21, "Correo": "hugo.salazar@email.com"},
    {"Nombre": "Paula Núñez", "Edad": 23, "Correo": "paula.nunez@email.com"}
]

# Nombre del archivo CSV
archivo_csv = "usuarios.csv"

# Escribir los datos en el archivo CSV
with open(archivo_csv, mode="w", newline="", encoding="utf-8") as archivo:
    encabezados=usuarios[0].keys()
    escritor = csv.DictWriter(archivo, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(usuarios)

print(f"Los datos se han guardado en el archivo {archivo_csv}")