import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio'],
    'Volumen de Ventas (€)': [247.00, 333.00, 548.00, 254.00, 751.00, 457.00],
    'Ingresos por Ventas (€)': [214.25, 654.21, 458.25, 325.54, 584.21, 874.24]
}

df = pd.DataFrame(data)
costes_fijos = 7.25


df['Costes Fijos (€)'] = costes_fijos
df['Costes Variables (€)'] = df['Volumen de Ventas (€)'] * 0.60
df['Costes Totales (€)'] = df['Costes Variables (€)'] + df['Costes Fijos (€)']
df['Beneficios (€)'] = df['Ingresos por Ventas (€)'] - df['Costes Totales (€)']

print(df)

plt.figure(figsize=(12, 7))
df.plot(x='Mes', y=['Costes Fijos (€)', 'Costes Variables (€)', 'Costes Totales (€)', 'Beneficios (€)'], kind='bar')
plt.title('Costes y Beneficios por Mes')
plt.xlabel('Mes')
plt.ylabel('Euros (€)')
plt.grid(True)
plt.legend(loc='best')
plt.savefig('costes_beneficios.png')
plt.show()
