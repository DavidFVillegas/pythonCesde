# Realizar un pátron de árbol de navidad con asteriscos y espacios.

for i in range(1, 7):
    espacios = ' ' * (6 - i)
    print(espacios + '*' * (2*i-1))