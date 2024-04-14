import pandas as pd

# Crear un diccionario con los datos de la tabla de posiciones del futbol colombiano 2024
datos = {
    'Posición': list(range(1, 21)),
    'Equipo': ['Atlético Bucaramanga', 'Deportes Tolima', 'Independiente Santa Fe', 'Deportivo Pereira', 'Once Caldas',
               'La Equidad', 'Junior', 'América de Cali', 'Fortaleza CEIF', 'Atlético Nacional', 'Millonarios',
               'Independiente Medellín', 'Jaguares de Córdoba', 'Águilas Doradas', 'Deportivo Cali', 'Envigado',
               'Deportivo Pasto', 'Boyacá Chicó', 'Alianza', 'Patriotas Boyacá'],
    'Jugados': [15, 16, 16, 16, 16, 15, 16, 16, 16, 16, 15, 15, 16, 16, 16, 16, 15, 15, 15, 15],
    'Victorias': [9, 9, 8, 8, 8, 7, 7, 6, 6, 5, 5, 5, 4, 5, 4, 3, 4, 4, 3, 3],
    'Derrotas': [1, 2, 4, 4, 4, 3, 5, 5, 6, 6, 6, 6, 6, 8, 8, 6, 8, 8, 8, 9],
    'Empates': [5, 5, 4, 4, 4, 5, 4, 5, 4, 5, 4, 4, 6, 3, 4, 7, 3, 3, 4, 3],
    'Diferencia de goles': [13, 12, 9, 7, 2, 6, 3, 7, 0, 0, 2, -12, -3, -4, -2, -5, -7, -9, -7, -12],
    'Puntos': [32, 32, 28, 28, 28, 26, 25, 23, 22, 20, 19, 19, 18, 18, 16, 16, 15, 15, 13, 12],
}

# Crear el DataFrame a partir del diccionario
df = pd.DataFrame(datos)

print(df)

# https://www.winsports.co/posiciones/liga-betplay-dimayor-2024-i
