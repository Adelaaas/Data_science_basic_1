# Задача №1

def distance(x1, y1, x2, y2):
  if x1 == x2:
    s = abs(y1 - y2)
  elif y1 == y2:
    s = abs(x1 -x2)
  else:
    s = (((x1 - x2)**2)+((y1 - y2)**2))**0,5
  return s


# Задача №2

def season(month)
  s global
  if month == 12 or month == 1 or month == 2:
    s = 'Зима'
  elif month == 3 or month == 4 or month == 5:
    s = 'Весна'
  elif month == 6 or month == 7 or month == 8:
    s = 'Лето'
  elif month == 9 or month == 10 or month == 11:
    s = 'Осень'
    
    
# Задача №4

a = list(input().split(', '))
b = []
l = int(len(a))
for i in range(l-1):
  print(a[l-i-1], end=', ')
print(a[0])


# Задача №5

hello = list('Привет мир!')
bye = []
bye.extend(hello[3:7])
bye = str(bye)
bye.upper()
print(*bye)


# Задача №7
for i in range(500):
  if i % 7 == 0:
    if i % 10 == 8 or 80 <= i % 100 < 90:
      print(i)
      
      
# Задача №8

def more_than_five(lst):
  b = []
  for r in range(len(lst)):
    if abs(int(lst[i])) > 10:
      b.extend(lst[i])
  print(lst)
