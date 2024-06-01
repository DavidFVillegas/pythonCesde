import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Submodulo1': [4.25, 4.5, 3.9, 4.6, 4.4],
    'Submodulo2': [4.35, 4.45, 4.5, 4.9, 4.4],
    'Submodulo3': [3.9, 3.75, 3.85, 4.3, 4.4],
    'Submodulo4': [4.4, 4.6, 4.0, 4.45, 4.5]
}
df = pd.DataFrame(data, index=['Estudiante1', 'Estudiante2', 'Estudiante3',
                               'Estudiante4', 'Estudiante5'])

stats_df = df.agg(['min', 'max', 'mean'])

print(stats_df)

stats_df.transpose().plot(kind='bar')

plt.show()

stats_df.loc['mean'].plot(kind='pie', autopct='%1.1f%%')

plt.show()