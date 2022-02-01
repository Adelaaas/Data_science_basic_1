import numpy as np
import math
sum1 = 0
a = np.array([[1,2,3],[1,2,3],[1,2,3]])
print("Задание найти все элементы столбца, потом строк")
print("Столбцы")
for i in range(3):
    for j in range(3):
        print(a[j][i], end=' ') # по столбцам
    print()
print("Строки")
for i in range(3):
    for j in range(3):
        print(a[i][j], end=' ') # по строкам
    print()
print("Задание сумму всех элементов и их средняя сумма")
a = np.array([[1,2,3],[1,2,3],[1,2,3]])
for i in range(3):
    for j in range(3):
        sum1=sum1+1
print("Сумма =", a.sum(),"Среднее =", a.sum()/sum1)
a = np.array([[1,2,3],[9,0,8],[7,8,5]])
print("Задание найти главную диагональ")
for i in range(3):
    for j in range(3):
        if i==j:
            print(a[i][j], end=' ')
print()
print("Задание Мальчики и Девочки")
print (a [0 :, 1] ,"- Девочки")
print (*a [ 1 : 2 ,:] ,"- Мальчики")
a=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Задание")
print(a.shape)
b=a.flatten()
print(b)
print(b.shape)