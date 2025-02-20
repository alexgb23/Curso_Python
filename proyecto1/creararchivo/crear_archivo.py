archivo_txt = "texto_usuario.txt"
print("Escribe el texto que deseas guardar en el archivo")
print("Escribe 'SALIR' para salir")

with open(archivo_txt, mode="a", encoding="utf-8") as archivo:
    while True:
        texto = input("Escribe el texto:")
        if texto.strip().upper() == "SALIR":
            print(f"texto guardado en el archivo {archivo_txt}")
            break
        archivo.write(texto+"\n")
        print("texto añadido. Escribe mas texto o 'SALIR' para salir")
    archivo.close()


