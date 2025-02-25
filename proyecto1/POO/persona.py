class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Estudiante(Persona):
    def __init__(self, nombre, edad, matricula):
        super().__init__(nombre, edad)
        self.matricula = matricula
        print(
            f"Nombre: {self.nombre}, Edad: {self.edad}, Matricula: {self.matricula}")


alumno = Estudiante("Juan", 20, 1234)
