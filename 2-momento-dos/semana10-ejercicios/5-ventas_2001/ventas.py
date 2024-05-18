import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Vendedor': [
        'Giovanna Santiago', 'Teresa Losada', 'José Luis Jimenez',
        'Cristina Rodriguez', 'Ana Alcolea', 'Emma Berzal', 'Celia Pulido'
    ],
    'T1': [12452, 14785, 21458, 21479, 32547, 32584, 21548],
    'T2': [12587, 25987, 32568, 32569, 65847, 65988, 21548],
    'T3': [25412, 25413, 45987, 32654, 98752, 32564, 69841],
    'T4': [25478, 56987, 21547, 32569, 25489, 65412, 98752]
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
df.to_csv('ventas.csv', index=False)

df['Total por Vendedor'] = df[['T1', 'T2', 'T3', 'T4']].sum(axis=1)
total_por_trimestre = df[['T1', 'T2', 'T3', 'T4']].sum()
df.loc['Total por Trimestre'] = df[['T1', 'T2', 'T3', 'T4']].sum()

plt.figure(figsize=(10, 7))
plt.pie(df['Total por Vendedor'][:-1], labels=df['Vendedor'][:-1], autopct='%1.1f%%', startangle=140)
plt.title('Ventas efectuadas en 2001')
plt.axis('equal')
plt.savefig('total_ventas_vendedor.png')
plt.show()