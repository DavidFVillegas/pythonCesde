import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear DataFrame con datos de ejemplo
np.random.seed(42)
num_publicaciones = 20
usuarios = ['usuario_' + chr(i) for i in range(ord('A'), ord('A') + num_publicaciones)]
fechas = pd.date_range('2023-01-01', periods=num_publicaciones).to_pydatetime().tolist()
textos = [''.join(np.random.choice(list('abcdefghijklmnñopqrstuvwxyz '), np.random.randint(10, 51))) for _ in range(num_publicaciones)]
me_gusta = np.random.randint(0, 1001, num_publicaciones)
compartidos = np.random.randint(0, 101, num_publicaciones)

data = {'usuario': usuarios, 'fecha': fechas, 'texto_publicacion': textos, 'me_gusta': me_gusta, 'compartidos': compartidos}
df = pd.DataFrame(data)

# 3. Calcular longitud del texto
df['longitud_texto'] = df['texto_publicacion'].apply(len)

# 4. Agrupar por usuario y calcular promedios
user_stats = df.groupby('usuario')[['me_gusta', 'compartidos', 'longitud_texto']].mean()

# 5. Gráfico de dispersión
plt.figure(figsize=(10, 6))
plt.scatter(df['longitud_texto'], df['me_gusta'], alpha=0.7)
plt.title('Relación entre Longitud del Texto y Me Gusta')
plt.xlabel('Longitud del Texto')
plt.ylabel('Me Gusta')
plt.grid(axis='y', linestyle='--')

# 6. Top 10 usuarios y filtrar
top_users = df['usuario'].value_counts().head(10).index
user_stats_top = user_stats.loc[top_users]

# 7. Gráfico de barras
plt.figure(figsize=(12, 6))
user_stats_top.plot(kind='bar', rot=0)
plt.title('Promedio de Me Gusta y Compartidos por Usuario (Top 10)')
plt.xlabel('Usuario')
plt.ylabel('Promedio')
plt.legend(["Me Gusta", "Compartidos"])
plt.grid(axis='y', linestyle='--')

# 8. Gráfico de violín (con manejo de cuartiles duplicados)
df['cuartil_longitud'] = pd.qcut(df['longitud_texto'], 4, labels=['Q1', 'Q2', 'Q3', 'Q4'], duplicates='drop')
plt.figure(figsize=(10, 6))
plt.violinplot([df[df['cuartil_longitud'] == q]['me_gusta'] for q in df['cuartil_longitud'].unique()])
plt.title('Distribución de Me Gusta por Cuartil de Longitud del Texto')
plt.xlabel('Cuartil de Longitud del Texto')
plt.ylabel('Me Gusta')

# Mostrar gráficos
plt.show()
plt.show()
plt.show()
