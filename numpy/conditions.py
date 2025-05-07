import numpy as np

arr = np.linspace(1,10,10, dtype='int8')
indices_cond = arr > 5
print(indices_cond)

print(arr[(indices_cond) & (arr < 9)])

print(arr[indices_cond] = 99)