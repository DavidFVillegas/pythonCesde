import pandas as pd

df = pd.read_csv('planilla-gestion.csv')

# Cual es la cantidad total de cada producto.
total_quantity = df.groupby('Producto')['Cantidad'].sum()
print("Cantidad total de cada producto:")
print(total_quantity)


# Cual fue el producto mas vendido en octubre.
october_sales = df.groupby('Producto')['Ventas_Octubre'].sum()
best_selling_product_october = october_sales.idxmax()
print("\nProducto más vendido en octubre:")
print(best_selling_product_october)

# Total de ventas generado en el trimestre
total_sales = df['Ventas_Trimestre'].sum()
print("\nTotal de ventas generado en el trimestre:")
print(total_sales)