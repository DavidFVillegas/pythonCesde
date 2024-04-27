import matplotlib.pyplot as plt
import pandas as pd


def generate_chart():
    data = pd.read_csv('trabajadores.csv')

    grouped_data = data.groupby('Departamento').sum()

    labels = grouped_data.index
    values = grouped_data['Salario Mensual']

    plt.bar(labels, values)

    plt.title('Salario total por departamento en la empresa de software')
    plt.xlabel('Departamento')
    plt.ylabel('Salario Mensual Total')

    plt.savefig('salario_por_departamento.png')
    plt.close()
