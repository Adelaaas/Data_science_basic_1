# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z_N02Fd1BTDcyE6mHwRqSB3bveKntgmF
"""

#Задание №1
list_1 = [1, 2, 3, 4, 5, 6, 7]
print(list_1)
A = [[i]*i for i in list_1 if i % 2 == 0]
print(A)

#Задание №2
x = int(input())
y = int(input())
if (-1 <= x <= 1 and -1 <= y <= 1):
  print("Да, принадлежит")
else:
  print("Увы, нет:(")

#Задание №3

import random
A = [random.randint(-100, 100) for i in range(10)]

print(A)

print([i for i in A if i % 2 == 0])

#Задание №4
name = input()
text = f'Привет, {name}!'
print(text)

#Задание №5
Num = int(input())
text = f'The next number for the number {Num} is {Num + 1}. The previous number for the number {Num} is {Num - 1}.'
print(text)
