print("Задание 1")
def distance(x1, y1, x2, y2):
    return ((x2-x1)**2 + (y2-y1)**2)**0.5

X1 = float(input())
Y1 = float(input())
X2 = float(input())
Y2 = float(input())
print(f'{distance(X1, Y1, X2, Y2)}\n')

print("Задание 2")
A = [3, -12, 65, 77, -94, 110, 22]
B = [0, 37, -77, 51, 62, 24, 88]
C = []
print(A)
print(B)
for i in range(len(A)):
    if A[i] % 2 == 0:
        C.append(A[i]*B[i])
    else:
        C.append(A[i]+B[i])

print(f'{C}\n')

print("Задание 3")

import numpy as np

x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
res = x[0]

for i in range(len(x)):
    if x[i] != 0:
        if res > x[i] and x[i + 1] == 0:
            res = x[i]

print(f'{res}\n')

print("Задание 4")

import pandas as pd

df = pd.read_csv("C:/Users/maryk/Downloads/Task/income_evaluation.csv", encoding="utf-8")
Bachelors = set(df[' education'])
counter = dict()
for i in Bachelors:
    counter[i] = 0
for i in (df[' education']):
    counter[i] += 1
print(f'Задание 4.1\n{counter}')
print(f'Задание 4.2\n{df["age"].mean()}')

import matplotlib.pyplot as plt

x = ['Male', 'Female']
y = [len(df[df[' sex'] == ' Male']), len(df[df[' sex'] == ' Female'])]

x1, x2 = plt.subplots()

x2.bar(x, y)

x2.set_facecolor('yellow')
x1.set_facecolor('purple')

plt.show()

print("Задание 4.4")
print(df.drop(df[df[' income'] == ' >50K'].index))
