print("Задание номер 1")
ex = [1, 2, 3, 4, 5, 6, 7]
for i in ex:
    arr = [i] * i
    if i % 2 == 0:
        print(arr)
print("Задание номер 2")
print("Введите координаты точек")
x = int(input())
y = int(input())
if (x >= -1 and x <= 1) and (y >= -1 and y <= 1):
    print("Принадлежит")
else:
    print("Не принаджлежит")
print("Задание номер 3")
print("Введите элементы списка через пробел")
b=[]
lis = list(map(int, input().split()))
for i in lis:
    if i % 2 == 0:
        b=b+[i]
print(b)
print("Задание номер 4")
print("Введите имя")
name = input()
text = f'Привет, {name}!'
print(text)
print("Задание номер 5")
print("Введите число")
num = int(input())
text_1 = f'The next number for the number {num} is {num+1}. The previous number for the number {num} is {num-1}.'
print(text_1)