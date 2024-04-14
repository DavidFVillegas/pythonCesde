import pandas as pd

datos = {
    'Nombre': ['Juan', 'Maria', 'Pedro', 'Sandra'],
    'Ciencias': [4.5, 5.0, 4.8, 4.7],
    'Matemáticas': [2.5, 1.5, 2.6, 1.9],
    'Historia': [5.0, 4.0, 2.0, 4.9]
}

df = pd.DataFrame(datos)

df['Promedio'] = df[['Ciencias', 'Matemáticas', 'Historia']].mean(axis=1)

print(df)
