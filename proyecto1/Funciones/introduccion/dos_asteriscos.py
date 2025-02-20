def productos(**datos):
    print(datos)

# productos(Producto1="Camisa", Producto2="Pantalon", Producto3="Zapatos")


def show_info(**datos):
    print("Tipo Datos: ", type(datos))
    print("Contenido de Datos: ", datos)

# show_info(Producto1="Camisa", Producto2="Pantalon", Producto3="Zapatos")


def mostrar_info(**datos):
    for key, value in datos.items():
        print(f"{key}: {value}")

# Con este foreach se muestran las claves y los valores
# mostrar_info(Producto1="Camisa", Producto2="Pantalon", Producto3="Zapatos")


def mostrar_detalles(**datos):
    for data in datos:
        print(data)

# Con este foreach solo se muestran las claves
# mostrar_detalles(Producto1="Camisa", Producto2="Pantalon", Producto3="Zapatos")


def informacion(palabra, *arg, **kwargs):
    print("Contenido de la Variable: ", palabra)
    print("Datos posicionales: ", arg)
    print("Datos nombrados: ", kwargs)


informacion("Informacion", 1, 2, 3, Producto1="Camisa",
            Producto2="Pantalon", Producto3="Zapatos")
