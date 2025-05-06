import numpy as np

arr = np.array([1,2,3,4])
print(arr.dtype)
print(arr)

arr = np.array([1,2,3,4], dtype='float64')
print(arr.dtype)
print(arr)

# definimos el array de tipo float directamente desde la libreria
arr = arr.astype(np.float64)
print(arr)

# bool
arr = np.array([0, 1,2,3,4])
arr = arr.astype(np.bool_)
print(arr)

# string
arr = np.array([0, 1,2,3,4])
arr = arr.astype(np.string_)
print(arr)

# int
arr = np.array(['0', '1' ,'2' ,'3', '4'])
arr = arr.astype(np.int8)
print(arr)