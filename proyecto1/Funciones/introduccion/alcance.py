"""
Modificando una variable global
"""
mensaje = "Hola desde el ambito global"


def saludar():
    global mensaje
    mensaje = "Hola desde el ambito local"
    print(mensaje)

# print(mensaje)
# saludar()
# print(mensaje)

contador=0
def incrementar():
    global contador
    contador+=1
    print(contador)

print(contador)
incrementar()
print(contador)