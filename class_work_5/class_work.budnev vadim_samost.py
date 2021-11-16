import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print("Задание 4")
print("""Посчитать сколько в датасете бакалавров, 11 класса и тд (по колонке education)
Посчитайте средний возраст всех людей
Постройте гистограмму расределения мужчин и женщин
Удалить из датасета все строки в которых ['income'] > 50""")

df = pd.read_csv("E:\Вадим\income_evaluation.csv\income_evaluation.csv")

print(df)
print("Подпункт 1")
print(df[' education'].value_counts())
print("Подпункт 2")
print(df['age'].mean())
print("Подпункт 3")
print("Не понял)")
print("Подпункт 4")
print(df.drop(df[df[' income'] == ">50K"].index))


def distance(x1,y1,x2,y2):
    print(((x2-x1)**2)+((y2-y1)**2)**(1/2))

if __name__ == '__main__':
    print("Задание 1")
    distance(float(input()),float(input()),float(input()),float(input()))

print("Задание 2")
print("""Даны два списка А и В одинаковой длины. Создайте новый список С в котором какждый новый элемент формируется как:
если значение элемента списка А[i] четное, то С[i] = A[i]*B[i]
если значение элемента списка A[i] нечетное, то С[i] = A[i]+B[i]""")

print("Введите элементы A: ",end='')
a = list(map(int,input().split()))
print("Введите элементы B: ",end='')
b = list(map(int,input().split()))
c=[]

for i in range(len(a)):
    if a[i]%2==0:
        c.append(a[i]*b[i])
    elif a[i]%2 != 0:
        c.append(a[i]+b[i])

for i in c:
    print(i)

print("Задание 3")
print("""Найти минимальный элемент в векторе x среди элементов, после которых стоит нулевой.
Для x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0]) ответ 2.""")
print("Введите вектор: ")
a = list(map(int,input().split()))
a = np.array(a)
min = a[0]
for i in range(len(a)):
    if a[i]!=0:
        if min>a[i] and a[i+1]==0:
            min=a[i]
print(min)