import pandas as pd

# Cargar el archivo ventas.csv en un dataframe
df = pd.read_csv('ventas.csv')

# Mostrar las primeras 5 filas del dataframe
print(df.head())

# Mostrar el número total de filas y columnas en el dataframe
print(f'Número de filas: {df.shape[0]}')
print(f'Número de columnas: {df.shape[1]}')

# Verificar si hay valores nulos en el dataframe y mostrar la cantidad de valores nulos por columna
print(df.isnull().sum())

# Calcular la suma total de ventas (columna “ventas”) en todas las transacciones
total_ventas = df['ventas'].sum()
print(f'Suma total de ventas: {total_ventas}')

# Calcular el promedio de ventas por mes
promedio_ventas_mes = df.groupby('mes')['ventas'].mean()
print(f'Promedio de ventas por mes: \n{promedio_ventas_mes}')

# Encontrar el producto más vendido y la cantidad total vendida de ese producto
producto_mas_vendido = df.groupby('producto')['ventas'].sum().idxmax()
total_vendido_producto = df.groupby('producto')['ventas'].sum().max()
print(f'Producto más vendido: {producto_mas_vendido} con un total de {total_vendido_producto} vendidos')

# Crear un nuevo dataframe que contenga solo las ventas de productos en la categoría “Electronica”
df_electronica = df[df['categoria'] == 'Electronica']

# Guardar el nuevo dataframe en un archivo csv llamado “Ventas_electronica.csv”
df_electronica.to_csv('Ventas_electronica.csv', index=False)