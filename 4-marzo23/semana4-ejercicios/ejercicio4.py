"""
4. Escribir un programa que gestione los pedidos por cobrar de una cafetería, los pedidos se almacenaran en un
diccionario donde la clave de cada pedido es el numero de pedido y el valor el costo del pedido.

- Se debe preguntar si desea añadir un nuevo pedido, pagar el pedido o terminar.
- Si desea añadir un nuevo pedido, se le preguntara el numero del pedido y el costo del pedido y
    se agregara al diccionario.
- Si desea pagar el pedido, se preguntará por el numero de pedido y se eliminará del diccionario.
- Después de cada operación el programa debe mostrar por pantalla la cantidad cobrada hasta el momento de pedidos y
lo que falta por cobrar de los pedidos.
"""

pedidos = {}
total_pagado = 0.0

while True:
    accion = input("¿Desea añadir un nuevo pedido (A), pagar un pedido (P) o terminar (T)? ")

    if accion.upper() == 'A':
        numero_pedido = input("Introduce el número de pedido: ")
        costo_pedido = float(input("Introduce el costo del pedido: "))
        pedidos[numero_pedido] = costo_pedido
    elif accion.upper() == 'P':
        numero_pedido = input("Introduce el número de pedido que deseas pagar: ")
        if numero_pedido in pedidos:
            total_pagado += pedidos[numero_pedido]
            del pedidos[numero_pedido]
        else:
            print("El número de pedido no existe.")
    elif accion.upper() == 'T':
        break
    else:
        print("Acción no reconocida. Por favor, introduce A, P o T.")

    total_cobrado = sum(pedidos.values())
    print(f"Total cobrado hasta el momento: {total_pagado}")
    print(f"Total pendiente de cobro: {total_cobrado}")

"""
Datos de prueba:
A
1
5000

A
2
7000

P
1
T
"""