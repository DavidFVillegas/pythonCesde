import pandas as pd
import matplotlib.pyplot as plt

# Leer los datos desde el archivo CSV
df = pd.read_csv('movimientos.csv')

# Crear el gráfico de columnas
plt.figure(figsize=(10,6))
plt.bar(df['MES'], df['INGRESOS'], label='Ingresos')
plt.bar(df['MES'], df['GASTOS'], label='Gastos')

# Añadir títulos y etiquetas
plt.title('Ingresos y Gastos por Mes')
plt.xlabel('Mes')
plt.ylabel('Cantidad')
plt.legend()

# Rotar las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()