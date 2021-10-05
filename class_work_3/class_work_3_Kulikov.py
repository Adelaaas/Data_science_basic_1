import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], int)

print('Задание 1')

print("Числa главной диагонали:", a[0, 0], a[1, 1], a[2, 2])

print('Задание 2')

print('Все элементы столбцов второй строчки:', *a[1:2])

print('Задание 3')

b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], int)
for x1 in range(b.shape[0]):
    print('Cтрока:', x1 + 1)
    for y1 in range(b.shape[1]):
        print(b[x1, y1])

print('Задание 4')

s = 0
s = int(s)
sr = 0
sr = int(sr)
amount = 0
amount = int(amount)
for x2 in range(b.shape[0]):
  for y2 in range(b.shape[1]):
    s += a[x2, y2]
    amount += 1
sr = s/amount
print('Сумма всех элементов:', s)
print('Среднее значение всех элементов:', sr)
