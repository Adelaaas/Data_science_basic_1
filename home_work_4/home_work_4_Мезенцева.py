import numpy as np
from math import ceil
from math import floor
# 1
A = np.ones((10, 10))
A[1:-1, 1:-1] = 0
print(A)
# 2
A = np.zeros((5, 5))
for i in range(4):
    A[i, i + 1] = i + 1
print(A)
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
Z = []
for i in range(len(A)):
    if A[i] < 0:
        Z.append(floor(A[i]))
    else:
        Z.append(ceil(A[i]))
print(Z)
# 9
A = np.array([int(y) for y in input().split()])
B = np.array([int(z) for z in input().split()])
Z = []
for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            Z.append(A[i])
Z = sorted(Z)
print(Z)