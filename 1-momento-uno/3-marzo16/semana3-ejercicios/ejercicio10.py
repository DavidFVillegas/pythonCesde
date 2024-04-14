# 10. Leer una palabra, mostrar cuantas vocales tiene

palabra: str = input("Ingresa una palabra: ")

palabra = palabra.lower()

vocales = "aeiou"

contador_vocales = 0

for caracter in palabra:
    if caracter in vocales:
        contador_vocales += 1

print(f'La palabra \'{palabra}\' tiene {contador_vocales} vocales.')
