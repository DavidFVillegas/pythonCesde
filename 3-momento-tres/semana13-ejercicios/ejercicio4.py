import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    'usuario': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'David', 'Alice', 'Eva', 'Bob', 'Charlie'],
    'fecha': ['2024-05-15', '2024-05-12', '2024-05-18', '2024-05-10', '2024-05-16', '2024-05-09', '2024-05-22', '2024-05-13', '2024-05-19', '2024-05-11'],
    'texto': ['¡Me encanta este nuevo café!', 'Acabo de terminar un gran libro.', '¡Buenos días a todos!', '¡Qué día tan hermoso!', '¿Alguien quiere jugar videojuegos?', 'El clima está perfecto para salir.', '¡Nuevo video en mi canal!', '¡Feliz cumpleaños a mi mejor amigo!', '¡Acabo de correr 5 km!', '¡Gran concierto anoche!'],
    'me_gusta': [25, 18, 32, 45, 12, 9, 58, 62, 21, 38],
    'compartidos': [5, 3, 8, 10, 2, 1, 12, 15, 4, 7]
}

df = pd.DataFrame(data)

df['fecha'] = pd.to_datetime(df['fecha'])

# Calcular la longitud del texto de la publicación
df['longitud_texto'] = df['texto'].apply(len)

# Agrupar por usuario y calcular estadísticas
user_stats = df.groupby('usuario').agg(
    promedio_me_gusta=('me_gusta', 'mean'),
    promedio_compartidos=('compartidos', 'mean'),
    promedio_longitud_texto=('longitud_texto', 'mean')
).reset_index()  # Reset index for plotting

# Gráfico de dispersión de longitud de texto vs. me gusta
plt.figure(figsize=(8, 6))
plt.scatter(df['longitud_texto'], df['me_gusta'], alpha=0.7)
plt.xlabel('Longitud del Texto')
plt.ylabel('Número de Me Gusta')
plt.title('Relación entre Longitud del Texto y Me Gusta')
plt.show()

# Seleccionar los 10 usuarios más activos
top_10_users = df['usuario'].value_counts().head(10)

# Filtrar el DataFrame para los usuarios principales
df_top_10_users = user_stats[user_stats['usuario'].isin(top_10_users.index)]

# Gráfico de barras de me gusta y compartidos por usuario (top 10)
df_top_10_users.plot(x='usuario', y=['promedio_me_gusta', 'promedio_compartidos'], kind='bar', figsize=(10, 6))
plt.xlabel('Usuario')
plt.ylabel('Promedio')
plt.title('Me Gusta y Compartidos Promedio por Usuario (Top 10)')
plt.show()

# Gráfico de violín de distribución de me gusta por longitud del texto
plt.figure(figsize=(10, 6))
sns.violinplot(x='longitud_texto', y='me_gusta', data=df)
plt.xlabel('Longitud del Texto')
plt.ylabel('Número de Me Gusta')
plt.title('Distribución de Me Gusta por Longitud del Texto')
plt.show()
