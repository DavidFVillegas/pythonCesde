"""
4. Adivina el número: Escribe un programa que genere un número aleatorio
    entre 1 y 100(importar librería random), y que le pida al usuario adivinarlo.
    El programa debe indicar si el número ingresado por el usuario es
    mayor, menor o igual al número generado.

    El usuario debe tener 3 intentos para adivinar el número. Ejem: aleatorio = random.randint(1,100)
"""

import random

# Generar un número aleatorio entre 1 y 100
numero_aleatorio = random.randint(1, 100)

# Inicializar el número de intentos
intentos = 0

while intentos < 3:
    # Pedir al usuario que adivine el número
    numero_usuario = int(input("Adivina el número entre 1 y 100: "))
    intentos += 1

    # Indicar si el número ingresado por el usuario es mayor, menor o igual al número generado
    if numero_usuario < numero_aleatorio:
        print("El número ingresado es menor al número generado.")
    elif numero_usuario > numero_aleatorio:
        print("El número ingresado es mayor al número generado.")
    else:
        print("¡Has adivinado el número!")
        break

if intentos == 3 and numero_usuario != numero_aleatorio:
    print("Has agotado tus intentos. El número era", numero_aleatorio)