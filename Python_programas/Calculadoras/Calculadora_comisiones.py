
def calculadora_comisiones(nombre, ventas, porcentaje):

    comision = round((ventas*(porcentaje/100)),2)
    
    return comision


def main():
    try:
        nombre = input("Ingresa tu nombre:")
        ventas = float(input("Ingrese el monto de sus ventas del mes actual:"))
        porcentaje = float(input("Ingrese su porcentaje de comisioón:"))
        
        comision_calculada = calculadora_comisiones(nombre, ventas, porcentaje)
        print(f"Hola {nombre}, su comisión del mes actual es de: {comision_calculada:.2f}")
    except ValueError:
        print("Por favor ingrese valores numéricos válidos.")


if __name__ == "__main__":
    main()