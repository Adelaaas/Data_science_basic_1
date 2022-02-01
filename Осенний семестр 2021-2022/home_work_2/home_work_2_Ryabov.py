from math import sqrt
from random import randint

# num1


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# num2

s = ''


def season(month):
    global s
    if month == 12 or month == 1 or month == 2:
        s = 'Зима'
    elif 3 <= month <= 5:
        s = 'Весна'
    elif 6 <= month <= 8:
        s = 'Лето'
    elif 9 <= month <= 11:
        s = 'Осень'

# num3


def is_prime(num):
    flag = True
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            flag = False
            break

    if flag:
        return True
    return False

# num4


def reverse_list(lst):
    lst = [lst[i] for i in range(len(lst) - 1, -1, -1)]
    return lst


# num5
print("Привет мир!"[3:8].upper())


# num6


def reverse_odd(lst):
    if len(lst) % 2 == 0:
        for i in range(1, len(lst) // 2, 2):
            lst[i], lst[len(lst) - i] = lst[len(lst) - i], lst[i]
    else:
        for i in range(1, len(lst) // 2, 2):
            lst[i], lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]
    return lst


# num7

for i in range(501):
    if i % 7 == 0 and '8' in str(i):
        print(i, end=' ')

print()
# num8


def more_than_five(lst):
    return list(filter(lambda x: abs(x) > 10, lst))


example = [randint(-100, 100) for i in range(10)]
print(f'Исходный массив: {example},\nНовый массив: {more_than_five(example)}')