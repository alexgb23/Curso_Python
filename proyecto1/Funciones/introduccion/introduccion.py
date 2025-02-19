# """
# Escribe una funcion que lance un saludo personalizado
# Calcular el area de un triangulo recto dados los lados
# Verifica que un numero es para o impar
# Calculo de la potencia de un numero, siendo el exponente opcional, si falta = 2

# """
# import math


# def saludar(nombre):
#     print(f"Hola {nombre}, vamos a hacer algunos ejercicios")
#     return True


# def sumar(a, b, c=0):
#     suma = a+b+c
#     print(suma)


# def calcularArea(bas, alt):
#     area = (bas*alt)/2
#     print(f"El area del triangulo es: {area}")


# def potencia(numero, exponente):
#     result = numero ** exponente
#     print(f"El resultado es: {result}")


# def par_impar(numero):
#     if numero % 2 == 0:
#         print("El numero es par")
#     else:
#         print("El numero es impar")


# def es_primo(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(math.sqrt(n)) + 1):
#         if n % i == 0:
#             return False
#     return True


# def invertir_texto(texto):
#     return texto[::-1]


# while True:
#     try:
#         jugar = input("Ingrese su nombre: ")
#         if jugar != "":

#             print("Calcular el area de un triangulo")
#             base = int(input("Ingrese la base del triangulo: "))
#             altura = int(input("Ingrese la altura del triangulo: "))
#             calcularArea(base, altura)

#             print("Saber si el numero es par o impar")
#             npar = int(input("Ingrese un numero: "))
#             par_impar(npar)

#             print("Calcular la potencia de un numero")
#             num = int(input("Ingrese un numero: "))
#             e_input = input(
#                 "Ingrese el exponente (presione Enter para usar el valor por defecto 2): ")
#             if e_input.strip() == "":
#                 e = 2  # Valor por defecto
#             else:
#                 e = int(e_input)
#             potencia(num, e)

#             print("Verificar si un numero es primo")
#             np = int(input("Ingrese un numero: "))
#             if es_primo(np):
#                 print(f"El numero {np} es primo")
#             else:
#                 print(f"El numero {np} no es primo")

#             print("Invertir un texto")
#             text = input("Ingrese un texto: ")
#             print(invertir_texto(text))
#             break

#         else:
#             break
#     except ValueError:
#         print("Entrada no válida.")
