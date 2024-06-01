import pandas as pd
import matplotlib.pyplot as plt

data = {
    'usuario': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'E', 'A'],
    'cantidad': [100, -50, 200, 150, -30, 80, -120, 75, 110, -60],
    'fecha': ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-02', '2024-05-03', '2024-05-05', '2024-05-05',
              '2024-05-06', '2024-05-07', '2024-05-08'],
    'tipo': ['deposito', 'retiro', 'deposito', 'deposito', 'retiro', 'deposito', 'retiro', 'deposito', 'deposito', 'retiro'],
    'saldo_final': [100, 50, 250, 200, 170, 250, 80, 155, 265, 205]
}

df = pd.DataFrame(data)

df['fecha'] = pd.to_datetime(df['fecha'])

df['saldo_diario'] = df.groupby('usuario')['cantidad'].cumsum()

# Agrupar por usuario y calcular estadísticas
user_stats = df.groupby('usuario').agg(
    saldo_promedio=('saldo_diario', 'mean'),
    total_depositos=('cantidad', lambda x: x[x > 0].sum()),
    total_retiros=('cantidad', lambda x: x[x < 0].sum())
)

# Seleccionar los 5 usuarios con más transacciones
top_users = df['usuario'].value_counts().head(5).index

# Filtrar el DataFrame para los usuarios principales
df_top_users = df[df['usuario'].isin(top_users)]

# Gráfico de líneas del saldo promedio diario
plt.figure(figsize=(10, 6))
for user in top_users:
    user_data = df_top_users[df_top_users['usuario'] == user]
    plt.plot(user_data['fecha'], user_data['saldo_diario'], label=user)
plt.xlabel('Fecha')
plt.ylabel('Saldo Promedio Diario')
plt.title('Evolución del Saldo Promedio Diario (Top 5 Usuarios)')
plt.legend()
plt.show()

# Gráfico de barras comparando depósitos y retiros
user_stats_top = user_stats.loc[top_users]
user_stats_top[['total_depositos', 'total_retiros']].plot(kind='bar', figsize=(10, 6))
plt.xlabel('Usuario')
plt.ylabel('Cantidad')
plt.title('Comparación de Depósitos y Retiros (Top 5 Usuarios)')
plt.show()
