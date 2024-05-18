import matplotlib.pyplot as plt
import pandas as pd

# Leer los datos desde el archivo CSV
df = pd.read_csv('hotel-miramar.csv')

# Calcular la cantidad de días de estancia para cada cliente
dias_estancia = df.groupby('Cliente')['Días de estancia'].sum()

# Crear el gráfico de pastel
plt.figure(figsize=(10,6))
plt.pie(dias_estancia, labels=dias_estancia.index, autopct='%1.1f%%')

# Añadir un título
plt.title('Distribución de los días de estancia de los clientes')

# Mostrar el gráfico
plt.show()