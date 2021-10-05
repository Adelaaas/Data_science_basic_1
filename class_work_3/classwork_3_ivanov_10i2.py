import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], int)
#1
print(a[0, 0], a[1, 1], a[2, 2])
#2
print(a[1,:])
#3
print(np.shape(a))
b = a.flatten()
print(b)
#4
for l in range(a.shape[1]):
  print('столбец',l)
  for i in range(a.shape[0]):
    print(a[i,l])
#5
c = 0
g = 0
for x in a:
  c+=x
for y in c:
  g += y
print("sum =", g)
print("srznah =",g/(len(a[0, :])+len(a[1, :])+len(a[2, :])))
