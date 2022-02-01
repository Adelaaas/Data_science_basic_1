print('Задание 1')
a = [i for i in range(1, 8)]
arr = [[i]*i for i in a if i  % 2 == 0]
print(*a)
print(arr)


print('Задание 2')
x = int(input())
y = int(input())
if -2 <= x <= 2 and -2 <= y <= 2:
    print('YES')
else:
    print('NO')


print('Задание 3')
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
b = []
for i in range(10):
    if (a[i]%2 == 0):
        b.append(a[i])
print(b)


print('Задание 4')
print(f'Привет, {input()}!')


print('Задание 5')
num = int(input())
print(f'The next number for the number {num} is {num+1}. The previous number for number {num} is {num-1}.')