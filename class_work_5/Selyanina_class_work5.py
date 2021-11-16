# -*- coding: utf-8 -*-
"""Селянина_№4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1vnyMSb1e5J_GSmwkJCcTOgiacPdUWkSE

Задание 1
"""

from math import sqrt
def distance(x1, y1, x2, y2):
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)
 
x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())
print(distance(x1, x2, y1, y2))

"""Задание 2"""

a = [1, 2, 6, 5, 2, 1]
b = [2, 6, 3, 4, 2, 1]
c = []
for i in range(len(a)):
  if a[i] % 2 == 0:
    c.append(a[i] * b[i])
  else:
    c.append(a[i] + b[i])

print(c)

"""Задание 3"""

import numpy as np
 
x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
arr = []
for i in range(len(x)):
  if x[i] == 0:
    arr.append(x[i - 1])
for i in arr:
  if i == 0:
    arr.remove(i)
print(min(arr))

"""Задание 4.1-4.4"""

from google.colab import files
uploaded = files.upload()

import pandas as pd

df = pd.read_csv('income_evaluation.csv')
df.head()

df[' education'].value_counts()

m_age = df['age'].mean()
print(round(m_age))

import matplotlib.pyplot as plt

x = ['Мужчины', 'Женщины']
y = [len(df[df[' sex'] == ' Male']), len(df[df[' sex'] == ' Female'])]

fig, ax = plt.subplots()
ax.bar(x, y)

plt.show()

df = df.drop(df[df[' income'] == ' >50K'].index)
df

print(df[df[' race'] == ' White']['age'].max())