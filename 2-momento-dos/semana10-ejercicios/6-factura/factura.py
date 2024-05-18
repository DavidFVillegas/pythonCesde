import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Descripción': ['Reparaciones', 'Limpieza', 'Pintura'],
    'Materiales (€)': [100.21, 3.25, 18.00],
    'Mano de Obra (horas)': [2.00, 0.50, 6.00]
}

df = pd.DataFrame(data)


precio_hora_mano_obra = 18.00

df['Mano de Obra (€)'] = df['Mano de Obra (horas)'] * precio_hora_mano_obra
df['Total (€)'] = df['Materiales (€)'] + df['Mano de Obra (€)']
subtotal = df['Total (€)'].sum()

iva = subtotal * 0.16
total_con_iva = subtotal + iva


print(df)


plt.figure(figsize=(10, 6))
plt.plot(df['Descripción'], df['Materiales (€)'], marker='o', label='Materiales (€)')
plt.plot(df['Descripción'], df['Mano de Obra (€)'], marker='o', label='Mano de Obra (€)')

for i, txt in enumerate(df['Materiales (€)']):
    plt.annotate(f'{txt:.2f} €', (df['Descripción'][i], df['Materiales (€)'][i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, txt in enumerate(df['Mano de Obra (€)']):
    plt.annotate(f'{txt:.2f} €', (df['Descripción'][i], df['Mano de Obra (€)'][i]), textcoords="offset points", xytext=(0,-15), ha='center')

plt.title('Factura')
plt.xlabel('Descripción')
plt.ylabel('Euros (€)')
plt.grid(True)
plt.legend(loc='best')
plt.savefig('materiales_mano_obra.png')
plt.show()
