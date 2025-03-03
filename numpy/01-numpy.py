import numpy as np
import time

# lista=[1,2,3,4,5]
# array=np.array(lista)

# lista_doble= [x*2 for x in lista]
# print(array*2)

# array_doble= array*2
# print(array_doble)


# array2=np.array([10,20,30,40,50])
# array +=5

# print(array)

# array2 *=3

# print(array2)

"""Comparar rendimiento
Crear una lista de 1 millon de valores
Crear un array de 1 millon de valores
Usar una funcion de tiempo para calcular lavelocidad de calculo
"""

n=10**6

lista=list(range(n))
array=np.arange(n)

inicio=time.time()
lista2=[x*2 for x in lista]
end=time.time()
print(f"Tiempo con listas:{end-inicio:.5f} segundos")

array2=array*2
inicio=time.time()
array2*=2
end=time.time()
print(f"Tiempo con arrays:{end-inicio:.5f} segundos")