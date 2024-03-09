# Realice un algoritmo en python que permita calcular la nota definitiva de 3 módulos del curso,
# cada módulo tiene cuatro notas de seguimiento con un valor del 35%,
# tres parciales cada uno con un valor del 20% y una auto y coevaluación del 5% para la nota definitiva

def calcular_nota_modulo(notas_seguimiento, notas_parciales, auto_coevaluacion):

    promedio_seguimiento = sum(notas_seguimiento) / len(notas_seguimiento)
    promedio_parciales = sum(notas_parciales) / len(notas_parciales)

    nota_final = (promedio_seguimiento * 0.35) + (promedio_parciales * 0.6) + (auto_coevaluacion * 0.05)
    return nota_final

def calcular_nota_curso(modulos):

    nota_curso = sum(modulos) / len(modulos)
    return nota_curso

modulos = []
for i in range(3):
    print(f"Ingresa las notas del Módulo {i + 1}:")
    seguimiento = [float(input(f"Nota de seguimiento {j + 1}: ")) for j in range(4)]
    parciales = [float(input(f"Nota del parcial {k + 1}: ")) for k in range(3)]
    auto_coevaluacion = float(input("Nota de auto y coevaluación: "))

    nota_modulo = calcular_nota_modulo(seguimiento, parciales, auto_coevaluacion)
    modulos.append(nota_modulo)
    print(f"La nota final del Módulo {i + 1} es: {nota_modulo}\n")

nota_curso = calcular_nota_curso(modulos)
print(f"La nota definitiva del curso es: {nota_curso}")