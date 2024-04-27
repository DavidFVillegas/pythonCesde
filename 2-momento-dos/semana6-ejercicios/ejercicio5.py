"""
5. Escribir una función que reciba un diccionario con las notas de los alumnos de un curso y devuelva una serie
    con la nota mínima, la máxima, media y la desviación típica.
"""

import pandas as pd


def estadisticas_notas(notas_alumnos):
    notas_curso = pd.Series(notas_alumnos)

    minima = notas_curso.min()
    maxima = notas_curso.max()
    media = notas_curso.mean()
    desviacion = notas_curso.std()

    estadisticas = pd.Series({'Mínima': minima, 'Máxima': maxima, 'Media': media, 'Desviación típica': desviacion})

    return estadisticas


notas = {'Juan': 8.5, 'María': 9.0, 'Pedro': 7.5, 'Ana': 8.0}

print(estadisticas_notas(notas))
