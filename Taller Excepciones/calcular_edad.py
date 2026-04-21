from datetime import datetime


def calcular_edad(fecha_nacimiento: str) -> int:
    fecha = datetime.strptime(fecha_nacimiento, "%Y-%m-%d").date()
    hoy = datetime.today().date()

    edad = hoy.year - fecha.year
    if (hoy.month, hoy.day) < (fecha.month, fecha.day):
        edad -= 1
    return edad


def main():
    fecha_nacimiento = input("Ingresa fecha de nacimiento (AAAA-MM-DD): ").strip()

    try:
        edad = calcular_edad(fecha_nacimiento)
        if edad < 0:
            print("La fecha ingresada no es valida (es futura).")
            return
        print(f"La persona tiene {edad} anios.")
    except ValueError:
        print("Formato invalido. Debe ser AAAA-MM-DD.")


if __name__ == "__main__":
    main()
