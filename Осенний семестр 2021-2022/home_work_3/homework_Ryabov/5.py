from random import randint
import numpy as np

X = [[randint(1, 19) for _ in range(6)] for _ in range(7)]
X = np.array(X, dtype='int32')
print(X)
print(X.dtype)