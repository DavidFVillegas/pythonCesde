# 9. Mostrar los números pares entre 1 y 20, luego la suma de dichos números pares.

suma_pares = 0

for numero in range(1, 21):
    if numero % 2 == 0:
        print(numero)
        suma_pares += numero

print("La suma de los números pares entre 1 y 20 es:", suma_pares)
