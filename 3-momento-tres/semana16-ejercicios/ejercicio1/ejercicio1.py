import pandas as pd
import matplotlib.pyplot as plt

data = {
    'usuario': ['A', 'B', 'A', 'C', 'B', 'A', 'D', 'C', 'E', 'A'],
    'cantidad': [100, -50, 200, 150, -30, 80, -120, 75, 110, -60],
    'fecha': ['2024-05-01', '2024-05-02', '2024-05-03', '2024-05-02', '2024-05-03', '2024-05-05', '2024-05-05', '2024-05-06', '2024-05-07', '2024-05-08'],
    'tipo': ['deposito', 'retiro', 'deposito', 'deposito', 'retiro', 'deposito', 'retiro', 'deposito', 'deposito', 'retiro']
}

# 1. Cargar datos en un DataFrame
df = pd.DataFrame(data)

# 2. Convertir fecha a datetime
df['fecha'] = pd.to_datetime(df['fecha'])

# 3. Calcular el saldo diario (con manejo de valores iniciales)
df['saldo_diario'] = df.groupby('usuario')['cantidad'].cumsum()

# Llenar posibles valores NaN al inicio (si el usuario no tiene saldo inicial)
df['saldo_diario'] = df.groupby('usuario')['saldo_diario'].fillna(method='ffill').fillna(0)

# 4. Agrupar y calcular estadísticas por usuario
user_stats = df.groupby('usuario').agg(
    saldo_promedio=('saldo_diario', 'mean'),
    total_depositos=('cantidad', lambda x: x[x > 0].sum()),
    total_retiros=('cantidad', lambda x: x[x < 0].sum())
).round(2)  # Redondear a 2 decimales

# 5. Seleccionar top 5 usuarios y filtrar
top_users = df['usuario'].value_counts().head(5).index
df_top_users = df[df['usuario'].isin(top_users)]

# Gráfico 1: Evolución del saldo promedio diario (líneas)
plt.figure(figsize=(12, 6))
for user in top_users:
    user_data = df_top_users[df_top_users['usuario'] == user]
    plt.plot(user_data['fecha'], user_data['saldo_diario'], label=user, marker='o')
plt.xlabel('Fecha', fontsize=12)
plt.ylabel('Saldo Diario', fontsize=12)
plt.title('Evolución del Saldo Diario (Top 5 Usuarios)', fontsize=14)
plt.legend(fontsize=12)
plt.grid(axis='y', linestyle='--')
plt.tight_layout()
plt.show()

# Gráfico 2: Comparación depósitos vs. retiros (barras)
user_stats_top = user_stats.loc[top_users]
user_stats_top[['total_depositos', 'total_retiros']].plot(kind='bar', figsize=(10, 6))
plt.xlabel('Usuario', fontsize=12)
plt.ylabel('Cantidad', fontsize=12)
plt.title('Comparación de Depósitos y Retiros (Top 5 Usuarios)', fontsize=14)
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--')
plt.show()
