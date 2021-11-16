import numpy as np

n = 5
A = np.random.randint(1, 20, size=n)
print(A)
B = np.random.randint(1, 20, size=n)
print(B)

C = np.arange(n)

for i in range(n):
    if A[i] % 2 == 0:
        C[i] = A[i] * B[i]
    else:
        C[i] = A[i] + B[i]

print(C)