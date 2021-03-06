print("Задача №1")

from math import sqrt


def distance(x1, y1, x2, y2):
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


print("Введите x1, y1, x2, y2: ")
x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(f'Расстояние между 2-мя точками = {distance(x1, y1, x2, y2)}')

print("\nЗадача №2")


def season(month):
    if month == 1 or month == 2 or month == 12:
        s = "зимы"
        return s
    if month == 3 or month == 4 or month == 5:
        s = "весны"
        return s
    if month == 6 or month == 7 or month == 8:
        s = "лета"
        return s
    if month == 9 or month == 10 or month == 11:
        s = "осени"
        return s


print("Введите номер месяца: ")
month_1 = int(input())
print(f'Это месяц {season(month_1)}')

print("\nЗадача №3")


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    else:
        return True


print("Введите число:")
num_1 = int(input())
print(is_prime(num_1))

print("\nЗадача №4")

lst = [8, 1, 0, 4]


def reverse_list(lst, num=0):
    if len(lst) <= 1:
        return lst
    lst[num], lst[-num - 1] = lst[-num - 1], lst[num]
    if num + 1 != int(len(lst) / 2):
        return reverse_list(lst, num + 1)
    return lst


print(reverse_list(lst))

print("\nЗадача №5")

print(str.upper('Привет мир!'[3:8]))

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
    print([i for i in lst if abs(i)>10])

more_than_five(list(map(int, input().split())))