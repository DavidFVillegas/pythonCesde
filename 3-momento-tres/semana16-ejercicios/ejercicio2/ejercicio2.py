import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Crear datos
np.random.seed(42)  # Para reproducibilidad

num_ubicaciones = 5
num_horas = 24 * 7  # Datos para una semana

data = {
    'fecha_hora': pd.date_range('2024-01-01', periods=num_horas, freq='H'),
    'ubicacion': np.random.choice(['A', 'B', 'C', 'D', 'E'], num_horas),
    'temperatura': np.random.uniform(15, 35, num_horas),
    'humedad': np.random.uniform(30, 90, num_horas),
    'calidad_aire': np.random.uniform(50, 100, num_horas)
}

df = pd.DataFrame(data)

# 2. Convertir a datetime
df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])

# 3. Remuestrear a promedios diarios
df_diario = df.set_index('fecha_hora').resample('D')[['temperatura', 'humedad', 'calidad_aire']].mean().reset_index()

# 4. Gráficos de líneas
fig, axes = plt.subplots(3, 1, figsize=(10, 12))

for i, metric in enumerate(['temperatura', 'humedad', 'calidad_aire']):
    sns.lineplot(data=df_diario, x='fecha_hora', y=metric, ax=axes[i])
    axes[i].set_title(f'Promedio Diario de {metric.capitalize()}', fontsize=12)
    axes[i].set_xlabel('Fecha', fontsize=10)
    axes[i].set_ylabel(metric.capitalize(), fontsize=10)
    axes[i].grid(axis='y', linestyle='--')

plt.tight_layout()
plt.show()

# 5. Mapa de calor de correlaciones
correlation_matrix = df_diario[['temperatura', 'humedad', 'calidad_aire']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlaciones entre Métricas', fontsize=14)
plt.show()

# 6. Gráfico de dispersión con regresión lineal
plt.figure(figsize=(8, 6))
sns.regplot(data=df_diario, x='temperatura', y='humedad', scatter_kws={'alpha':0.5})
plt.title('Relación entre Temperatura y Humedad', fontsize=14)
plt.xlabel('Temperatura (°C)', fontsize=12)
plt.ylabel('Humedad (%)', fontsize=12)
plt.grid(axis='both', linestyle='--')
plt.show()
