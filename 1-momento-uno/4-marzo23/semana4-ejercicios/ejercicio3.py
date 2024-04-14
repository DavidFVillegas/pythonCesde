# 3. Crea un juego parecido a piedra, papel o tijeras,
#  algo así como adivina la respuesta correcta o lo que se te ocurra.

import random


def juego_adivinanza():
    numero_secreto = random.randint(1, 10)
    intentos = 0

    print("Bienvenido al juego de adivinanzas!")
    print("Estoy pensando en un número entre 1 y 10.")

    while True:
        intentos += 1
        adivinanza = int(input("Por favor, introduce tu adivinanza: "))

        if adivinanza < numero_secreto:
            print("Demasiado bajo!")
        elif adivinanza > numero_secreto:
            print("Demasiado alto!")
        else:
            print(f"Felicidades! Has adivinado el número en {intentos} intentos.")
            break


juego_adivinanza()
