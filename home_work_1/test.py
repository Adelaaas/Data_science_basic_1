print("Задание 1")
example = [1, 2, 3, 4, 5, 6, 7]
a = [[i] * i for i in example if i % 2 == 0]
print(a)

print("Задание 2")
print("Введите координаты точек:")
x = int(input())
y = int(input())
if (-1 <= x <= 1) and (-1 <= y <= 1):
    print("Принадлежит")
else:
    print("Не принадлежит")

print("Задание 3")
print("Введите элементы списка:")
print(*(x for x in input().split() if not int(x) % 2))

print("Задание 4")
print("Ваше имя:")
name = input()
temp = f'Привет, {name}!'
print(temp)

print("Задание 5")
print("Введите число:")
num = int(input())
temp_x = f'The next number for the number {num} is {num + 1}. The previous number for the number {num} is {num - 1}.'
print(temp_x)
