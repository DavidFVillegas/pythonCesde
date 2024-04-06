# Se desea calcular la distancia recorrida (m) por un móvil que tiene velocidad constante (m/s) durante un tiempo t(s)
#
# v = distancia / tiempo
#
# distancia = velocidad * tiempo

def calcular_distancia(velocidad, tiempo):

    distancia = velocidad * tiempo
    return distancia


# Solicitar al usuario la velocidad y el tiempo
velocidad = float(input("Ingrese la velocidad del móvil en m/s: "))
tiempo = float(input("Ingrese el tiempo durante el cual se mueve el móvil en segundos: "))

# Calcular y mostrar la distancia
distancia = calcular_distancia(velocidad, tiempo)
print(f"La distancia recorrida por el móvil es: {distancia} metros")