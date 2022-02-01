import numpy as np

print('Задание 1')
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], float)
print(f'работа с массивом {a}\n')
i: int = 0
j: int = 0
for i in range(3):
    for j in range(3):
        if i == j :
            print(a[i, j])
print("\n")

print('Задание 2')
for j in range(3):
    print(a[1, j])
print("\n")

print('Задание 3')
print(a.shape)
print(a.flatten(), a.shape)

print('Задание 4')
for y in range(a.shape[0]):
    print("Столбец", y + 1)
    for x in range(a.shape[1]):
        print(a[x, y])
print("\n")
for x in range(a.shape[1]):
    print("Строка", x + 1)
    for y in range(a.shape[0]):
        print(a[x, y])
print("\n")

print('Задание 5')
sum: float = 0
n: float = 0
for x in range(a.shape[0]):
    for y in range(a.shape[1]):
        sum += a[x, y]
        n += 1
print(f'Сумма всех элементов матрицы = {sum}')
print(f'Среднее значение = {sum / n}')
