import numpy as np
from numpy import ndarray

print("Задание 1")
a = np.zeros((10, 10), int)
a[0::9, ::] = a[::, 0::9] = 1
print(a)
print('\n')

print("Задание 2")
b: ndarray = np.diag(range(1, 5), k=1)
print(b)
print('\n')

print("Задание 3")
X = np.random.rand(5, 10)
Y = [X[j] - X[j].mean() for j in range(X.shape[0])]
print(Y)
print('\n')

print("Задание 4")
counter = np.random.rand(6, 7)
print(f"\n{counter}")
counter[2::3, ::] = counter[5::-3, ::]
print(f"\n{counter}")
print("\n")

print("Задание 5")
d = []
for el in range(4):
    d.append([])
    for i in range(6):
        d[el].append(np.random.randint(1, 9))
arr = np.array(np.int32(d), int)
print(arr)
print("\n")

print("Задание 6")
counter = 0
Z = np.random.randint(-50, 50, size=(89, 67))
for el_2 in range(89):
    for l in range(67):
        if Z[el_2][l] != 0:
            counter = counter + 1
print(counter)
print("\n")

print("Задание 7")
n, m = map(int, input().split())
arr_7 = np.zeros((n, m))
for k in range(n):
    for q in range(m):
        if (k + q) % 2 != 0:
            arr_7[k, q] = 1
print(arr_7)
print("\n")

print("Задание 8")
from math import ceil
from math import floor
A = np.array([float(y) for y in input().split()])
Z = []
for i in range(len(A)):
    if A[i] < 0:
        Z.append(floor(A[i]))
    else:
        Z.append(ceil(A[i]))
print(Z)
print("\n")

print("Задание 9")
A = np.array(np.random.rand(10) * 10, int)
B = np.array(np.random.rand(10) * 10, int)
Z = []
print(f'{A}\n{B}')
for h in range(10):
    if any(A[h] == B):
        Z.append(A[h])
print(sorted(set(Z)))