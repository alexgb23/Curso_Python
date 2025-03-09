from panel_Principal.form_maestro_design import *

# definir_botones laterales y superiores
 # Agregar estado a cada botón del menu lateral y superior para marcar el botón activo con el metodo marcar_boton
def definir_btn_menu_lateral(self):
    return [
        {"text": "Inicio", "icon": "\uf0e4", "activo": False},
        {"text": "Libros", "icon": "\uf0f6", "activo": False},
        {"text": "Autores", "icon": "\uf0f6", "activo": False},
        {"text": "Editoriales", "icon": "\uf0f6", "activo": False},
        {"text": "Autor-Libro", "icon": "\uf0f6", "activo": False},
        {"text": "Crear Tabla", "icon": "\uf0f6", "activo": False},
    ]

def definir_btn_menu_superior(self):
    return [ 
        {"text": "Actualizar", "icon": "\uf021", "activo": False},
        {"text": "Eliminar", "icon": "\uf2ed", "activo": False},
        {"text": "Insertar", "icon": "\uf067", "activo": False},
        {"text": "Buscar", "icon": "\uf002", "activo": False},
        ]

