"""
Generar una lista del 1 al 100
mostrar la suma de los numeros pares
mostrar la suma de los numeros impares
"""

# lista = [i for i in range(1, 101)]
# print(lista)
# print(f"La suma de los pares es: {sum([i for i in lista if i%2==0])}")
# print(f"La suma de los impares es: {sum([i for i in lista if i%2!=0])}")


# lista=[]

# for i in range(1,101):
#     lista.append(i)

# def par():
#     return sum([i for i in lista if i%2==0])

# def impar():
#     return sum([i for i in lista if i%2!=0])


# print(par())
# print(impar())


# lista=list(range(1,101))
# pares=0
# impares=0

# for num in lista:
#     if num%2==0:
#         pares+=num
#     else:
#         impares+=num

# print(f"La suma de los pares es: {pares}")
# print(f"La suma de los impares es: {impares}")


"""
Crea una lista con numeros pares dado el numero por teclado
"""

# numero_dado = int(input("Ingresa un numero: "))

# # lista = [i for i in range(1, numero_dado+1) if i%2==0]

# # print(f"La lista es: {lista}")

# lista=[]

# for i in range(1, numero_dado+1):
#     if i%2==0:
#         lista.append(i)

# print(f"La lista es: {lista}")


"""
Dada una lista con elementos repetidos, crear una nueva lista sin elementos repetidos
"""

# repetidos = [1, 2, 3, 2, 4, 5, 4, 6, 1]

# # no_repetidos = [i for i in set(repetidos)]

# no_repetidos=[]

# for item in repetidos:
#     if item not in no_repetidos:
#         no_repetidos.append(item)

# print("Repetidos", repetidos)
# print("No Repetidos", no_repetidos)


"""
dado un numero, generar una lista con los numeros primos
"""

# n = int(input("Ingresa un numero: "))


# def es_primo(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5)+1):  # acotar hasta la raiz cuadrada del numero
#         if num % i == 0:
#             return False
#     return True

# def primeros_n_primos(n):
#     primos = []
#     num = 2
#     while len(primos) < n:
#         if es_primo(num):
#             primos.append(num)
#         num += 1

#     return primos

# print(f"Los primos son: {primeros_n_primos(n)}")

