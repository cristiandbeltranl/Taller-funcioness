def guardar_diez_palabras(nombre_archivo: str = "palabras.txt"):
    palabras = []
    print("Ingresa 10 palabras:")

    while len(palabras) < 10:
        palabra = input(f"Palabra {len(palabras) + 1}: ").strip()
        if not palabra:
            print("La palabra no puede estar vacia.")
            continue
        palabras.append(palabra)

    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        for palabra in palabras:
            archivo.write(palabra + "\n")

    print(f"Se guardaron 10 palabras en '{nombre_archivo}'.")


if __name__ == "__main__":
    guardar_diez_palabras()
