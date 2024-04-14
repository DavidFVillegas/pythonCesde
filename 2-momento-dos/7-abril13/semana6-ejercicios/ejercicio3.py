"""
3. Crea una Serie que contenga los siguientes datos:
    'a': 100, 'b': 200, 'c': 300, 'd': 400.
    Luego, accede al valor asociado con la etiqueta 'b'.
"""

import pandas as pd

datos = pd.Series({'a': 100, 'b': 200, 'c': 300, 'd': 400})
print(datos['b'])
