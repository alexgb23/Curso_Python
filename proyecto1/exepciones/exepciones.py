try:
    n1=int(input("Ingrese un número: "))
    # aeiou
except ValueError as e:
    print("Ingrese un número correcto")
except NameError as e:
    print("Variable no definida")
else:
    print("No hubo errores")
finally:
    print("Esto se ejecutara siempre")