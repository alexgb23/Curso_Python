class Usuario:
    def guardar(self):
        print("Guardando en BD")


class Session:
    def guardar(self):
        print("Guardando en Archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()
sesion = Session()

guardar([usuario, sesion])
