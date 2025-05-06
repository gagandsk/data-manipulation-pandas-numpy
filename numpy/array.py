import numpy as np

list = [1,2,3,4,5,6,7,8,9]
print(list)
arr = np.array(list)
print(type(arr))

matriz = [[1,2,3], [4,5,6], [7,8,9]]
matriz = np.array(matriz)
print(matriz)

# suma
print(arr[0] + arr[1])

# acceder a una posicion especifica de la matriz
print(matriz[0, 2])

# slice
print(arr[0:3])
print(arr[1:6])

# automaticamente arranca desde la posicion 0 hasta la 6
print(arr[:6])

# arranca desde la posicion 2 hasta el final
print(arr[2:])

# me devuelve todo de 3 en 3
print(arr[::3])

# esta accediendo al primer valor pero desde el final
print(arr[-1])

# Para el caso de las matrices sucede algo similar. Para acceder a los valores a nivel de filas.
print(matriz[1:])

#Para acceder a los valores a nivel de filas y columnas.
print(matriz[1:,0:2])