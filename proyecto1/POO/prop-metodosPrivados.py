class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.__set_nombre(nombre)
        self.__set_edad(edad)

    def habla(self):
        print(f"{self.__nombre} dice: ¡Guau!")

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def __set_nombre(self, nombre):
        if nombre != "":
            self.__nombre = nombre
        else:
            self.__nombre = "Sin nombre"

    def __set_edad(self, edad):
        if edad != 0:
            self.__edad = edad
        else:
            self.__edad = 1


mi_perro = Perro("", 0)
mi_perro.habla()
# print(mi_perro.__dict__)
# mi_perro._Perro__nombre = "Firulais"
# print(mi_perro._Perro__nombre)
# print(mi_perro.get_nombre())
# print(type(mi_perro._Perro__nombre))


