import numpy as np
import math as m

# задание 1

x1, y1, x2, y2 = map(float, input().split())

def distance(x1, y1, x2, y2):
    dist = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

print(distance(x1, y1, x2, y2))

# задание 2

N = int(input())
A = [0] * N
B = [0] * N
C = [0] * N
A = [int(x) for x in input().split()]
B = [int(y) for y in input().split()]

for i in range(N):
    if A[i] % 2 == 0:
        C[i] = A[i] * B[i]
    else:
        C[i] = A[i] + B[i]

print(C)

# задание 3

A = np.array([int(z) for z in input().split()], int)
mmin = 1000

for j in range(1, len(A)):
    if A[j] == 0 and (A[j - 1] < mmin and A[j - 1] != 0):
        mmin = A[j - 1]

print(mmin)