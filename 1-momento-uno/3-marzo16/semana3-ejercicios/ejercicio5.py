"""
5. Un cliente tiene una inversión en el banco.
El decidirá reinvertir con los intereses siempre y cuando estos excedan a $100.000, sino solo dejará el capital.
Desea saber cuánto dinero tendrá finalmente en su cuenta.
Se lee el valor invertido (que debe ser máximo de $90.000) y la tasa de interés.
"""


def calcular_inversion_final(capital_inicial, tasa_interes):

    if capital_inicial > 90000:
        return "El capital inicial no debe exceder $90.000"

    intereses = capital_inicial * (tasa_interes / 100)

    if intereses > 100000:
        return capital_inicial + intereses
    else:
        return capital_inicial


print(f"Caso 1 - Capital final: {calcular_inversion_final(90000, 1)}")
print(f"Caso 2 - Capital final: {calcular_inversion_final(50000, 300)}")
print(f"Caso 3 - Capital final: {calcular_inversion_final(91000, 10)}")
