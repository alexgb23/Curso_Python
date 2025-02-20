punto = {
    "x": 50,
    "y": 20
}

print(punto)
print(punto["x"])
print(punto["y"])

punto.update({"y": 70})
punto["z"] = 30
punto["x"] = 100
print(punto)

# if "lala" in punto:
#     print(punto["lala"])


print(punto.get("lala", 77))
print(punto.get("lala", "No existe"))
print(punto.get("z", 77))


del punto["z"]
del(punto["x"])
print(punto)

punto["x"] = 100
punto["z"] = 30

# for valor in punto:
#     print(valor, punto[valor])

# for valor in punto.items():
#     print(valor)

# for llave, valor in punto.items():
#     print(llave , valor)

# for llave in punto.keys():
#     print(llave)

# for valor in punto.values():
#     print(valor)


# punto.clear()
# print(punto)