from panel_Principal.form_maestro_design import *
import modulos.paneles.crear_panel_admin as crear_panel_admin

def siguiente_registro(self):
    """ Muestra el siguiente registro """
    if self.indice_actual < len(self.registros) - 1:
        self.indice_actual += 1
        crear_panel_admin.mostrar_registro(self)

def anterior_registro(self):
    """ Muestra el registro anterior """
    if self.indice_actual > 0:
        self.indice_actual -= 1
        crear_panel_admin.mostrar_registro(self)