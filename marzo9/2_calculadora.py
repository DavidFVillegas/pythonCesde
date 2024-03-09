def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir por cero."
    return x / y

def main():
    while True:
        print("Operaciones disponibles:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        seleccion = input("Selecciona una operación (1/2/3/4/5): ")

        if seleccion == '5':
            print("Saliendo del programa...")
            break

        if seleccion in ('1', '2', '3', '4'):
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))

            if seleccion == '1':
                print("Resultado:", sumar(num1, num2))
            elif seleccion == '2':
                print("Resultado:", restar(num1, num2))
            elif seleccion == '3':
                print("Resultado:", multiplicar(num1, num2))
            elif seleccion == '4':
                print("Resultado:", dividir(num1, num2))
        else:
            print("Selección no válida")


if __name__ == "__main__":
    main()
