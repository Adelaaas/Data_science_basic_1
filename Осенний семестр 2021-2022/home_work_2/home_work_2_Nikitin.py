import math

# Задача 1
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return dist


s = ""
# Задача 2
def season(month):
    global s
    if month <= 2 or month == 12:
        s = 'winter'
    elif 2 < month <= 5:
        s = 'spring'
    elif 5 < month <= 8:
        s = 'summer'
    else:
        s = 'autumn'
    return 0

# x = int(input())
# season(x)
# print(s)

# Задача 3
def is_prime(x):
    counter = [i for i in range(1, 1001) if x % i == 0]
    judgement = len(counter) == 2
    return judgement


# k = int(input())
#
# print(is_prime(k))

# Задача 4
def reverse_list(lst):
    lst = lst[::-1]
    return lst

# lizt = [1, 1, 1, 1, 3, 4, 3, 4, 5, 7, 9, 0]
# print(reverse_list(lizt))

# Задача 5
print(str.upper('Привет мир!'[4:9]))

# Задача 6
x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = [x[i] for i in range(len(x)) if i % 2 != 0]
for i in range(len(x)):
    if i % 2 != 0:
        x[i] = y.pop()
print(x)

# Задача 7
asn = []
for i in range(501):
    if i % 7 == 0 and i % 10 == 8:
        asn.append(i)
print(*asn)


# Задача 8
def more_than_five(lst):
    lst2 = [i for i in lst if abs(i) > 10]
    return lst2


print(more_than_five([1, 2, 3, 20, -12, 47, -100, 31, 0, 1]))
