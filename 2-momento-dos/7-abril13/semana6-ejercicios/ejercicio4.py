"""
4. Escribir un programa que pregunte al usuario por las ventas de un rango de años y muestre por pantalla una serie
    con los datos de las ventas indexada por los años, antes y después de aplicarles un descuento del 10%. .
"""

import pandas as pd

inicio = int(input("Ingrese el año de inicio: "))
fin = int(input("Ingrese el año de fin: "))

ventas = {}
for year in range(inicio, fin+1):
    ventas[year] = float(input(f"Ingrese las ventas del año {year}: "))

serie_ventas = pd.Series(ventas)

print("Ventas antes del descuento:")
print(serie_ventas)

serie_ventas_con_descuento = serie_ventas * 0.9

print("\nVentas despues del descuento:")
print(serie_ventas_con_descuento)

"""
Datos de prueba 1:
Ingrese el año de inicio: 2010
Ingrese el año de fin: 2012
Ingrese las ventas del año 2010: 1000
Ingrese las ventas del año 2011: 2000
Ingrese las ventas del año 2012: 3000

Datos de prueba 2:
Ingrese el año de inicio: 2000
Ingrese el año de fin: 2000
Ingrese las ventas del año 2000: 5000
"""