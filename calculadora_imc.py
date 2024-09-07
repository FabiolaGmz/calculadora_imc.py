def validar_numero(mensaje, tipo_dato):
    while True:
        try:
            valor = tipo_dato(input(mensaje))
            return valor
        except ValueError:
            print(f"Por favor, ingrese un valor numérico válido para {mensaje.lower()}.")

def validar_no_vacio(mensaje):
    while True:
        valor = input(mensaje).strip()
        if valor:
            return valor
        else:
            print("Este campo no puede estar vacío. Por favor, ingrese un valor.")

def calcular_imc(peso, estatura):
    return round(peso / estatura ** 2, 2)

def clasificar_imc(imc):
    if imc < 16.00:
        return "Delgadez severa"
    elif 16.00 <= imc < 17.00:
        return "Delgadez moderada"
    elif 17.00 <= imc < 18.50:
        return "Delgadez leve"
    elif 18.50 <= imc < 25.00:
        return "Normal"
    elif 25.00 <= imc < 30.00:
        return "Sobrepeso"
    elif 30.00 <= imc < 35.00:
        return "Obesidad leve"
    elif 35.00 <= imc < 40.00:
        return "Obesidad media"
    else:
        return "Obesidad mórbida"

def main():
    print("Por favor, proporcione la siguiente información:")

    nombre = validar_no_vacio("Nombre: ")
    apellido_paterno = validar_no_vacio("Apellido Paterno: ")
    apellido_materno = validar_no_vacio("Apellido Materno: ")
    edad = validar_numero("Edad en años: ", int)
    peso = validar_numero("Peso en kilogramos: ", float)
    estatura = validar_numero("Estatura en metros: ", float)

    imc = calcular_imc(peso, estatura)
    clasificacion = clasificar_imc(imc)

    if edad < 18:
        print("Usted es menor de edad.")
    else:
        print("Usted es mayor de edad.")

    print(f"Nombre: {nombre} {apellido_paterno} {apellido_materno}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Estatura: {estatura} m")
    print(f"Índice de Masa Corporal (IMC): {imc}")
    print(f"Clasificación: {clasificacion}")

if __name__ == "__main__":
    main()
