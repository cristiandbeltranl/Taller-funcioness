import re


def validar_correo(correo: str) -> bool:
    patron = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"
    return bool(re.match(patron, correo))


def main():
    correo = input("Ingresa un correo electronico: ").strip()

    if validar_correo(correo):
        print("Correo valido.")
    else:
        print("Correo invalido.")


if __name__ == "__main__":
    main()
