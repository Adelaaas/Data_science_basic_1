import numpy
import random

# num1
print(1)
arr = numpy.empty([3, 3], dtype=int)

for i in range(3):
    for j in range(3):
        arr[i][j] = random.randint(-100, 100)

print("Исходный массив \n", arr)
print("Элементы главной диагонали: ", arr[0][0], arr[1][1], arr[2][2])
print('-' * 40)
# num2
print(2)
print(arr[1, :])
print('-' * 40)
# num3
print(3)
arr = numpy.empty([3, 3], dtype=int)

for i in range(3):
    for j in range(3):
        arr[i][j] = random.randint(-100, 100)

print('Исходный массив \n', arr)
print('Shape:', arr.shape)
arr = arr.flatten()
print('Новый массив \n', arr)
print('Shape:', arr.shape)
print('-' * 40)

# num4
print(4)
arr = numpy.empty([3, 3], dtype=int)

for i in range(3):
    for j in range(3):
        arr[i][j] = random.randint(-100, 100)

print(arr)

for x in range(arr.shape[0]):
    print('столбец', x + 1)
    for y in range(arr.shape[1]):
        print(arr[y][x], end=" ")
    print()

print('-' * 40)
# num5
print(5)
arr = numpy.empty([3, 3], dtype=int)

for i in range(3):
    for j in range(3):
        arr[i][j] = random.randint(-100, 100)

print(arr)

summa = 0
avg = 0

for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        summa += arr[i][j]

avg = summa / len(arr.flatten())

print(f'Сумма элементов равна: {summa} ({arr.sum()})')
print(f'Среднее зачение элементов: {avg} ({arr.mean()})')
