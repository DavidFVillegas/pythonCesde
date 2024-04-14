# 3. Lea dos números NRO1 y NRO2 y escriba ambos números sólo si son de diferente signo y distintos de cero.

NR01 = float(input("Ingrese el primer número: "))
NR02 = float(input("Ingrese el segundo número: "))

if (NR01 * NR02 < 0) and (NR01 != 0 and NR02 != 0):
    print(f"Ambos números, {NR01} y {NR02}, son de distinto signo y distintos de cero.")
else:
    print(f"Los números {NR01} y {NR02} no cumplen con las condiciones de ser de distinto signo y distintos de cero.")

"""
Caso de prueba 1: 
NRO1 = -5
NRO2 = 10

Caso de prueba 2:
NRO1 = 5
NRO2 = 10

Caso de prueba 3:
NRO1 = -5
NRO2 = -10

Caso de prueba 4:
NRO1 = 0
NRO2 = 10
"""
