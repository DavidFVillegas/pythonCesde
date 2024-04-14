import pandas as pd

datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [100, 150, 200, 180, 220]
}

df = pd.DataFrame(datos)

primer_trimestre = df[df['Mes'].isin(['Enero', 'Febrero', 'Marzo'])]

total_ventas = primer_trimestre['Ventas'].sum()

print(total_ventas)
