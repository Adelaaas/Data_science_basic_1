#Задача 1

def distance(x1, y1, x2, y2):
  dist=(((x1 - x2)**2) + ((y1 - y2)**2))**0.5
  return dist
x1=int(input())
y1=int(input())
x2=int(input())
y2=int(input())
distance(x1, y1, x2, y2)

#Задача 2

month = int(input())
s = ""
def season(month):
    global s
    if month==12 or month<3:
        s = "Зима"
    elif month < 6:
        s = "Весна"
    elif month < 9:
        s = "Лето"
    elif month < 12:
        s = "Осень"
    print(s)
season(month)

#Задача 3

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    else:
        return True

num = int(input())
is_prime(num)

#Задача 4

def list_reverse(a):
  a = a[::-1]
  print(a)

lst = [8, 1, 0, 4]
list_reverse(lst)

#Задача 5

s = "Привет мир!"
s = s[3:8].upper()
print(s)

#Задача 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
ans = []
for i in range (len(x)):
    if i % 2 != 0:
        if len(x) % 2 == 0:
            ans.append(x[len(x)-i])
        else:
            ans.append(x[len(x)-i-1])
    else:
        ans.append(x[i])
print(ans)

#Задача 7

for i in range(501):
  a = i
  b = 0
  if i % 7 == 0:
    while a != 0:
      b = b + 1
      a = a // 10
    a = i
    for j in range(b):
      if (a % 10 == 8):
        print(i)
        break
      a = a // 10

#Задача 8

def more_than_five(lst):
  for i in range(len(lst)):
    if abs(lst[i]) > 10:
      lst1.append(lst[i])
  print(lst1)

lst = [12, 15, 2, 31, -4, -25, 6, 10, -10, 0]
lst1 = []
more_than_five(lst)
