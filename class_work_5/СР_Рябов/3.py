import numpy as np

n = 9
max_num = 7
x = np.random.randint(0, max_num, size=n)
# x = np.array([6, 2, 0, 3, 0, 0, 1, 7, 0])
print(x)
is_find = False
min_ = max_num + 1
for i in range(n - 1):
    if x[i + 1] == 0 and min_ > x[i] != 0:
        is_find = True
        min_ = x[i]
if is_find:
    print(min_)
else:
    print('Not found')