numeros = [1, 2, 3, 4, 5]

primero, *segundo, tercero = numeros


# print(primero)
# print(segundo)
# print(tercero)


mascotas = ["Lai", "Gaba", "Pulga", "Cuqui"]

# for mascota in mascotas:
#     print(mascota)

# for mascota in enumerate(mascotas):
#     print(f"indice: {mascota[0]}, valor: {mascota[1]}")  # print(mascota[0], mascota[1])

# for indice , mascota in enumerate(mascotas):
#     print(f"indice: {indice}, valor: {mascota}")

# if "Cuqui" in mascotas:
#     print("Existe la mascota")
# else:
#     print("No existe la mascota")

try:
    posicion= mascotas.index("jose")
    print(posicion)
except ValueError:
    print("No existe la mascota")


