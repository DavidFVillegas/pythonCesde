"""
6. Crea una lista vacía llamada departamentos Colombia, pida al usuario la
    cantidad de departamentos a ingresar, a través de un ciclo for pida al usuario
    que ingrese el departamento de Colombia que desee, agregue esta información
    a la lista y luego esta sea ordenada en orden descendente.

    a. Se debe imprimir la lista con los valores organizados de forma descendentes.
    b. Debe imprimir además los 2 últimos departamentos ingresados
"""

# Crear una lista vacía llamada departamentos_colombia
departamentos_colombia = []

# Pedir al usuario la cantidad de departamentos a ingresar
cantidad = int(input("¿Cuántos departamentos quieres ingresar? "))

# A través de un ciclo for, pedir al usuario que ingrese el departamento de Colombia que desee
for i in range(cantidad):
    departamento = input("Ingresa un departamento de Colombia: ")
    departamentos_colombia.append(departamento)

# Ordenar la lista en orden descendente
departamentos_colombia.sort(reverse=True)

# Imprimir la lista con los valores organizados de forma descendente
print("Departamentos ordenados de forma descendente:", departamentos_colombia)

# Imprimir los 2 últimos departamentos ingresados
print("Los dos últimos departamentos ingresados son:", departamentos_colombia[-2:])

"""
Prueba: Ingresar 3 departamentos
Cantidad: 3
Departamentos: "Antioquia", "Bogotá", "Cundinamarca"
Esperado: 
"Departamentos ordenados de forma descendente: ['Cundinamarca', 'Bogotá', 'Antioquia']"
"Los dos últimos departamentos ingresados son: ['Bogotá', 'Antioquia']"
"""