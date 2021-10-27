import numpy as np
from math import ceil
from math import floor


print('\nЗадание 1')
arr_1 = np.zeros((10, 10), int)
arr_1[0::9, ::] = arr_1[::, 0::9] = 1
print(arr_1)


print('\nЗадание 2')
arr_2 = np.diag(range(1, 5), k=1)
print(arr_2)


print('\nЗадание 3')
arr_3 = np.random.rand(5, 10)
arr_3_n = [arr_3[i] - arr_3[i].mean() for i in range(arr_3.shape[0])]
print(arr_3_n)


print('\nЗадание 4')
arr_4 = np.random.rand(6, 7)
print(f"\n{arr_4}")
arr_4[2::3, ::] = arr_4[5::-3, ::]
print(f"\n{arr_4}")


print('\nЗадание 5')
l = []
for i in range(4):
    l.append([])
    for q in range(6):
        l[i].append(np.random.randint(1, 9))
arr_5 = np.array(np.int32(l), int)
print(arr_5)


print('\nЗадание 6')
c = 0
arr_6 = np.random.randint(-50, 50, size=(89, 67))
for k in range(89):
    for q in range(67):
        if arr_6[k][q] != 0:
            c = c + 1
print(c)


print('\nЗадание 7')
n, m = map(int, input().split())
arr_7 = np.zeros((n, m))
for k in range(n):
    for q in range(m):
        if (k + q) % 2 != 0:
            arr_7[k, q] = 1
print(arr_7)


print('\nЗадание 8')
arr_8 = np.array([float(x) for x in input().split()])
z = []

for i in range(len(arr_8)):
    if arr_8[i] < 0:
        z.append(floor(arr_8[i]))
    else:
        z.append(ceil(arr_8[i]))
print(z)


print('\nЗадание 9')
arr_9 = np.array([int(x) for x in input().split()])
arr_9_n = np.array([int(z) for z in input().split()])
z = []

for k in range(len(arr_9)):
    for q in range(len(arr_9_n)):
        if arr_9[k] == arr_9_n[q]:
            z.append(arr_9[k])
z = sorted(z)
z = np.unique(z)
print(z)
