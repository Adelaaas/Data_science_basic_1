import numpy as np
import math
from random import randint

print("Задание номер 1")
print("Создать матрицу размером 10х10 с 0 внутри, и 1 на границах.")

print()
print("Введите строки, потом столбцы")
a = []
n, m = map(int,input().split())
for i in range(n):
    a.append([0]*m)
for i in range(n):
    for j in range(m):
        a[i][j]=1
        if i>0:
            break
for i in range(n-1,-1,-1):
    for j in range(m-1,-1,-1):
        a[i][j]=1
        if j==m-1:
            break
for i in range(n-1,-1,-1):
    for j in range(m):
        a[i][j]=1
        if i>=1 and i<n-1:
            break
for i in a:
    print(i)

print()
print("Задание номер 2")
print("Создать 5x5 матрицу с 1,2,3,4 над диагональю. Все остальные элементы - 0.")

print()
print("Введите строки, потом столбцы")
count = 0
a = []
n, m = map(int,input().split())
for i in range(n):
    a.append([0]*m)
for i in range(n):
    for j in range(m):
        if j-i==1:
            count=count+1
            a[i][j]=count
for i in a:
    print(i)

print()
print("Задание номер 3")
print("Создайте случайную матрицу и вычтите из каждой строки среднее.")

X = np.random.randint(1, 11, size=(5, 10))
Y = np.sum(X, axis = 1)/10
print(Y, "1 способ")
# или даже лучше
print(X.mean(axis=1), "2 способ")

print()
print("Задание номер 4")
print("Создать Массив размерностью (6,7). Поменять в массиве 3 строку с последней.")


a = np.random.randint(1, 11, size=(6, 7))
print(a[2,:]," - 3 строка")
print(a[5,:]," - Последня строка")
print()
b = a.copy()
a[5,:] = a[2,:]
a[2,:] = b[5,:]
for i in a:
    print(i)


print()
print("Задание номер 5")
print("Создать двумерный список и заполнить его рандомными числами. Преобразовать созданный список в NumPy массив (с типом int32).")
print()
print("Введите строки и столбцы через пробел")
n, m = map(int,input().split())
b = []
for i in range(n):
    for j in range(m):
        b.append(randint(1,11))
print(b, type(b))
a = np.array(b)
print(a, type(a))


print()
print("Задание номер 6")
print("Создать массив размерностью (89, 67) и заполнить его случайными числами от -50 до 50. Посчитать количество ненулевых элементов полученного массива.")

count=0
a = np.random.randint(-50, 51, size=(89, 67))
for i in range(89):
    for j in range(67):
        if a[i][j] != 0:
            count=count+1
print()
print(count)

print()
print("Задание номер 7")
print('''Считайте 2 числа: n, m.
Создайте матрицу размера n*m и "раскрасьте" её в шахматную раскраску.
0 - "чёрное"
1 - "белое"''')

print()
print("Введите строки и столбцы, через пробел")
n, m = map(int, input().split())
a = np.random.randint(0, 2, size=(n, m))
for i in range(n):
    for j in range(m):
        if (i+j)%2==0:
            a[i][j]=0
        else:
            a[i][j]=1
for i in a:
    print(i)

print()
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
for i in a:
    z.append(math.ceil(i))
for i in z:
    print(i)

print()
print("Задание номер 9")
print('''Даны 2 вектора целых чисел A и B.
Найдите числа, встречающиеся в обоих векторах и составьте их по возрастанию в вектор Z.
Если пересечений нет, то вектор Z будет пустым.''')

print()
print("Введите элементы а-вектора через пробел:", end = '')
a = list(map(int,input().split()))
print("Введите элементы b-вектора через пробел:", end = '')
b = list(map(int,input().split()))
z = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            z.append(b[j])
z.sort()
z = np.unique(z)
print(z)