import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Crear DataFrames
np.random.seed(42)
n_products = 10
n_users = 50
n_transactions = 100
n_reviews = 150

products = pd.DataFrame({
    'product_id': range(1, n_products + 1),
    'category': np.random.choice(['Electrónica', 'Ropa', 'Hogar', 'Juguetes'], n_products),
    'price': np.random.uniform(10, 200, n_products)
})

users = pd.DataFrame({
    'user_id': range(1, n_users + 1),
    'age': np.random.randint(18, 65, n_users),
    'location': np.random.choice(['Ciudad A', 'Ciudad B', 'Ciudad C'], n_users)
})

transactions = pd.DataFrame({
    'transaction_id': range(1, n_transactions + 1),
    'product_id': np.random.choice(products['product_id'], n_transactions),
    'user_id': np.random.choice(users['user_id'], n_transactions),
    'purchase_date': pd.date_range('2023-01-01', periods=n_transactions, freq='D')
})

reviews = pd.DataFrame({
    'review_id': range(1, n_reviews + 1),
    'product_id': np.random.choice(products['product_id'], n_reviews),
    'user_id': np.random.choice(users['user_id'], n_reviews),
    'rating': np.random.randint(1, 6, n_reviews)
})

# 2. Unir DataFrames
merged_df = transactions.merge(products, on='product_id').merge(users, on='user_id').merge(reviews, on=['product_id', 'user_id'], how='left')

# 3. Calcular tasa de conversión por categoría
visits_by_category = merged_df['category'].value_counts()
purchases_by_category = merged_df[merged_df['rating'].notnull()]['category'].value_counts()
conversion_rate = (purchases_by_category / visits_by_category).fillna(0)

# 4. Gráfico de barras de tasa de conversión
plt.figure(figsize=(10, 6))
conversion_rate.plot(kind='bar')
plt.title('Tasa de Conversión por Categoría de Producto')
plt.ylabel('Tasa de Conversión')
plt.show()

# 5. Calcular calificación promedio y distribución
average_rating = reviews['rating'].mean()
rating_distribution = reviews['rating'].value_counts()

print(f"Calificación promedio de los productos: {average_rating:.2f}")
print("Distribución de calificaciones:")
print(rating_distribution)

# 6. Gráfico de líneas de tendencia de ventas mensuales
monthly_sales = merged_df.set_index('purchase_date').resample('M')['transaction_id'].count()
plt.figure(figsize=(10, 6))
monthly_sales.plot()
plt.title('Tendencia de Ventas Mensuales')
plt.ylabel('Número de Transacciones')
plt.show()

# 7. Gráfico de cajas de distribución de precios por categoría
plt.figure(figsize=(10, 6))
merged_df.boxplot(column='price', by='category')
plt.title('Distribución de Precios por Categoría')
plt.ylabel('Precio')
plt.show()
