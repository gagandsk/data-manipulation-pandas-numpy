import numpy as np

# Shape me indica la forma del arreglo Reshape transforma el arreglo mientras se mantengan los elementos.

arr = np.random.randint(1,10,(3,2))
print(arr.shape)
print(arr)

print(arr.reshape(1,6))
print(arr.reshape(2,3))
print(np.reshape(arr,(1,6)))

print(arr)

# Reshape en C, apilamos los valores mediante filas
print('C =>', np.reshape(arr,(2,3), 'C'))

# Reshape en Fortran, apilamos los valores mediante columnas
print('F =>', np.reshape(arr,(2,3), 'F'))

# Además existe la opción de hacer reshape según como esté optimizado nuestro computador.
print('A =>',np.reshape(arr,(2,3), 'A'))

'''
Reto
Crear un array de cualquier dimesnión y cambiar sus dimensiones Intentar cambiar el array de forma que no respete la estructura original 1.
'''

array_original = np.random.randint(0,10, (3,3))
print(array_original)
print(array_original.reshape(1,9))

print(array_original.reshape(2,4))
