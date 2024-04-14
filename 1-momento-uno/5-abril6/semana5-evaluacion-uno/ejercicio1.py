""""
1. Solicitar al usuario las horas trabajadas, teniendo en cuenta que la jornada
   es de 42 horas y valor hora es de 33000.calcular el salario del trabajador
   teniendo en cuenta si este excede la jornada y trabaja horas extras o si
   por el contrario no excede la jornada de trabajo.

   Pregunta a la profesora: ¿A que tarifa se pagan las horas extras?
"""

# Solicitar al usuario las horas trabajadas
horas_trabajadas = float(input("Introduce las horas trabajadas: "))

# Definir la jornada laboral y el valor por hora
jornada_laboral = 42
valor_hora = 33000

# Calcular el salario del trabajador
if horas_trabajadas > jornada_laboral:
    # Si las horas trabajadas exceden la jornada laboral, calcular las horas extras
    horas_extras = horas_trabajadas - jornada_laboral
    # El salario se calcula sumando el salario por la jornada laboral y el salario por las horas extras
    salario = jornada_laboral * valor_hora + horas_extras * valor_hora * 1.5
else:
    # Si las horas trabajadas no exceden la jornada laboral, el salario se calcula
    # simplemente multiplicando las horas trabajadas por el valor por hora
    salario = horas_trabajadas * valor_hora

print(f"El salario del trabajador es: {salario}")

"""
Caso de prueba 1: No se excede la jornada laboral
Horas trabajadas: 40
Salario esperado: 40 * 33000 = 1320000

Caso de prueba 2: Se excede la jornada laboral
Horas trabajadas: 45
Salario esperado: 42 * 33000 + 3 * 33000 * 1.5 = 1489500
"""