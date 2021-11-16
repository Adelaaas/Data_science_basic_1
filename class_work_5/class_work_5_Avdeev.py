from math import sqrt
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ex1
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2))

# ex 2
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]
C = B

for i in range(len(A)):
    if i % 2 == 0:
        C[i] = A[i] * B[i]
    else:
        C[i] = A[i] + B[i]
print(C)

# ex 3

x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
min_x = x[0]

for i in range(len(x) - 1):
    if x[i + 1] == 0 and x[i] != 0 and x[i] < min_x:
        min_x = x[i]
print(min_x)

# ex 4.1
df = pd.read_csv("income_evaluation.csv")
print(df[' education'].value_counts())

# ex 4.2
print(df['age'].mean())

# ex 4.3
x = ['Мужчины', 'Женщины']
y = [len(df[df[' sex'] == ' Male']), len(df[df[' sex'] == ' Female'])]
fig, ax = plt.subplots()
ax.bar(x, y)

# ex 4.4
df = df.drop(df[df[' income'] == ' >50K'].index)

# ex 4.5
print(df[df[' race'] == ' White']['age'].max())
