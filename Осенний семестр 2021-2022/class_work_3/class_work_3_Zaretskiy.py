import numpy as np

# №1
print("№1")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr)
print(arr[0,0], arr[1,1], arr[2,2])

# №2
print("\n№2")
print(arr[:, 1])

# №3
print("\n№3")
print(arr.shape)
print(arr.flatten(),arr.flatten().shape)


# №4
print("\n№4")
for y in range(arr.shape[1]):
  print('Стобец:',y)
  for x in range(arr.shape[0]):
    print(arr[x,y])
for x in range(arr.shape[0]):
    print('Строка:', x)
    for y in range(arr.shape[1]):
        print(arr[x, y])

# №5
print("\n№5")
summ = 0
n = 0
h = 0
for x in range(arr.shape[0]):
  for y in range(arr.shape[1]):
    summ = summ + arr[x, y]
    h += 1
n = summ/h
print(summ, n)