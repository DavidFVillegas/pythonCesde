"""
4. Se tiene un código, número de artículos vendidos y el valor de cada artículo.
Calcule el valor de la compra, tiendo en cuenta lo siguiente:
compra 50 o más artículos se le da al cliente 10% de descuento;
si la compra es menor de 50 artículos no se hace descuento.
Mostrar el código, el total de la venta y el valor del descuento.
"""

codigo_producto = input("Ingrese el código del producto: ")
numero_articulos = int(input("Ingrese el número de artículos vendidos: "))
valor_articulo = float(input("Ingrese el valor de cada artículo: "))

total_sin_descuento = numero_articulos * valor_articulo

if numero_articulos >= 50:
    descuento = total_sin_descuento * 0.10
    total_con_descuento = total_sin_descuento - descuento
else:
    descuento = 0
    total_con_descuento = total_sin_descuento

print(f"Código producto: {codigo_producto}, Total venta: {total_con_descuento}, Descuento: {descuento}")

"""
Caso de prueba 1: Compra de 50 o más artículos
Código del producto: 001
Número de artículos vendidos: 50
Valor de cada artículo: 100

Caso de prueba 2: Compra de menos de 50 artículos
Código del producto: 002
Número de artículos vendidos: 30
Valor de cada artículo: 100
"""