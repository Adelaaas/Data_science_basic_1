import numpy as np

print('\nЗадание 1')


def distance(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))

print('\nЗадание 2')
A = [5, -16, 75, 87, -104, 310, 32]
B = [1, 47, -99, 63, 72, 28, 188]
C = []
print(A)
print(B)
for i in range(len(A)):
    if A[i] % 2 == 0:
        C.append(A[i] * B[i])
    else:
        C.append(A[i] + B[i])

print(C)

print('\nЗадание 3')
x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
x = np.array(x)
min = x[0]

for i in range(len(x)):
    if x[i] != 0:
        if min > x[i] and x[i + 1] == 0:
            min = x[i]

print(min)

print('\nЗадание 4.1')
import pandas as pd

df = pd.read_csv("C:/Users/User/Downloads/archive.zip", encoding="utf-8")

bac = set(df[' education'])

result = dict()

for i in bac:
    result[i] = 0

for i in (df[' education']):
    result[i] += 1

print(result)

print('\nЗадание 4.2')

x = df["age"].mean()
print(x)


print('\nЗадание 4.3')
import matplotlib.pyplot as plt

x = ['Man', 'Woman']
y = [len(df[df[' sex'] == ' Male']), len(df[df[' sex'] == ' Female'])]

n_1, n_2 = plt.subplots()

n_2.bar(x, y)

n_2.set_facecolor('red')
n_1.set_facecolor('white')

plt.show()


print('\nЗадание 4.4')
df = df.drop(df[df[' income'] == ' >50K'].index)
print(df)
