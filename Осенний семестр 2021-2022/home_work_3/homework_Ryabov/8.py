import random
from math import ceil

arr = [random.uniform(-50, 50) for i in range(10)]
print(arr)

for i in range(len(arr)):
    arr[i] = ceil(arr[i])

print(arr)