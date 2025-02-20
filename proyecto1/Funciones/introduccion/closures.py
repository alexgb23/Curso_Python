def saludo_Personalizado(nombre):
    def mensaje():
        return f"Hola {nombre}"

    return mensaje

# saludo=saludo_Personalizado("Kepa")
# print(saludo())


def multiplicador(factor):
    def multiplicar(numero):
        return numero * factor
    return multiplicar

# doblar=multiplicador(2)
# triplicar=multiplicador(3)

# print(doblar(5))
# print(triplicar(5))


print(multiplicador(2)(5))
print(multiplicador(3)(5))
