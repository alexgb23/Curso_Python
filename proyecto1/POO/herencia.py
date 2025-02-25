class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass


class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"


class Gato(Animal):
    def hacer_sonido(self):
        return "Miau"


perro = Perro("Firulais", 5)
gato = Gato("Garfield", 3)
print(f"{perro.nombre} hace {perro.hacer_sonido()}")
print(f"{gato.nombre} hace {gato.hacer_sonido()}")
