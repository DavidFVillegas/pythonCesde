"""
    1. Una agencia de alquiler de autos cobra la hora de uso del vehículo a un valor determinado.
    Si el cliente usa el carro por más de 10 horas, le hacen un descuento del 20% por cada hora de más.
    Haga un programa que lea horas de uso, valor hora, y determine el total a pagar.
"""

# 1. Solicitar al usuario las horas de uso y el valor por hora
horas_uso = float(input("Ingrese las horas de uso del vehículo: "))
valor_hora = float(input("Ingrese el valor por hora del vehículo: "))

# 2. Verificar si las horas de uso exceden las 10 horas
if horas_uso <= 10:
    # 3. Calcular el costo total para 10 horas o menos
    total_pagar = horas_uso * valor_hora
else:
    # 4. Calcular el costo para más de 10 horas
    horas_extra = horas_uso - 10
    descuento_hora = valor_hora * 0.2
    total_pagar = (10 * valor_hora) + (horas_extra * (valor_hora - descuento_hora))

# 5. Mostrar el total a pagar
print(f"El total a pagar es: {total_pagar}")

"""
    Probar con 5 horas y valor hora $1000
    Probar con 12 horas y valor hora $1000
"""