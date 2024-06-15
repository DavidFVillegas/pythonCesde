import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# 1. Cargar los datos (reemplaza con tus datos reales)
data = {
    'comentario': ["Me encantó este producto, es genial!", "No me gustó para nada, muy mala calidad.", "Es un producto decente, pero podría mejorar.", "Excelente servicio al cliente, muy satisfecho.", "No lo recomiendo, no vale la pena el precio."],
    'calificacion': [5, 1, 3, 5, 2],
    'fecha': ['2024-01-15', '2024-02-28', '2024-03-10', '2024-04-05', '2024-05-20']
}

df = pd.DataFrame(data)

# 2. Palabras clave para análisis de sentimiento (puedes personalizarlas)
positive_words = ['encantado', 'genial', 'excelente', 'satisfecho', 'bueno', 'rápido', 'recomiendo', 'me gusta', 'feliz']
negative_words = ['no me gustó', 'mala calidad', 'no recomiendo', 'no vale', 'pésimo', 'terrible', 'horrible', 'decepcionado']

# 3. Función para clasificar el sentimiento
def classify_sentiment(text):
    text_lower = text.lower()  # Convertir a minúsculas para evitar problemas de mayúsculas/minúsculas
    positive_count = sum(word in text_lower for word in positive_words)
    negative_count = sum(word in text_lower for word in negative_words)

    if positive_count > negative_count:
        return 'positivo'
    elif negative_count > positive_count:
        return 'negativo'
    else:
        return 'neutro'

# 4. Clasificar sentimientos
df['sentimiento'] = df['comentario'].apply(classify_sentiment)

# 5. Agrupar por mes y calcular promedios de sentimientos
df['fecha'] = pd.to_datetime(df['fecha'])  # Asegurarse de que la fecha esté en formato datetime
df['mes'] = df['fecha'].dt.to_period('M')
monthly_sentiment_counts = df.groupby('mes')['sentimiento'].value_counts().unstack(fill_value=0)

# 6. Gráfico de líneas de tendencias mensuales
plt.figure(figsize=(10, 6))
for sentiment in ['positivo', 'negativo', 'neutro']:
    if sentiment in monthly_sentiment_counts:  # Manejar el caso de que no haya comentarios de un sentimiento en un mes
        plt.plot(monthly_sentiment_counts.index.to_timestamp(), monthly_sentiment_counts[sentiment], label=sentiment, marker='o')
plt.xlabel('Mes')
plt.ylabel('Cantidad de Comentarios')
plt.title('Tendencia Mensual de Sentimientos')
plt.legend()
plt.grid(axis='y')  # Agregar líneas de grid en el eje y
plt.show()

# 7. Gráfico de barras de distribución de sentimientos por calificación
df['calificacion_bin'] = pd.cut(df['calificacion'], bins=[0, 2, 5], labels=['baja', 'alta'])
sentiment_by_rating = df.groupby('calificacion_bin')['sentimiento'].value_counts().unstack(fill_value=0)
sentiment_by_rating.plot(kind='bar')
plt.title('Distribución de Sentimientos por Calificación')
plt.ylabel('Cantidad de Comentarios')
plt.show()

# 8. Análisis de frecuencia de palabras (alternativa a nube de palabras)
def get_top_words(df, sentiment, n=10):
    words = Counter(' '.join(df[df['sentimiento'] == sentiment]['comentario']).lower().split())
    # Eliminar palabras comunes (stopwords) y palabras clave de sentimiento
    stopwords = ['me', 'este', 'para', 'es', 'un', 'el', 'la', 'los', 'las'] + positive_words + negative_words
    for word in stopwords:
        words.pop(word, None)
    return words.most_common(n)

top_positive_words = get_top_words(df, 'positivo')
top_negative_words = get_top_words(df, 'negativo')

print("Palabras más frecuentes en comentarios positivos:", top_positive_words)
print("Palabras más frecuentes en comentarios negativos:", top_negative_words)
