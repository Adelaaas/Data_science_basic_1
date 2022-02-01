# 1
arr = [1, 2, 3, 4, 5, 6, 7]
res = [i for i in arr]
res2 = [[i]*i for i in arr if i % 2 == 0]
print(res, res2)

# 2
x = int(input())
y = int(input())
print(-1 <= x <= 1 and -1 <= y <= 1)

# 3
A = [1, 2, 3, 4, 5, 6, 7, 7]
res3 = [i for i in A if i % 2 == 0]
print(res3)

# 4
name = input()
print(f"Привет, {name}!")

# 5
number = int(input())
print(f"The next number for the number {number} is {number+1}. "
      f"The previous number for the number {number} is {number-1}.")

