import numpy as np

arr = np.random.randint(1,20,10)

matriz = arr.reshape(2,5)
print(matriz)

print(arr.max())

print(matriz.max(1))
print(matriz.max(0))

print(arr.argmax())
print(matriz.argmax(0))

print(arr.min())
print(matriz.min(0))
print(matriz.min(1))

print(arr.argmin())
print(matriz.argmin(0))
print(matriz.argmin(1))

print(arr.ptp())
print(matriz.ptp(0))

arr.sort()
print(arr)
print(np.percentile(arr, 0))
print(np.percentile(arr, 50))
print(np.percentile(arr, 100))

print('median =>', np.median(arr))
print(np.median(matriz,1))

print(np.std(arr))

print(np.var(arr))

print(np.mean(arr))

a = np.array([[1,2], [3,4]])
b= np.array([5, 6])
print('a =>', a)
print('b =>', b)

print(a.ndim)
print(b.ndim)

b = np.expand_dims(b, axis = 0)

print(np.concatenate((a,b), axis = 0))
print(np.concatenate((a,b.T), axis = 1))