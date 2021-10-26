import numpy as np
from math import ceil
from math import floor

# 1
A = np.ones((10, 10))
A[1:-1, 1:-1] = 0
print(A)

# 2
A = np.zeros((5, 5))
for i in range(5):
    A[i, i] = i + 1
print(A)

# 3
X = np.random.rand(5, 10)
Y = np.array([[X[i, j] - X[i].mean() for j in range(X.shape[1])] for i in range(X.shape[0])])
print(Y)

# 4
A = np.array([[1, 2, 3, 4, 5, 6, 7],
              [8, 9, 10, 11, 12, 13, 14],
              [15, 16, 17, 18, 19, 20, 21],
              [22, 23, 24, 25, 26, 27, 28],
              [29, 30, 31, 32, 33, 34, 35],
              [36, 37, 38, 39, 40, 41, 42]], int)
A2 = A.copy()
A[2] = A[5]
A[5] = A2[2]
print(A)

# 5
A = np.random.rand(10, 10)
A = A.astype('int32')
print(A)

# 6
count = 0
A = np.random.randint(-50, 50, size=(89, 67))
for i in range(89):
    for j in range(67):
        if A[i][j] != 0:
            count = count + 1
print(count)

# 7
n, m = map(int, input().split())
A = np.zeros((n, m))
for i in range(n):
    for j in range(m):
        if (i + j) % 2 != 0:
            A[i, j] = 1 
print(A)

# 8
A = np.array([float(x) for x in input().split()])
B = []
for i in range(len(A)):
    if A[i] < 0:
        B.append(floor(A[i]))
    else:
        B.append(ceil(A[i]))
print(B)

# 9
A = np.array([int(y) for y in input().split()])
B = np.array([int(z) for z in input().split()])
C = []
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            C.append(A[i])
C = sorted(C)
print(C)
