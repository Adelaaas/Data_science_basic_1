# -*- coding: utf-8 -*-
"""home_work_3_ivanov.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lGCYQbMrwKnDFYV1zm-ODo9braCg6VWF
"""

!pip install numpy
import numpy as np

"""Задача 1"""

a = np.ones((10,10))
a[1:-1,1:-1] = 0
a

"""Задача 2 (Done)"""

a = np.diag([1,2,3,4], 1)
a

"""Задача 3 (Done)"""

x = np.random.rand(5, 10)
a = 0
m = x.mean()
for i in x:
  x[a] = i.mean() - m
  a += 1
print(x)

"""Задача 4 (Done)"""

a = np.random.rand(6, 7)
b = np.copy(a)
a[2] = b[5]
a[5] = b[2]
a

"""Задача 5 (Done)"""

X = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
a = X.astype('int32')
print(a)

"""Задача 6 (Done)"""

a = np.empty((89, 67), dtype = "int8")
amount = 0
for i in range(a.shape[0]):
  for j in range(a.shape[1]):
    a[i][j] = np.random.randint(-50, 51)
    if a[i][j] != 0:
      amount += 1
print(amount)

"""Задача 8 (Done)"""

a = np.array([1.7, 2.4, -3], float)
b = np.array([-1.3, -2.9, 1], float)
z = np.array([a,b] )
for i in range(z.shape[0]):
  if z.all() > 0:
    z[i] = np.ceil(z[i])
  else:
    z[i] = np.floor(z[i])
z

"""Задача 9 (Done)"""

a = np.array([1,2,3,4,6,5])
b = np.array([4,5,6,7,8,9,10])
z = np.array([])
for i in a:
  for j in b:
    if i == j:
      z = np.append(z, i)
print(np.sort(z))