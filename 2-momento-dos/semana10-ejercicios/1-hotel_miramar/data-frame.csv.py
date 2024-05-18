import pandas as pd
from io import StringIO

data = """
Cliente,Fecha Llegada,Días de estancia,Precio,I.V.A.,TOTAL
Antonio Pérez,25/06/2002,2,106.98,17.12,124.1
Juan Fernández,20/06/2002,5,267.45,42.83,310.28
Amelia Antón,14/05/2002,4,213.96,34.23,248.19
Marisa Peña,05/06/2002,7,374.93,59.99,434.92
Violeta Rodriguez,14/06/2002,14,749.86,120.08,869.94
Carmen Benavente,07/07/2002,10,534.9,85.23,620.13
Mario Puerta,05/07/2002,3,160.47,25.67,186.14
Salvador Yuste,01/07/2002,5,267.45,42.83,310.28
"""

# Convertir la cadena de texto en un objeto StringIO
data_io = StringIO(data)

# Leer los datos en un DataFrame
df = pd.read_csv(data_io)

# Mostrar el DataFrame
print(df)

# Guardar el DataFrame en un archivo CSV
df.to_csv('hotel-miramar.csv', index=False)