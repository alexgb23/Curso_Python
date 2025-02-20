primero={1,1,2,3,4,4}
segundo={3,4,5,6}

# primero=tuple(primero)
# primero= set(primero)

# print(primero)

# primero.add(5)
# print(primero)

# primero.remove(5)
# print(primero)

# prueba={(1,2,3),4,5,6,(1,2,3)}
# print(prueba)

# tercero=(1,2,3,3)
# tercero= set(tercero)
# print(tercero)

print(f"Union: {primero | segundo} \nIntersección: {primero & segundo} \nDiferencia: {primero - segundo} \nDiferencia simetrica: {primero ^ segundo} \nDiferencia simetrica: {primero | segundo}")
# print(primero.union(segundo))
# print(primero.intersection(segundo))
# print(primero.difference(segundo))
# print(segundo.difference(primero))
