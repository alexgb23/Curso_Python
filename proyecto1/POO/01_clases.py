class Perro:
    patas = 4
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def habla(self):
        print("El perro dice: ¡Guau!")

mi_perro = Perro("Lai", 2)
mi_perro.habla()

print(Perro.patas)