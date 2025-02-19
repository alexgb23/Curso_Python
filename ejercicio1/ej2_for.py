# """Ejercicio 2"""
# for i in range(3):
#     compra = float(input("Ingrese el monto de la compra: "))
#     if compra < 50:
#         DESCUENTO = 0
#     elif compra < 100:
#         DESCUENTO = 5
#     elif compra < 200:
#         DESCUENTO = 10
#     else:
#         DESCUENTO = 15

#     print(f"El descuento aplicado es de: {DESCUENTO*compra/100}")
#     print(f"El total de la compra es de: {compra - compra*DESCUENTO/100}")


# """Contar_Numeros"""
# positivos_pares = 0
# positivos_impares = 0
# negativos_pares = 0
# negativos_impares = 0
# ceros = 0

# for _ in range(10):
#     num = int(input("Ingrese un número: "))
#     if num == 0:
#         ceros += 1
#     if num > 0:
#         if num % 2 == 0:
#             positivos_pares += 1
#         else:
#             positivos_impares += 1
#     else:
#         if num % 2 == 0:
#             negativos_pares += 1
#         else:
#             negativos_impares += 1


# print(f"Positivos pares: {positivos_pares}")
# print(f"Positivos impares: {positivos_impares}")
# print(f"Negativos pares: {negativos_pares}")
# print(f"Negativos impares: {negativos_impares}")
# print(f"Ceros: {ceros}")


#Obtener Coordenadas
# for i in range(5):
#     for j in range(5):
#         print(f"({i}, {j})")