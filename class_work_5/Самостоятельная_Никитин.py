import numpy as np
import pandas as pd
import math
# Задание 1
x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
print(math.sqrt((x2-x1)**2 + (y2-y1)**2))

# Задание 2
A = [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 16]
B = [2, 4, 5, 6, 3, 3, 5, 7, 11, 13, 14, 15, 11]
C = [0]*len(A)
for i in range(len(A)):
    if A[i] % 2 == 0:
        C[i] = A[i]*B[i]
    elif A[i] % 2 != 0:
        C[i] = A[i]+B[i]
print(*C)

# Задание 3
x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
min = 0
for i in range(len(x)):
    if i + 1 < len(x) and x[i+1] == 0 and x[i] != 0:
        if min == 0:
            min = x[i]
        elif x[i] < min:
            min = x[i]
print(min)

# Задание 4
df = pd.read_csv("income_evaluation.csv")
df.head()
counter = 0
for i in df[' education'].isna():
    if i == False:
        counter+= 1
print(counter)
print(round(np.mean(df['age'])))

df = df.drop(df[df[' income'] == ' >50K'].index)
print(df[' income'])