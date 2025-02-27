# class Animal:
#     def comer(self):
#         return "Comiendo"


# class Perro(Animal):
#     def pasear(self):
#         return "Paseando"


# class PerroProgramador(Perro):
#     def programar(self):
#         return "Programando"


# animal = Animal()
# perro = Perro()
# perro_programador = PerroProgramador()

# print(animal.comer())
# print(perro.comer(), perro.pasear())
# print(perro_programador.comer(), perro_programador.pasear(),
#       perro_programador.programar())


# class Animal:
#     def comer(self):
#         return "Comiendo"

#     def pasear(self):
#         return "Paseando animales"


# class Perro:
#     def pasear(self):
#         return "Paseando al perro"


# class Programador(Perro, Animal):
#     def programar(self):
#         return "Programando"


# programador = Programador()
# print(programador.comer(), programador.pasear(), programador.programar(), Animal.pasear(programador))


# class Caminador:
#     def caminar(self):
#         return "Caminando"
    

# class Volador:
#     def volar(self):
#         return "Volando"
    

# class Nadador:
#     def nadar(self):
#         return "Nadando"
    

# class Pato(Caminador, Volador, Nadador):
#     def programar(self):
#         return "Programando"
    

# pato = Pato()
# print(pato.caminar(), pato.volar(), pato.nadar(), pato.programar())


# class Ave:
#     def __init__(self):
#         self.volador = True

#     def volar(self):
#         print("Vuela ave")
    
# class Pato(Ave):
#     def __init__(self):
#         super().__init__()
#         self.nadador = True
#     def volar(self):
#         super().volar()
#         print("Vuela pato")
    
# lucas = Pato()
# print(lucas.nadador, lucas.volador)

