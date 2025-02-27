import csv

class GestorCSV:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def escribir_csv(self, encabezados, datos):
        try:
            with open(self.nombre_archivo, mode="w", newline="", encoding="utf-8") as archivo:
                escritor = csv.DictWriter(archivo, fieldnames=encabezados)
                escritor.writeheader()
                escritor.writerows(datos)
            print(
                f"Los datos se han guardado en el archivo {self.nombre_archivo}")
        except Exception as e:
            print(f"Error al escribir en el archivo CSV: {e}")

    def leer_csv(self):
        try:
            with open(self.nombre_archivo, mode="r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                datos = [fila for fila in lector]
                return datos
        except FileNotFoundError:
            print(f"El archivo {self.nombre_archivo} no existe")
        except Exception as e:
            print(f"Error al leer el archivo CSV: {e}")
            return []

# Lista de diccionarios con datos de usuarios


if __name__ == "__main__":
    gestor_csv = GestorCSV("usuarios.csv")
    encabezados = ["id", "nombre", "edad", "email"]
    datos = [
        {"id": 1, "nombre": "Juan", "edad": 25, "email": "juan@email"},
        {"id": 2, "nombre": "María", "edad": 30, "email": "maria@email"},
        {"id": 3, "nombre": "Pedro", "edad": 35, "email": "pedro@email"},
    ]
    gestor_csv.escribir_csv(encabezados, datos)
    datos_leidos = gestor_csv.leer_csv()
    print("Datos leidos del archivo CSV:")
    for indice, usuario in enumerate(datos_leidos):
        print(f"Usuario {indice + 1}: {usuario}")
        for clave, valor in usuario.items():
            print(f"{clave}: {valor}")

