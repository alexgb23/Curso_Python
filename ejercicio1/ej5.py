"""
Crea una funcion que se encargue de eliminar los espacios en blanco de un String
usando la compresion de listas y y devolvera los caracteres restantes
"""


def quitar_espacios(texto):
    return "".join([i for i in texto if i != " "])


string = "hola mundo, este es mi string"
sinespacios = quitar_espacios(string)
print(sinespacios)

"""
contar en un diccionario, cuantas veces se repiten los caracteres
de un string. esta funcion recibira como parametro lista
"""


def cuenta_caracteres(sinesp):
    # Crear un diccionario para almacenar la cuenta de caracteres
    contador = {}

    # Iterar sobre cada carácter en el string
    for caracter in sinesp:
        if caracter in contador:
            # Incrementar el contador si el carácter ya está en el diccionario
            contador[caracter] += 1
        else:
            # Inicializar el contador si es la primera vez que aparece
            contador[caracter] = 1

    return contador


contador = cuenta_caracteres(sinespacios)

print(contador)

"""
Vamos a tener que ordenar las llaves de un diccionario por el valor 
que tienen y devolver una lista de tuplas, se ordena de mayor a menor
"""


def ordenar(dicc):
    # Ordenar el diccionario por sus valores en orden descendente
    return sorted(dicc.items(), key=lambda item: item[1], reverse=True)


ordenados = ordenar(contador)
print(ordenados)

"""
De un listado de tuplas, devolver aquellas que tengan el mayor valor
(pueden ser varias con el mismo valor)
"""

def mayores_tuplas(tup):
    # Encontrar el valor máximo en las tuplas
    # Suponiendo que el valor está en la segunda posición
    valor_maximo = max(tupla[1] for tupla in tup)
    # Filtrar y devolver las tuplas que tienen el valor máximo
    return [tupla for tupla in tup if tupla[1] == valor_maximo]

mayores= mayores_tuplas(ordenados)

print(mayores)