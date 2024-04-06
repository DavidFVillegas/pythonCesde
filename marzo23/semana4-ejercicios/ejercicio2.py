"""
2. Aplíquele los métodos trabajados (obtener un elemento, actualizarlo, agregarle dos elementos, eliminar el ultimo y
el primero, ordena la lista)
"""

# Lista inicial de frutas favoritas
frutas_favoritas = ["Mango", "Fresa", "Kiwi", "Manzana", "Plátano"]
print(frutas_favoritas)

# Obtener un elemento (el tercer fruto de la lista)
fruta_obtenida = frutas_favoritas[2]
print(fruta_obtenida)  # Kiwi

# Actualizar un elemento (cambiar "Fresa" por "Uva")
frutas_favoritas[1] = "Uva"
print(frutas_favoritas[1])  # Uva

# Agregar dos elementos
frutas_favoritas.append("Pera")
frutas_favoritas.append("Sandía")
print(frutas_favoritas)

# Eliminar el último elemento
frutas_favoritas.pop()
print(frutas_favoritas)

# Eliminar el primer elemento
frutas_favoritas.pop(0)
print(frutas_favoritas)

# Ordenar la lista
frutas_favoritas.sort()
print(frutas_favoritas)

