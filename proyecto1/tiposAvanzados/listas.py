# mi_lista = [1, True, "Kepa", 3.14]

# print(mi_lista)

frutas = ["manzana", "banana", "naranja", "platano", "pera", "fresa", "kiwi", "melón", "cereza"]
# print(frutas[0])
# print(frutas[-1])

numeros = [1, 2, 3, 4, 5]
numeros[1] = 10
# print(numeros)

lista_grande = frutas+numeros
# print(lista_grande)

# rango= list(range(8))
# print(rango)

# print(frutas[1::2])

frutas.append("uva")
frutas.insert(2, "sandia")
frutas.remove("banana")
frutas.pop(5)
print(frutas)