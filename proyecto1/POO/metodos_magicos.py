class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
        self.hablando = self.habla()

    def habla(self):
        return 'Guau guau'

    def __str__(self):
        return f"{self.nombre} tiene {self.edad} años de edad y hace {self.hablando}"


mi_perro = Perro('Rex', 3)
print(mi_perro)
