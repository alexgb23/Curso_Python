# class Model:
#     tabla = False
#     def __init__(self):
#         if not self.tabla:
#             print('No se ha definido la tabla')
#         else:
#             print('La tabla es:', self.tabla)

#     @classmethod
#     def buscar_por_id(self, id):
#         print(f"Buscando por id {id} en la tabla {self.tabla}")

# class Usuario(Model):
#     tabla = 'usuarios'

# user = Usuario()
# Usuario.buscar_por_id(1)

from abc import ABC, abstractmethod


class Model (ABC):
    @property
    @abstractmethod
    def tabla(self):
        pass

    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, id):
        print(f"Buscando por id {id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = 'usuarios'

    def guardar(self):
        print(f"Guardando en la tabla {self.tabla}")


user = Usuario()
user.guardar()
Usuario.buscar_por_id(1)
