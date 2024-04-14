"""
    2. Leer el código de un empleado, el valor de la hora y el número de horas trabajadas en la semana.
    Calcule el salario semanal, teniendo en cuenta que:
        - Si trabaja más de 48 horas le debe pagar un 35% de recargo por cada hora de más.
"""

# 1. Solicitar al usuario el código del empleado, valor de la hora y número de horas trabajadas
codigo_empleado = input("Ingrese el código del empleado: ")
valor_hora = float(input("Ingrese el valor por hora: "))
horas_trabajadas = float(input("Ingrese el número de horas trabajadas en la semana: "))

# 2. Verificar si el número de horas trabajadas excede las 48 horas
if horas_trabajadas <= 48:
    # 3. Calcular el salario semanal para 48 horas o menos
    salario_semanal = horas_trabajadas * valor_hora
else:
    # 4. Calcular el salario para más de 48 horas
    horas_extras = horas_trabajadas - 48
    recargo_hora = valor_hora * 0.35  # 35% de recargo por hora extra
    salario_semanal = (48 * valor_hora) + (horas_extras * (valor_hora + recargo_hora))

# 5. Mostrar el salario semanal
print(f"Empleado {codigo_empleado}, Salario semanal: {salario_semanal}")

"""
## Casos de prueba 

### Caso 1: Sin horas extras
- **Código del empleado**: 001
- **Valor de la hora**: 20
- **Número de horas trabajadas en la semana**: 48
- **Resultado esperado**: El salario semanal debe ser 48 horas * 20 = 960

### Caso 2: Con horas extras
- **Código del empleado**: 002
- **Valor de la hora**: 20
- **Número de horas trabajadas en la semana**: 50
- **Resultado esperado**: Las primeras 48 horas se pagan a 20 cada una, y las 2 horas extras tienen un recargo del 35%. 
  Por lo tanto, el salario sería 48 * 20 + 2 * (20 * 1.35) = 960 + 54 = 1014  
"""
