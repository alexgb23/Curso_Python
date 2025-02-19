import random
# numero_secreto = random.randint(1, 100)
# intentos = 0

# print(numero_secreto)

# numero_ingresado = int(input("Ingrese un número entre 1 y 100: "))
# intentos = intentos+1

# while numero_ingresado != numero_secreto:
#     print("El numero ingresado no es correcto")
#     numero_ingresado = int(input("Ingrese un número entre 1 y 100: "))
#     intentos = intentos+1
# print("Felicidades, has adivinado el número secreto en", intentos, "intentos")


# Generar un número secreto aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)
intentos = 0

print("¡Bienvenido al juego de adivinanza!")
print("He elegido un número entre 1 y 100. Intenta adivinarlo.")

while True:
    try:
        numero_ingresado = int(input("Ingrese un número entre 1 y 100: "))

        if numero_ingresado < 1 or numero_ingresado > 100:
            print("Por favor, ingrese un número dentro del rango indicado.")
            continue

        intentos += 1

        if numero_ingresado < numero_secreto:
            print("El número ingresado es demasiado bajo.")
        elif numero_ingresado > numero_secreto:
            print("El número ingresado es demasiado alto.")
        else:
            print(
                f"¡Felicidades! Has adivinado el número secreto en {intentos} intentos.")
            break

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número entero.")
