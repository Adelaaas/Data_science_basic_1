# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/gist/stasya185/79d79d75a5f95067c745fe7c6540c3bb/untitled0.ipynb

#Задание №1
"""

a = [1,2,3,4,5,6,7]
i = int(input())
print(f"{i+1} элемент ряда: {a[i]}")

"""#Задание №2"""

x = int(input())
y = int(input())
if (x <= 2 and y <= 2) and (x >= -2 and y >= -2):
  print("принадлежат")
else:
    print("не принадлежат")

"""#Задание №3"""

А = [1, 2, 4, 5, 6, 7, 7]
B = []
for i in range(6):
  if (A[i]%2 == 0):
    B.append(A[i])
print (B)

"""#Задание №4"""

name=input()
print(f'Привет, {name}!')

"""#Задание №5"""

number=int(input())
print(f'The next number for the number {number} is {number+1}. The previous number for the number {number} is {number-1}.')