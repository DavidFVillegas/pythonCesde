import pandas as pd


datos = {
    'Nombre': ['Juan', 'Ana', 'Carlos', 'Maria', 'Pedro', 'Sofia', 'Luis', 'Carmen', 'Ricardo', 'Isabel', 'Jorge',
               'Laura', 'Miguel', 'Patricia', 'Raul'],
    'Apellido': ['Perez', 'Gomez', 'Lopez', 'Rodriguez', 'Martinez', 'Gonzalez', 'Fernandez', 'Torres', 'Sanchez',
                 'Diaz', 'Ramirez', 'Morales', 'Ortiz', 'Guerrero', 'Castillo'],
    'Edad': [30, 35, 40, 45, 50, 25, 30, 35, 40, 45, 50, 25, 30, 35, 40],
    'Salario Mensual': [3000, 3500, 4000, 4500, 5000, 2500, 3000, 3500, 4000, 4500, 5000, 2500, 3000, 3500, 4000],
    'Departamento': ['Desarrollo', 'Desarrollo', 'Desarrollo', 'Desarrollo', 'Desarrollo', 'Marketing', 'Marketing',
                     'Marketing', 'Marketing', 'Marketing', 'Recursos Humanos', 'Recursos Humanos', 'Recursos Humanos',
                     'Recursos Humanos', 'Recursos Humanos']
}

df = pd.DataFrame(datos)

df.to_csv('trabajadores.csv', index=False)
