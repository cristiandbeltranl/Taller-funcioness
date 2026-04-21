inventario = [
    {"talla": 38, "color": "negro", "tipo": "tenis"},
    {"talla": 39, "color": "blanco", "tipo": "deportivo"},
    {"talla": 40, "color": "cafe", "tipo": "formal"},
    {"talla": 37, "color": "rojo", "tipo": "sandalia"},
    {"talla": 41, "color": "negro", "tipo": "bota"},
]


def disponible(talla: int, color: str, tipo: str) -> bool:
    color = color.lower().strip()
    tipo = tipo.lower().strip()

    for zapato in inventario:
        if (
            zapato["talla"] == talla
            and zapato["color"] == color
            and zapato["tipo"] == tipo
        ):
            return True
    return False


def main():
    try:
        talla = int(input("Ingresa la talla: ").strip())
    except ValueError:
        print("La talla debe ser un numero entero.")
        return

    color = input("Ingresa el color: ").strip()
    tipo = input("Ingresa el tipo de zapato: ").strip()

    if disponible(talla, color, tipo):
        print("El zapato SI esta disponible en inventario.")
    else:
        print("El zapato NO esta disponible en inventario.")


if __name__ == "__main__":
    main()
