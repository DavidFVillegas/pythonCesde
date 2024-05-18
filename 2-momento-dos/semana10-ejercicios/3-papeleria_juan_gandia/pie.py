import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Cod.': [10, 40, 3, 5, 30, 1, 21],
    'Nombre': ['Libreta-50', 'Agenda-2002', 'Portafolios', 'Agenda-2003', 'Libreta-100', 'Lápiz-08', 'Lápiz-09'],
    'Precio Unitario': [8.20, 13.45, 20.40, 15.00, 2.84, 0.50, 0.50],
    'Proveedor': ['AGISA', 'CETESA', 'CETESA', 'PAPELSA', 'PAPELSA', 'CETESA', 'CETESA'],
    'Cantidad': [150, 50, 75, 75, 90, 120, 120]
}


df = pd.DataFrame(data)
df['Precio'] = df['Precio Unitario'] * df['Cantidad']
total = df['Precio'].sum()
iva = total * 0.16
precio_final = total + iva

df.to_csv('datos.csv', index=False)

plt.figure(figsize=(8, 8))
plt.pie(df['Precio'], labels=df['Nombre'], autopct='%1.1f%%', startangle=140)
plt.title('Papelería Juan Gandía')
plt.axis('equal')


plt.savefig('papleria_juan_gandia_pie.png')

plt.show()


print(f'Total: {total:.2f} €')
print(f'IVA (16%): {iva:.2f} €')
print(f'Precio Final: {precio_final:.2f} €')

