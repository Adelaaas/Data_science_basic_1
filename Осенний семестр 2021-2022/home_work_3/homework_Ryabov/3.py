import numpy as np

X = np.random.rand(5, 10)

print(X, "mean:", X.mean())
print()

Y = X - X.mean()

print(Y)