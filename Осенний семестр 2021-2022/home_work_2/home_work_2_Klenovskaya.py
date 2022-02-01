from math import sqrt
from random import randint
print('Задание 1')
x1, y1, x2, y2 = map(float, input().split())
def distance(x1, y1, x2, y2):
    distantion = sqrt((x2-x1)**2 + (y2-y1)**2)
    print(distantion)
distance(x1, y1, x2, y2)


print('Задание 2')
s = " "
month = int(input())
def season(month):
    if month == 12 or month <3:
        s = "зима"
    elif 2 < month < 6:
        s = "весна"
    elif 5 < month < 9:
        s = "лето"
    elif 8 < month < 12:
        s = "осень"
    else:
        s = "ошибка"
    print(s)
season(month)


print('Задание 3')
def is_prime(num):
    flag = True
    if num == 0 or num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            flag = False
            break
    return flag
num = int(input())
print(f'Проверим на простое число - {is_prime(num)}\n')

    
print('Задание 4')
lst = [8, 1, 0, 4]
def reverse_list(lst):
    lst = [lst[i] for i in range(len(lst)-1, -1, -1)]
    return lst
print (reverse_list(lst))


print('Задание 5')
print(str.upper("Привет мир!"[3:8]))


print('Задание 6')
lst = []
for i in range(100):
    lst.append(i)
for j in range(1, int(len(lst) / 2), 2):
    if not len(lst) % 2:
        lst[j], lst[-j] = lst[-j], lst[j]
    else:
        lst[j], lst[-j-1] = lst[-j-1], lst[j]
print(lst)


print('Задание 7')
answer = []
for i in range(501):
    if i % 7 == 0 and '8' in str(i):
        answer.append(i)
print(answer)


print('Задание 8')
lst = [randint(-100, 100) for j in range(10)]
def more_than_five(lst):
    answer=[]
    for i in range(len(lst)):
        if lst[i] > 10 or lst[i] < -10:
            answer.append(lst[i])
    return answer
print(more_than_five(lst))