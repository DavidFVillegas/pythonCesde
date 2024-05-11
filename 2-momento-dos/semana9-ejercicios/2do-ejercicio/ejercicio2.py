import pandas as pd

# Cargar el archivo CSV en un dataframe
df = pd.read_csv('temperaturas.csv')

# Mostrar las últimas 5 filas del dataframe
print(df.tail())

# Mostrar los nombres de las columnas
print(df.columns)

# Calcular y mostrar la mediana de cada columna de temperaturas
medianas_temperaturas = df.median()
print("Medianas de temperaturas:")
print(medianas_temperaturas)

# Calcular y mostrar la varianza de cada columna de temperaturas
varianza_temperaturas = df.var()
print("Varianzas de temperaturas:")
print(varianza_temperaturas)

# Filtrar y mostrar las filas donde la Temperatura 2 es menor que 26 grados
filtro_temperatura_2 = df[df['Temperatura 2'] < 26]
print("Filtrado por Temperatura 2 menor que 26 grados:")
print(filtro_temperatura_2)

# Calcular y mostrar la covarianza entre las columnas de temperaturas
covarianza_temperaturas = df.cov()
print("Covarianza entre temperaturas:")
print(covarianza_temperaturas)

# Crear una nueva columna que sea la mediana de las tres temperaturas y mostrar el dataframe
df['Mediana_temperaturas'] = df.median(axis=1)
print("DataFrame con nueva columna de mediana de temperaturas:")
print(df)

# Ordenar el dataframe por la Temperatura 3 de forma ascendente y mostrar el dataframe
df_ordenado = df.sort_values(by='Temperatura 3', ascending=True)
print("DataFrame ordenado por Temperatura 3 de forma ascendente:")
print(df_ordenado)

# Guardar el dataframe ordenado en un archivo CSV
df_ordenado.to_csv('temperaturas_ordenadas.csv', index=False)
print("DataFrame ordenado guardado en 'temperaturas_ordenadas.csv'.")

# Calcular y mostrar la temperatura mínima de cada columna de temperaturas
temperatura_minima_Temperatura1 = df['Temperatura 1'].min()
temperatura_minima_Temperatura2 = df['Temperatura 2'].min()
temperatura_minima_Temperatura3 = df['Temperatura 3'].min()

print(f"Temperatura mínima en Temperatura 1: {temperatura_minima_Temperatura1} grados")
print(f"Temperatura mínima en Temperatura 2: {temperatura_minima_Temperatura2} grados")
print(f"Temperatura mínima en Temperatura 3: {temperatura_minima_Temperatura3} grados")

# Calcular y mostrar la suma de cada columna de temperaturas
suma_Temperatura1 = df['Temperatura 1'].sum()
suma_Temperatura2 = df['Temperatura 2'].sum()
suma_Temperatura3 = df['Temperatura 3'].sum()

print(f"Suma en Temperatura 1: {suma_Temperatura1} grados")
print(f"Suma en Temperatura 2: {suma_Temperatura2} grados")
print(f"Suma en Temperatura 3: {suma_Temperatura3} grados")

# Calcular y mostrar la suma acumulada de cada columna de temperaturas
suma_acumulada = df.cumsum()
print("Suma acumulada por columna:")
print(suma_acumulada)