import random

import numpy as np
print("#1")
a = np.array(np.zeros((10,10)), int)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if i == 0 or i == 9 or j == 9 or j == 0:
            a[i, j] = 1
        print(a[i, j], end = " ")
    print()
print("#2")

n = 0
b = np.array(np.eye(5, k=1), int)
for i in range(b.shape[0]):
    for j in range(b.shape[1]):
        if b[i, j] == 1:
            b[i , j] += n
            n += 1
        print(b[i, j], end = " ")
    print()
print("#3")

X = np.random.rand(5, 10)
Y = np.array([[X[i, j] - X[i].mean() for j in range(X.shape[1])] for i in range(X.shape[0])])
print(Y)
print("#4")
c = np.array([  [ 1,  2,  3,  4,  5,  6,  7],
                [ 8,  9, 10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19, 20, 21],
                [22, 23, 24, 25, 26, 27, 28],
                [29, 30, 31, 32, 33, 34, 35],
                [36, 37, 38, 39, 40, 41, 42]], int)
c1 = c[2]
c[3] = c[0]
c[0] = c1
print(c)
print("#5")
r = [[1, 2, 5, 3, 56],[1, 1.5, 37, 33, 67],[5, 55, 555, 55, 5],[12, 21, 121, 12, 21],[56, 65, 56, 65, 56]]
r = np.int32(np.array(r))
print(r)
print("#6")
c = 0
a = np.array([[random.randint(-50, 50) for j in range(67)] for i in range(86)], int)
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        if a[i, j] != 0:
            c += 1
print(a, "\n", c)
print("#7")
n, m = map(int, (input(), input()))
z = np.array(np.ones((n, m)), int)
for i in range(z.shape[0]):
    for j in range(z.shape[1]):
        if (j % 2 == 0 and i % 2 == 0 or (i+j) % 2 == 0):
            z[i, j] = 0
print(z)
print("#8")
A = np.array([-1.555, 1.66, 2.567, -345.04, 11.23], float)
Z = np.array([], int)
for i in range(A.shape[0]):
    if A[i] < 0:
        Z[i] = np.ceil(A[i])
    elif A[i] > 0:
        Z[i] = np.floor(A[i])
    else:
        Z[i] = 0
#Выдаст ошибку, как можно использовать две функции на однин проход по массиву?
print(Z)