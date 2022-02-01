import numpy as np

arr = np.ones((10, 10), int)
arr[1:-1,1:-1] = 0
print(arr)