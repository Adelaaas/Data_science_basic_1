print("Задача 1:")
def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
print("Введите координаты 1 точки (x1, y1)>>")
X1 = float(input())
Y1 = float(input())
print("Введите координаты 2 точки (x2, y2)>>")
X2 = float(input())
Y2 = float(input())
print(f'Расстояние между двумя данными точками = {distance(X1, Y1, X2, Y2)}\n')


print("Задача 2:")
s = "Время года"
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
print("Введите месяц>>")
Month = int(input())
print(f'Время года - {season(Month)}\n')


print("Задача 3:")
def is_prime(number):
    flag = True
    for i in range(2, number):
        if number % i == 0:
            flag = False
            break
    return flag
print("Введите целое число в диапазоне от 1 до 1000>>")
Number = int(input())
print(f'Проверка на простое число - {is_prime(Number)}\n')


print("Задача 4:")
lst = [8, 1, 0, 4]
def reverse_list(lst, x = 0):
    if len(lst) <= 1:
        return lst
    lst[x], lst[-x - 1] = lst[-x - 1], lst[x]
    if x + 1 != int(len(lst) / 2):
        return reverse_list(lst, x + 1)
    return lst
print(reverse_list(lst))


print("Задача 5:")
print("Прив" + str.upper('Привет мир!'[4:9]) + "р!\n")


print("Задача 6:")
lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, int(len(lst) / 2), 2):
    if not len(lst) % 2:
        lst[i], lst[-i] = lst[-i], lst[i]
    else:
        lst[i], lst[-i - 1] = lst[-i - 1], lst[i]
print(lst)


print("Задача 7:")
for i in range(501):
    if i%7 == 0 and (i%10 == 8 or i/10 == 8 or i%100/10 == 8):
        print(i)


print("Задача 8:")
lst2 = []
def more_than_five(lst):
    c: int
    for c in range(len(lst)):
        if abs(lst[c]) > 10:
            lst2.append(lst[c])
    return lst2
lis = list(input())
print(more_than_five(lis))