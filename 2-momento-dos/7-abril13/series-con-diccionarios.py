import pandas as pd

sdata = {"Ohio": 35000, "Texas": 71000, "Oregon": 16000, "Utah": 5000}
obj3 = pd.Series(sdata)
print(obj3)

print("-----" * 20)
states = ["California", "Ohio", "Oregon", "Texas"]  # California no está en sdata
obj4 = pd.Series(sdata, index=states)
print(obj4)

# Cuales son los valores null
print("-----" * 20)
print("Null values:")
print(pd.isnull(obj4))  # Aqui marca el valor faltante como True
print(obj4.isnull())
#  Cuales son los valore que no estan vacios
print("-----" * 20)
print("Not null values:")
print(pd.notnull(obj4))
print(obj4.notnull())

# Operaciones aritmeticas con Series
print("-----" * 20)
print("Operaciones aritmeticas con Series")
print(obj3)
print(obj4)

print("Sumando las series")
print(obj3 + obj4)  # Aquellos indices que sean iguales los suman

# Podemos darle nombre a la serie
obj4.name = "population"
# Podemos cambiarle nombre a los indices
obj4.index.name = "state"
