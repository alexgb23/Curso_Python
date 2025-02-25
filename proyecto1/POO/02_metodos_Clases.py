class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):
        print("El perro dice: ¡Guau!")

    @classmethod
    def factory(cls):
        return cls("Felipe", 3)
    


# mi_perro = Perro("Lai", 2)
# mi_perro.habla()

# print(Perro.patas)

mi_perro = Perro.factory()
print(mi_perro.nombre, mi_perro.edad)

