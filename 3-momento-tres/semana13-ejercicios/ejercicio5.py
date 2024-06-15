import pandas as pd
import matplotlib.pyplot as plt

productos_data = {
    'id_producto': [1, 2, 3, 4, 5],
    'nombre_producto': ['Camiseta', 'Pantalón', 'Zapatos', 'Bolso', 'Gafas de sol'],
    'categoria': ['Ropa', 'Ropa', 'Calzado', 'Accesorios', 'Accesorios'],
    'precio': [20, 35, 50, 80, 40]
}

usuarios_data = {
    'id_usuario': [101, 102, 103, 104, 105],
    'nombre_usuario': ['Ana', 'Juan', 'Maria', 'Carlos', 'Laura']
}

transacciones_data = {
    'id_transaccion': [1001, 1002, 1003, 1004, 1005],
    'id_producto': [1, 3, 2, 4, 5],
    'id_usuario': [101, 103, 102, 105, 104],
    'fecha': ['2024-05-15', '2024-05-12', '2024-05-18', '2024-05-22', '2024-05-13'],
    'cantidad': [2, 1, 1, 1, 3]
}

resenas_data = {
    'id_resena': [2001, 2002, 2003, 2004, 2005],
    'id_producto': [1, 3, 2, 4, 5],
    'id_usuario': [101, 103, 102, 105, 104],
    'calificacion': [4, 5, 3, 4, 5]
}

# Crear DataFrames
df_productos = pd.DataFrame(productos_data)
df_usuarios = pd.DataFrame(usuarios_data)
df_transacciones = pd.DataFrame(transacciones_data)
df_resenas = pd.DataFrame(resenas_data)

# Unir DataFrames
df_transacciones_completas = df_transacciones.merge(df_productos, on='id_producto').merge(df_usuarios, on='id_usuario').merge(df_resenas, on=['id_producto', 'id_usuario'])

# Convertir la columna 'fecha' a datetime
df_transacciones_completas['fecha'] = pd.to_datetime(df_transacciones_completas['fecha'])

# Calcular la tasa de conversión por categoría
df_conversion = df_transacciones_completas.groupby('categoria').size() / df_productos.groupby('categoria').size()

# Gráfico de barras de tasa de conversión
df_conversion.plot(kind='bar')
plt.title('Tasa de Conversión por Categoría de Producto')
plt.ylabel('Tasa de Conversión')
plt.show()

# Calcular la calificación promedio y distribución
calificacion_promedio = df_resenas['calificacion'].mean()
distribucion_calificaciones = df_resenas['calificacion'].value_counts(normalize=True)

print(f'Calificación promedio de los productos: {calificacion_promedio:.2f}')
print('Distribución de calificaciones:')
print(distribucion_calificaciones)

# Calcular ventas mensuales y graficar tendencia
df_transacciones_completas['ventas'] = df_transacciones_completas['precio'] * df_transacciones_completas['cantidad']
ventas_mensuales = df_transacciones_completas.set_index('fecha').resample('M')['ventas'].sum()

plt.figure(figsize=(10, 6))
plt.plot(ventas_mensuales, marker='o')
plt.title('Tendencia de Ventas Mensuales')
plt.xlabel('Mes')
plt.ylabel('Ventas Totales')
plt.show()
