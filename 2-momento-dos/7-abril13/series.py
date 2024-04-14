import pandas as pd

obj = pd.Series([4, 7, -5, 3])  # Cada serie tiene dos partes los índices y los valores
print(obj)
# Aquí nos muestra los valores que se encuentran en la segunda columna
print(obj.values)
# Veamos sus índices
print(obj.index)

# Si queremos cambiar los índices lo podemos hacer así:
obj2 = pd.Series([4, 7, -5, 3], index=["d", "b", "a", "c"])
print(obj2)
print(obj2["a"])  # -5
print(obj2["d"])  # 4
print(obj2[["c", "a", "d"]])

# Filtrando por condiciones el objeto de la serie
print(obj2[obj2 > 0])  # Seleccionando los valores mayores a 0
print(obj2 * 2) # Multiplicando por 2 cada valor de la serie

