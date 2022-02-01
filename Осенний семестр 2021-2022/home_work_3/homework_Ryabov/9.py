import numpy as np

a = np.random.randint(-50, 50, 10)
b = np.random.randint(-50, 50, 10)
print(a)
print(b)

print(a[np.in1d(a, b)])