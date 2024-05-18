import matplotlib.pyplot as plt
import pandas as pd

# Leer los datos desde el archivo CSV
df = pd.read_csv('hotel-miramar.csv')

# Extraer los nombres de los clientes y los precios de la estancia
clientes = df['Cliente']
precios = df['Precio']

# Crear el gráfico
plt.figure(figsize=(10,6))
plt.plot(clientes, precios, marker='o')

# Añadir títulos y etiquetas
plt.title('Precios de estancia por cliente')
plt.xlabel('Cliente')
plt.ylabel('Precio')

# Rotar las etiquetas del eje x para una mejor visualización
plt.xticks(rotation=45)

# Mostrar el gráfico
plt.show()