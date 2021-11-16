# -*- coding: utf-8 -*-
"""class_work_5_ivanov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15XXjbKPXwFPPatkBRIOqm43anRmldyr-

Number 1
"""

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
def distance(x1, y1, x2, y2):
  return ((x2-x1)**2+(y2-y1)**2)**0.5
print(distance(x1, y1, x2, y2))

"""Number 2

"""

import numpy as np
a = np.array([1, 2, 3], int)
b = np.array([0, 1, 1], int)
c = np.copy(a)
for i in range(len(a)):
  if(a[i] % 2 == 0):
    c[i] = a[i] * b[i]
  else:
    c[i] = a[i] + b[i]
print(c)

"""Number 3"""

x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
min = 999
for i in range(len(x) - 1):
  if(x[i+1] == 0 and x[i] < min and x[i] != 0):
    min = x[i]
print(min)

"""Number 4"""

import matplotlib.pyplot as plt
from google.colab import files
uploaded = files.upload()
import pandas as pd
df = pd.read_csv("income_evaluation.csv")
df.head()
#1
a = df[' education'].value_counts()
#2
srvoz = df['age'].mean()
#3
m = f = 0
for i in df[' sex']:
  if (x == 'Male'):
   m += 1
else:
    f += 1
fig, ax = plt.subplots()
ax.bar(f, m)
fig.set_facecolor('floralwhite')
plt.show()
#4
df.drop(df[df[' income'] == ' >50K'].index)
