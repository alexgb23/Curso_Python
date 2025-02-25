class Perro:
    patas = 4

    def __init__(self, nombre):
        self.nombre = nombre

    @property
    def nombre(self):
        print("pasando por guetter")
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        print("pasando por setter")
        if nombre.strip():
            self.__nombre = nombre
        return None

            


perro=Perro("Lai")
print(perro.nombre)