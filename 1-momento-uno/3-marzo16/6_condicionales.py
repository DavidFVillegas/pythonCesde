# Ejemplo de uso de if
temperatura = 30
if temperatura > 25:
    print("Hace calor fuera")

# Ejemplo de uso de if con else
velocidad = 70
if velocidad > 100:
    print("Vas demasiado rápido")
else:
    print("Velocidad dentro del límite")

# Ejemplo de uso de if con elif y else
calificacion = 2.0
if calificacion >= 4.7:
    print("Excelente")
elif calificacion >= 3.5:
    print("Muy bien")
else:
    print("Necesitas estudiar más")

"""
    Se tienen cuatro esferas de las cuales tres son de igual peso y una es de diferente peso.
    Muestre el peso de la esfera diferente y si es más pesada o más ligera.
"""



def encontrar_esfera_diferente(pesos):

    if pesos[0] == pesos[1]:
        esfera_diferente = 2 if pesos[0] != pesos[2] else 3
    elif pesos[0] == pesos[2]:
        esfera_diferente = 1
    else:
        esfera_diferente = 0

    if esfera_diferente == 3 or (esfera_diferente < 3 and pesos[esfera_diferente] != pesos[3]):
        referencia = 0 if esfera_diferente > 0 else 1
        es_mas_pesada = pesos[esfera_diferente] > pesos[referencia]
    else:
        es_mas_pesada = False
    return esfera_diferente, "más pesada" if es_mas_pesada else "más ligera"

casos = [
    [45, 50, 50, 50],
    [50, 45, 50, 50],
    [50, 50, 45, 50],
    [50, 50, 50, 45]
]

for pesos in casos:
    esfera_diferente, descripcion = encontrar_esfera_diferente(pesos)
    print(f"En {pesos}, la esfera diferente es la número {esfera_diferente + 1} y es {descripcion}.")




