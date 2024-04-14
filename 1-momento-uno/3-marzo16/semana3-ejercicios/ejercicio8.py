# 8. Mostrar los números comprendidos entre 1 y 30 exceptuando los múltiplos de 3

for numero in range(1, 31):
    if numero % 3 != 0:
        print(numero)
