"""
3. Solicitar el ingreso de 2 nombres, validar si los nombres ingresados tienen la misma longitud,
    comienzan con la misma letra si es así el programa debe mostrar los nombres
    comienzan con la misma letra y la longitud de estos. De lo contrario debe
    mostrar un mensaje indicando que no coinciden.
"""

# Solicitar al usuario que ingrese dos nombres
nombre1 = input("Introduce el primer nombre: ")
nombre2 = input("Introduce el segundo nombre: ")

# Validar si los nombres ingresados tienen la misma longitud y comienzan con la misma letra
if len(nombre1) == len(nombre2) and nombre1[0].lower() == nombre2[0].lower():
    print(f"Los nombres {nombre1} y {nombre2} comienzan con la misma letra y tienen la misma longitud.")
else:
    print("Los nombres no coinciden.")

"""
Nombres con la misma longitud y que comienzan con la misma letra
Nombres: "Ana" y "Ada"
Esperado: "Los nombres Ana y Ali comienzan con la misma letra y tienen la misma longitud."

Nombres con diferente longitud
Nombres: "Ana" y "Anabel"
Esperado: "Los nombres no coinciden."

Nombres que comienzan con diferentes letras
Nombres: "Ana" y "Beto"
Esperado: "Los nombres no coinciden."

Nombres con la misma longitud y que comienzan con la misma letra, pero en diferentes casos
Nombres: "Ana" y "ada"
Esperado: "Los nombres Ana y ali comienzan con la misma letra y tienen la misma longitud."
"""