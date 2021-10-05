
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]],int)
# 1 задание
print(a.tolist(),'\n',a[0,0],a[1,1],a[2,2],'\n\n\n\n')
# 2 задание
print(a[1:2,:],'\n\n\n\n')
# 3 задание
print(a.shape)
b=a.flatten()
print(b.flatten(),b.shape,'\n\n\n\n')
# 4 задание
for y in range(a.shape[1]):
  print('stolbez',y)
  for x in range(a.shape[0]):
    print(a[x,y])
print('\n\n\n\n')
# 5 задание
v=0
n=0
for x in range(a.shape[0]):
  for y in range(a.shape[1]):
    v=v+1
    n=n+int(a[x,y])

print(n,"и",a.sum(),'\n',n/v,"и",a.mean()) 