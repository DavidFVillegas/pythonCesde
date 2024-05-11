import pandas as pd

# Crear un dataframe con la información del restaurante
data = {
    'Nombre completo': ['Juan Perez', 'Ana Gomez', 'Carlos Rodriguez', 'Maria Lopez', 'Pedro Torres'],
    'Edad': [30, 25, 35, 28, 32],
    'Cargo': ['Chef', 'Mesero', 'Chef', 'Mesero', 'Chef'],
    'Salario': [3000, 1500, 3200, 1500, 3100],
    'Sede': ['Sede1', 'Sede1', 'Sede2', 'Sede2', 'Sede2']
}
df = pd.DataFrame(data)

# Filtrar el dataframe para mostrar la sede que tiene 3 chefs y 5 meseros
sede_chefs = df[df['Cargo'] == 'Chef']['Sede'].value_counts()
sede_meseros = df[df['Cargo'] == 'Mesero']['Sede'].value_counts()
sede_filtrada = sede_chefs[sede_chefs == 3].index.intersection(sede_meseros[sede_meseros == 5].index)
print(f"Sede con 3 chefs y 5 meseros: {sede_filtrada}")

# Calcular el total de salarios por sede
total_salarios_sede = df.groupby('Sede')['Salario'].sum()
print("Total de salarios por sede:")
print(total_salarios_sede)

# Calcular el promedio de salarios
promedio_salarios = df['Salario'].mean()
print(f"Promedio de salarios: {promedio_salarios}")

# Calcular la suma total de salarios
suma_salarios = df['Salario'].sum()
print(f"Suma total de salarios: {suma_salarios}")

# Guardar el dataframe en un archivo CSV
df.to_csv('informacion_restaurante.csv', index=False)
print("Información del restaurante guardada en 'informacion_restaurante.csv'.")