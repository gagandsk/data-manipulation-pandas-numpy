'''
scalar: dim = 0 Un solo dato o valor

vector: dim = 1 Listas de Python

matriz: dim = 2 Hoja de cálculo

tensor: dim > 3 Series de tiempo o Imágenes
'''

import numpy as np

scalar = np.array(42)
print(scalar)
print('scalar dim => ',scalar.ndim)

vector = np.array([1,2,3])
print(vector)
print('vector dim => ', vector.ndim)

matriz = np.array([[1,2,3], [4,5,6], [7,8,9], [10,0,92]], )
print(matriz)
print('matriz dim => ', matriz.ndim)

tensor = np.array([[[1,2,3],[4,5,6],[7,8,9],[0,2,45]],[[1,2,3],[4,5,6],[7,8,9],[0,2,45]]])
print(tensor)
print('tensor dim => ',tensor.ndim)

# Agregar o eliminar dimensiones
vector = np.array([1,2,3], ndmin=10)
print(vector)
print('vector dim => ' ,vector.ndim)

expand = np.expand_dims(np.array([1,2,3]), axis=0)
print(expand)
print('expand dim => ', expand.ndim)

print(vector, vector.ndim)
vector_2 = np.squeeze(vector)
print(vector_2, vector_2.ndim)

tensor5 = np.array([[[[1, 2],[3, 4]], [[5, 6],[7, 8]]], [[[1, 2],[3, 4]], [[5, 6],[7, 8]]]], ndmin = 5)
print(tensor5, tensor5.ndim)