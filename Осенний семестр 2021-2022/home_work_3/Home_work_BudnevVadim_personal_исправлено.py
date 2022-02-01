import numpy as np
import math

print("Задание 3")
print("Вычтите среднее из элементов массива")
x = np.random.rand(5, 10)
y = []
print(x)
print()
for i in range(len(x)):
    print("Наше среднее: ",end='')
    print(x[i].mean())
    y.append(x[i]-(x[i].mean()))

print("Наш ответ")
for i in y:

    print(i)

print("Задание номер 8")
print('''Вектор A содержит float числа как больше, так и меньше нуля.
Округлите их до целых и результат запишите в переменную Z. Округление должно быть "от нуля", т.е.:
положительные числа округляем всегда вверх до целого отрицательные числа округляем всегда вниз до целого 0 остаётся 0''')

a = []
z = []
print()
print("Введите, сколько вы хотите ввести элементов вектора")
n = int(input())
print("Введите через энтер элементы")
while n>0:
    a.append(float(input()))
    n=n-1
for i in range(len(a)):
    if a[i]>=0:
        z.append(math.ceil(a[i]))
    if a[i]<0:
        z.append(math.floor(a[i]))
print(z)