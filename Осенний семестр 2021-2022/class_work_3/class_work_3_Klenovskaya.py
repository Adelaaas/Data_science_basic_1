import numpy as np
print('number 1')
a=np.array([[1,2,3],[4,5,6],[7,8,9]], int)
print(a[0,0],a[1,1],a[2,2])


print('number 2')
print(a[0:,1])


print('number 3')
print(a.shape)
anew=a.flatten()
print(anew.flatten(), anew.shape)


print('number 4')
for y in range(a.shape[1]):
  print('stolbik',y)
  for x in range(a.shape[0]):
    print(a[x,y])


print('number 5')
kolvo=0
n=0
for i in range(a.shape[0]):
  for j in range(a.shape[1]):
    kolvo=kolvo+1
    n=n+int(a[i,j])
print(n,"and",a.sum()," ",n/kolvo,"and",a.mean())