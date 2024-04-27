import pandas as pd

datos = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Sandra'],
    'Edad': [40, 25, 47, 28],
    'Ciudad': ['Bogota', 'Medellin', 'Cali', 'Armenia']
}

df = pd.DataFrame(datos)

print(df)
