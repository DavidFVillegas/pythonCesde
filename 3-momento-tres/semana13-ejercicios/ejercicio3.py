import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

data = {
    'comentario': ['Me encantó este producto!', 'No me gustó para nada.', 'Es un producto decente.', 'Excelente calidad!', 'Podría ser mejor.', 'Muy satisfecho con la compra.'],
    'calificacion': [5, 1, 3, 5, 2, 4],
    'fecha': ['2024-04-15', '2024-03-28', '2024-05-10', '2024-04-02', '2024-02-20', '2024-05-25']
}

df = pd.DataFrame(data)

df['fecha'] = pd.to_datetime(df['fecha'])

# Palabras clave para análisis de sentimiento básico
positive_words = ['encantado', 'excelente', 'satisfecho', 'bueno', 'genial']
negative_words = ['no', 'nada', 'mal', 'terrible', 'pésimo']

# Función para clasificar el sentimiento
def classify_sentiment(text):
    text_lower = text.lower()
    if any(word in text_lower for word in positive_words):
        return 'positivo'
    elif any(word in text_lower for word in negative_words):
        return 'negativo'
    else:
        return 'neutro'

# Clasificar sentimientos
df['sentimiento'] = df['comentario'].apply(classify_sentiment)

# Agrupar por mes y calcular promedios de sentimientos
df_monthly = df.set_index('fecha').resample('M')['sentimiento'].value_counts().unstack(fill_value=0)

# Gráfico de líneas de tendencias mensuales
df_monthly.plot(marker='o')
plt.title('Tendencia Mensual de Sentimientos')
plt.ylabel('Cantidad de Comentarios')
plt.show()

# Gráfico de barras de distribución de sentimientos por calificación
df['calificacion_bin'] = pd.cut(df['calificacion'], bins=[0, 2, 5], labels=['baja', 'alta'])
sentiment_by_rating = df.groupby('calificacion_bin')['sentimiento'].value_counts().unstack(fill_value=0)
sentiment_by_rating.plot(kind='bar')
plt.title('Distribución de Sentimientos por Calificación')
plt.ylabel('Cantidad de Comentarios')
plt.show()

# "Nubes de palabras" (análisis de frecuencia de palabras)
positive_words_counter = Counter(' '.join(df[df['sentimiento'] == 'positivo']['comentario']).lower().split())
negative_words_counter = Counter(' '.join(df[df['sentimiento'] == 'negativo']['comentario']).lower().split())

# Eliminar palabras comunes (stopwords) y palabras clave de sentimiento
stopwords = ['me', 'este', 'para', 'es', 'un', 'el', 'la', 'los', 'las'] + positive_words + negative_words
for word in stopwords:
    positive_words_counter.pop(word, None)
    negative_words_counter.pop(word, None)

# Mostrar las palabras más frecuentes
print("Palabras más frecuentes en comentarios positivos:", positive_words_counter.most_common(10))
print("Palabras más frecuentes en comentarios negativos:", negative_words_counter.most_common(10))
