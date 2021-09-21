# задание 1
arr = [1, 2, 3, 4, 5, 6, 7, 8]
for i in arr:
    if i % 2 == 0:
        a1 = i
        a2 = [i] * i
        print(a1, a2)

# задание 2
x = int(input())
y = int(input())
if -1 <= x <= 1 and -1 <= y <= 1:
    print("принадлежит")
else:
    print("нет")

# задание 3
A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
B = []
for i in A:
    if i % 2 == 0:
        B.append(i)
print(B)

# задание 4
name = input()
print(f'Привет, {name}!')

# задание 5
num = int(input())
print(f"The next number for the number {num} is {num + 1}. The previous number for the number {num} is {num - 1}.")
