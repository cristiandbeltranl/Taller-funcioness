SALARIO_MINIMO = 1300000
AUXILIO_TRANSPORTE = 162000


def calcular_nomina_15_dias(sueldo_mensual: float) -> tuple[float, float, float]:
    pago_15_dias = sueldo_mensual / 2
    auxilio_15_dias = 0.0

    if sueldo_mensual <= 2 * SALARIO_MINIMO:
        auxilio_15_dias = AUXILIO_TRANSPORTE / 2

    total = pago_15_dias + auxilio_15_dias
    return pago_15_dias, auxilio_15_dias, total


def main():
    try:
        sueldo = float(input("Ingresa el sueldo mensual: ").strip())
        if sueldo <= 0:
            print("El sueldo debe ser mayor que cero.")
            return
    except ValueError:
        print("Debes ingresar un numero valido para el sueldo.")
        return

    pago, auxilio, total = calcular_nomina_15_dias(sueldo)
    print(f"Pago por 15 dias: ${pago:,.2f}")
    print(f"Auxilio de transporte (15 dias): ${auxilio:,.2f}")
    print(f"Total a pagar: ${total:,.2f}")


if __name__ == "__main__":
    main()
