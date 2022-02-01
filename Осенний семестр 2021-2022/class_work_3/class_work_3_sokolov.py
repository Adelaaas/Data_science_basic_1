import numpy as np

print('\nЗадание 1')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print(arr[0, 0], arr[1, 1], arr[2, 2])

print('\nЗадание 2')
print(arr[0:, 1], ": Девочки")
print(arr[1: 2, :], ": Мальчики")

print('\nЗадание 3')
print(arr.shape)
r = arr.flatten()
print(r.flatten(), r.shape)

print('\nЗадание 4')
for a in range(arr.shape[1]):
    print('Столбик: ', a)
    for b in range(arr.shape[0]):
        print(arr[b, a])
for a in range(arr.shape[0]):
    print('Строка: ', a)
    for b in range(arr.shape[1]):
        print(arr[a, b])

print('\nЗадание 5')
summa = 0
k = 0
for x in range(arr.shape[0]):
    for y in range(arr.shape[1]):
        summa = summa + arr[x, y]
        k += 1
num = summa / k
print(summa, num)

