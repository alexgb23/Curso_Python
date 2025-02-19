def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    print(total)

def saludar(*nombres):
    for nombre in nombres:
        print(f"Hola {nombre}")