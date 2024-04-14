import pandas as pd

datos = {
    'Mes': ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo'],
    'Ventas': [100, 150, 200, 180, 220]
}

df = pd.DataFrame(datos)

print(df)
