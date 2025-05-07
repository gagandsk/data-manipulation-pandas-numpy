import numpy as np

lista = [1,2]
print(lista)

print(lista * 2)

arr = np.arange(0,10)
arr2 = arr.copy()

print(arr * 2)
print(arr + 2)
print(1 / arr)
print(arr ** 2)
print(arr + arr2)
print(arr * arr2)

matriz = arr.reshape(2,5)
matriz2 = matriz.copy()

print(matriz)
print(matriz + matriz2)
print(matriz - matriz2)

matriz2.T
print(np.matmul(matriz,matriz2.T))

print(matriz @ matriz2.T)