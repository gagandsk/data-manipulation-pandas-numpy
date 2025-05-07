import numpy as np

arr = np.arange(0,11)
print(arr)

arr2 = arr[0:6]
print(arr2)

arr2[:] = 0
print(arr2)
print(arr)

arr_copy = arr.copy()
print(arr_copy)

arr_copy[:] = 100
print(arr_copy)

print(arr)