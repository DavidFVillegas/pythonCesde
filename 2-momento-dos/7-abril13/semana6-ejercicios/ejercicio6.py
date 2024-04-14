"""
6. Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una
    serie con las notas de los alumnos aprobados ordenadas de mayor a menor.
"""

import pandas as pd


def notas_aprobados(notas_alumnos):
    notas_curso = pd.Series(notas_alumnos)

    notas_alumnos_aprobados = notas_curso[notas_curso >= 5.0].sort_values(ascending=False)

    return notas_alumnos_aprobados


notas = {'Juan': 8.5, 'María': 9.0, 'Pedro': 4.5, 'Ana': 8.0}
print(notas_aprobados(notas))
