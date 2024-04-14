"""
2. Solicitar al usuario un número y validar si este es número primo. (usar ciclos si es necesario)
"""

# Solicitar al usuario un número
num = int(input("Introduce un número: "))

# Validar si este número es primo
es_primo = True
for i in range(2, num):
    if num % i == 0:
        es_primo = False
        break

if es_primo and num != 1:
    print(f"El número {num} es primo.")
else:
    print(f"El número {num} no es primo.")

"""
Número: 2
Esperado: "El número 2 es primo."

Número: 4
Esperado: "El número 4 no es primo."

Número: 13
Esperado: "El número 13 es primo."

Número: 15
Esperado: "El número 15 no es primo."
"""