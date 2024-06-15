import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'Nombre': ['Ana', 'Luis', 'María', 'Juan'],
    'Edad': [28, 34, 29, 40],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla']
}

df = pd.DataFrame(data)

html_table = df.to_html(index=False)

with open('tabla.html', 'w', encoding='utf-8') as file:
    file.write(html_table)