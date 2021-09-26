print("Задача 1: ")

from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print("Введите координаты 1 точки (x1, y1): ")
x1 = float(input())
x2 = float(input())
print("Введите координаты 2 точки (x2, y2): ")
y1 = float(input())
y2 = float(input())
print(f'Расстояние между 2-мя точками = {distance(x1, x2, y1, y2)}')

print("\nЗадача 2: ")


def season(month):
    if month == 1 or month == 2 or month == 12:
        s = "Зима"
        return s
    elif 3 <= month <= 5:
        s = "Весна"
        return s
    elif 6 <= month <= 8:
        s = "Лето"
        return s
    elif 9 <= month <= 11:
        s = "Осень"
        return s


print("Введите месяц: ")
month_1 = int(input())
print(f'Время года - {season(month_1)}')

print("\nЗадача 3: ")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


print("Введите число в диапазоне от 1 до 1000: ")
num_1 = int(input())
print(f'Проверка на простое число - {is_prime(num_1)}')

print("\nЗадача 4: ")

lst = [8, 1, 0, 4]


def reverse_list(lst, num=0):
    if len(lst) <= 1:
        return lst
    lst[num], lst[-num - 1] = lst[-num - 1], lst[num]
    if num + 1 != int(len(lst) / 2):
        return reverse_list(lst, num + 1)
    return lst


print(reverse_list(lst))

print("\nЗадача 5: ")

print(str.upper('Привет мир!'[4:9]))

print("\nЗадача 6: ")

lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(1, int(len(lst) / 2), 2):
    if not len(lst) % 2:
        lst[i], lst[-i] = lst[-i], lst[i]
    else:
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
print(lst)

print("\nЗадача 7: ")

for i in range(501):
    if i % 7 == 0 and '8' in str(i):
        print(i)

print("\nЗадача 8: ")


def more_than_five(lst):
    new_lst = []
    for number in lst:
        if abs(number) > 10:
            new_lst.append(number)
    return new_lst


lst_2 = list(input())
print(more_than_five(lst_2))
