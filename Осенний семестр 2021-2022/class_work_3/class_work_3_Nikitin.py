import numpy as np

# №1
a = np.array([[1, 2, 3],
              [9, 0, 8],
              [7, 8, 5]], int)
print(a[0, 0], a[1, 1], a[2, 2])
# №2
print(' ')
print(a[1, :])
# №3
print(' ')
print(a.shape)
a = a.flatten()
print(a.shape)
# №4
print(' ')
a = np.array([[1, 2],
              [3, 4],
              [5, 6]], int)

for i in range(a.shape[1]):
    for j in range(a.shape[0]):
        print(a[j, i], end=' ')
    print(' ')

# №5
print(' ')
a = np.array([[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]], int)
s = 0
l = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        s += a[i][j]
        l += 1
print(s, s / l)
print(a.sum(), a.mean())
