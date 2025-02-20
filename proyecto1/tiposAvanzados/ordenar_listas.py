# numeros = [1, 5, 4, 10, 78, 69, 25, 8]

# numeros.sort()
# # numeros.sort(reverse=True)

# print(numeros)

# alfanumerico = [True, 4, 5, False, 6]

# alfa2 = sorted(alfanumerico)

# print(alfa2)

# print(alfanumerico)

# numeros1 = sorted(numeros, reverse=True)

# print(numeros1)


"""Ordenar listas de listas"""
usuarios=[
    [4, "kevin"],
    [1, "pedro"],
    [5, "jose"]
]

# usuarios.sort()

# print(usuarios)

Usuarios=[
    ["kevin", 4],
    ["pedro", 1],
    ["jose", 5]
]

# Usuarios.sort()

# print(Usuarios)

def ordena(elemento):
    return elemento[1]

# Usuarios.sort(key=ordena, reverse=True)

# print(Usuarios)


# Usuarios.sort(key=lambda elemento: elemento[1])
Usuarios.sort(key=lambda elemento: elemento[1], reverse=True)

print(Usuarios)