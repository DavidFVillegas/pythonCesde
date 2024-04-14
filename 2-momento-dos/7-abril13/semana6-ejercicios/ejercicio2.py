"""
2. Crea una Serie que contenga los siguientes números enteros:
    10, 20, 30, 40, 50.
    Luego, calcula la suma de todos los números en la Serie.
"""

import pandas as pd

numeros = pd.Series([10, 20, 30, 40, 50])
suma = numeros.sum()
print(suma)
