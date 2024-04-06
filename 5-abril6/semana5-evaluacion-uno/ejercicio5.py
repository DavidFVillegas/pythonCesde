"""
5. Solicitar al usuario cuánto dinero quiere ingresar al CDT y cuánto tiempo
    (este debe ser mayor a 3 meses (90 días) y menor a 2 años (720 días)).
    Si el ahorro es por 90 días los intereses serán 3.14% de lo ahorrado,
    si esta entre 91 y 180 días el interés es 4.85% y si es entre 181 a 360 días
    los intereses son de 5.75%. mostrar cuanto ganaría el usuario según el
    plazo aplicado al CDT.
"""

# Solicitar al usuario cuánto dinero quiere ingresar al CDT
dinero = float(input("¿Cuánto dinero quieres ingresar al CDT? "))

# Solicitar al usuario cuánto tiempo quiere mantener el dinero en el CDT
tiempo = int(input("¿Por cuántos días quieres mantener el dinero en el CDT? "))

# Validar que el tiempo ingresado esté entre 90 y 720 días
if tiempo < 90 or tiempo > 720:
    print("El tiempo debe ser mayor a 3 meses (90 días) y menor a 2 años (720 días).")
else:
    # Calcular los intereses ganados según el tiempo ingresado
    if tiempo == 90:
        intereses = dinero * 0.0314
    elif tiempo <= 180:
        intereses = dinero * 0.0485
    else:
        intereses = dinero * 0.0575

    # Mostrar cuánto ganaría el usuario según el plazo aplicado al CDT
    print(f"Ganarías {intereses} en intereses.")

"""
Prueba 1: Ahorro por 90 días
Dinero: 1000000
Tiempo: 90
Esperado: "Ganarías 31399.99 en intereses."

Prueba 2: Ahorro por 180 días
Dinero: 1000000
Tiempo: 180
Esperado: "Ganarías 48500.0 en intereses."

Prueba 3: Ahorro por 360 días
Dinero: 1000000
Tiempo: 360
Esperado: "Ganarías 57500.0 en intereses."

Prueba 4: Tiempo fuera de rango
Dinero: 1000000
Tiempo: 80
Esperado: "El tiempo debe ser mayor a 3 meses (90 días) y menor a 2 años (720 días)."
"""