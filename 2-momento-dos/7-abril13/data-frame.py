import numpy as np
import pandas as pd

data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
print(frame)

print("-----" * 20)
print("Con frame.head() podemos ver solamente las 5 primeras filas")
print(frame.head())  # Nos muestra los primeros 5 elementos
print(frame.head(3))  # Aqui podemos precisar cuantas filas deseamos ver

print("-----" * 20)
print("Podemos cambiar el orden de las columnas de la tabla")
print(pd.DataFrame(data, columns=["year", "state", "pop"]))  # Cambiando el orden de las columnas

print("-----" * 20)
frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"],
                      index=["one", "two", "three", "four", "five", "six"])
print(frame2)
print("Imprimiendo las columnas:")
print(frame2.columns)  # Nos muestra las columnas

print("-----" * 20)
print("Imprimiendo una columna:")
print(frame["state"])
print("-----" * 20)
# Modificando una columna para que los valores se llenen con 16.5
print("Modificando una columna para que los valores se llenen con 16.5")
frame2["debt"] = 16.5
print(frame2)

#  Utilizando Numpy para llenar los valores de la columna
frame2["debt"] = np.arange(6)
print(frame2)