import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'ubicacion': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'E', 'A'],
    'temperatura': [25, 22, 26, 28, 21, 24, 27, 23, 20, 25],
    'humedad': [60, 65, 58, 55, 68, 62, 59, 63, 70, 61],
    'calidad_aire': [85, 80, 88, 92, 78, 86, 90, 82, 75, 87],
    'fecha_hora': ['2024-05-01 08:00:00', '2024-05-01 09:00:00', '2024-05-01 10:00:00', '2024-05-01 11:00:00', '2024-05-01 12:00:00',
                   '2024-05-02 08:00:00', '2024-05-02 09:00:00', '2024-05-02 10:00:00', '2024-05-02 11:00:00', '2024-05-02 12:00:00']
}

df = pd.DataFrame(data)

df['fecha_hora'] = pd.to_datetime(df['fecha_hora'])

# Establecer 'fecha_hora' como índice
df.set_index('fecha_hora', inplace=True)

# Remuestrear a promedios diarios (solo para columnas numéricas)
df_daily = df.select_dtypes(include='number').resample('D').mean()

# Gráficos de líneas para cada métrica
metrics = df_daily.columns  # Obtener automáticamente las métricas
plt.figure(figsize=(12, 8))
for i, metric in enumerate(metrics):
    plt.subplot(len(metrics), 1, i + 1)
    plt.plot(df_daily[metric], marker='o')
    plt.title(f'Tendencia Diaria de {metric.capitalize()}')
    plt.ylabel(metric.capitalize())
plt.tight_layout()
plt.show()

# Mapa de calor de correlaciones
plt.figure(figsize=(8, 6))
sns.heatmap(df_daily.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlaciones entre Métricas')
plt.show()

# Gráfico de dispersión con regresión (temperatura vs. humedad)
sns.regplot(x='temperatura', y='humedad', data=df_daily)
plt.title('Relación entre Temperatura y Humedad')
plt.show()
