import numpy as np
n = int(input())
m = int(input())

Z = np.zeros((n, m), dtype=int)
color = 0

for i in range(len(Z)):
    for j in range(len(Z[i])):
        if i == 0:
            Z[i][j] = color
            color = abs(color - 1)
        else:
            Z[i][j] = abs(Z[i-1][j] - 1)

print(Z)