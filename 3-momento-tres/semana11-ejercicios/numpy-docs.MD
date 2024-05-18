# Guía de NumPy en Python

## ¿Qué es NumPy?

NumPy (Numerical Python) es una biblioteca de Python que proporciona soporte para grandes matrices multidimensionales y matrices, junto con una gran colección de funciones matemáticas de alto nivel para operar con estos arrays.

## ¿Cómo se utiliza NumPy?

### Instalación

Para instalar NumPy, puedes usar pip, que es el administrador de paquetes de Python. Abre tu terminal y ejecuta el siguiente comando:

```bash
pip install numpy
```

### Importando NumPy

Una vez que NumPy está instalado, puedes importarlo en tus scripts de Python utilizando el siguiente código:

```python
import numpy as np
```

### Creando Arrays

Puedes crear un array de NumPy utilizando la función `np.array()`, pasando una lista como argumento:

```python
import numpy as np

# Crear un array de NumPy
arr = np.array([1, 2, 3, 4, 5])

print(arr)  # Output: [1 2 3 4 5]
```

### Operaciones Matemáticas

NumPy proporciona una gran cantidad de funciones matemáticas que puedes usar para realizar cálculos en arrays. Aquí hay algunos ejemplos:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Sumar 2 a cada elemento del array
arr_plus_2 = arr + 2

print(arr_plus_2)  # Output: [3 4 5 6 7]

# Calcular la media del array
mean = np.mean(arr)

print(mean)  # Output: 3.0
```

### Indexación y Segmentación

Puedes acceder a los elementos de un array de NumPy utilizando índices, de la misma manera que lo harías con una lista de Python. También puedes usar segmentación para acceder a subconjuntos de un array:

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Acceder al primer elemento del array
first_elem = arr[0]

print(first_elem)  # Output: 1

# Acceder a los primeros tres elementos del array
first_three_elems = arr[:3]

print(first_three_elems)  # Output: [1 2 3]
```

Estos son solo algunos ejemplos básicos de lo que puedes hacer con NumPy. NumPy es una biblioteca muy poderosa y versátil, y hay mucho más que puedes aprender sobre ella. Te recomendamos que consultes la [documentación oficial de NumPy](https://numpy.org/doc/) para obtener más información.

## Numpy Arrays

Un array de NumPy es una cuadrícula de valores, todos del mismo tipo, y es indexada por una tupla de enteros no negativos. El número de dimensiones es el rango del array; la forma de un array es una tupla de enteros que da el tamaño del array a lo largo de cada dimensión.

```python
import numpy as np

# Crear un array de rango 1
a = np.array([1, 2, 3])   

# Crear un array de rango 2
b = np.array([[1,2,3],[4,5,6]])    
```

## Tipos de Datos

NumPy soporta una variedad mucho mayor de tipos numéricos que Python. Aquí hay algunos ejemplos:

- int64: Entero de 64 bits
- float32: Flotante de 32 bits
- complex: Complejo, representado por dos flotantes de 128 bits

```python
import numpy as np

# Crear un array de enteros
x = np.array([1, 2])   

# Crear un array de flotantes
y = np.array([1.0, 2.0])   

# Crear un array de complejos
z = np.array([1+2j, 2+3j])   
```

## Dimensiones

En NumPy, las dimensiones se llaman ejes. El número de ejes es el rango.

```python
import numpy as np

# Crear un array de rango 1
a = np.array([1, 2, 3])   

# Crear un array de rango 2
b = np.array([[1,2,3],[4,5,6]])    
```

## Creando un Array

Puedes crear un array de NumPy utilizando la función `np.array()`, pasando una lista como argumento:

```python
import numpy as np

# Crear un array de NumPy
arr = np.array([1, 2, 3, 4, 5])

print(arr)  # Output: [1 2 3 4 5]
```

## Shape y Reshape

La forma de un array de NumPy es el número de elementos en cada dimensión. Puedes obtener la forma de un array utilizando el atributo `shape` y puedes cambiar la forma de un array sin cambiar sus datos utilizando la función `reshape`.

```python
import numpy as np

# Crear un array de rango 2
b = np.array([[1,2,3],[4,5,6]]) 

# Imprimir la forma del array
print(b.shape)  # Output: (2, 3)

# Cambiar la forma del array a (3, 2)
b_reshaped = b.reshape(3, 2)

print(b_reshaped)
# Output: 
# [[1 2]
#  [3 4]
#  [5 6]]
```
## Funciones Principales

NumPy proporciona una gran cantidad de funciones matemáticas y estadísticas que puedes usar para realizar cálculos en arrays. Aquí hay algunos ejemplos:

- `np.sum()`: Suma todos los elementos del array.
- `np.mean()`: Calcula la media de los elementos del array.
- `np.median()`: Calcula la mediana de los elementos del array.
- `np.std()`: Calcula la desviación estándar de los elementos del array.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Sumar todos los elementos del array
total = np.sum(arr)

print(total)  # Output: 15

# Calcular la media del array
mean = np.mean(arr)

print(mean)  # Output: 3.0
```

## Copy

La función `np.copy()` crea una copia independiente de un array. Modificar la copia no afectará al array original.

```python
import numpy as np

# Crear un array
arr = np.array([1, 2, 3, 4, 5])

# Crear una copia del array
arr_copy = np.copy(arr)

# Modificar la copia
arr_copy[0] = 10

print(arr)  # Output: [1 2 3 4 5]
print(arr_copy)  # Output: [10 2 3 4 5]
```

## Condición

Puedes usar condiciones para indexar arrays de NumPy. Esto te permite seleccionar y modificar elementos que cumplan con ciertas condiciones.

```python
import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Seleccionar los elementos del array que son mayores que 2
greater_than_two = arr[arr > 2]

print(greater_than_two)  # Output: [3 4 5]
```

## Operaciones

NumPy permite realizar operaciones elemento por elemento en arrays, como suma, resta, multiplicación y división.

```python
import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])

# Sumar los arrays elemento por elemento
sum_arr = arr1 + arr2

print(sum_arr)  # Output: [ 7  9 11 13 15]
```