from DataBase import Database
from config_manager import ConfigManager

# Permitir al usuario seleccionar la base de datos y tabla
config = ConfigManager()
print(f"Base de datos actual: {config.get_database_config()['database']}")

nueva_db = input(
    "Ingrese el nombre de la base de datos (Enter para mantener la actual): ")
if nueva_db:
    config.set_database(nueva_db)

tabla = input("Ingrese el nombre de la tabla con la que quiere trabajar: ")

# Crear la instancia de la base de datos con la tabla seleccionada
db = Database(tabla)

# Mostrar los registros de la tabla seleccionada
# registros = db.ejecutar_consulta(f"SELECT * FROM {tabla}", fetch=True)
registros = db.listar_todos()


print("\nRegistros en la tabla seleccionada:")
for registro in registros:
    print(registro)

db.cerrar_conexion()
