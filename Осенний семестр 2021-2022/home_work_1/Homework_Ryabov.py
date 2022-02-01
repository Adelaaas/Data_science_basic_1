import random

# Num1

print('-'*10)
print('Задание 1')

ex = [i for i in range(1, 8)]
print(*ex)
arr = [[i] * i for i in ex if i % 2 == 0]
print(arr)

# Num2

print('-'*10)
print('Задание 2')

x = int(input())
y = int(input())

print('Принадлежат' if -1 <= x <= 1 and -1 <= y <= 1 else 'Не принадлежат')

# Num3

print('-'*10)
print('Задание 3')

arr = [random.randint(-100, 100) for i in range(10)]

print("Исходный массив:", arr)

print([i for i in arr if i % 2 == 0])

# Num4

print('-'*10)
print('Задание 4')

print(f"Привет, {input()}!")

# Num5

print('-'*10)
print('Задание 5')

inp = int(input())
print(f"The next number for the number {inp} is {inp+1}. The previous number for the number {inp} is {inp-1}.")