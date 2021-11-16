import numpy as np


arr = np.random.randint(-50, 50, (89, 67))
print(arr)
print()
print(np.where(arr != 0, True, False).sum())