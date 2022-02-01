from random import randint


X = [[randint(1, 19) for _ in range(6)] for _ in range(7)]

for i in X:
    print(i)

X[-1], X[2] = X[2], X[-1]

print()
for i in X:
    print(i)