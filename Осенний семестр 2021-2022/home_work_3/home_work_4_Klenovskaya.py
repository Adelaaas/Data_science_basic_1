import numpy as np
import math
from random import randint
from math import ceil
from math import floor
print('number 1')
a=np.ones((10,10))
a[1:-1, 1:-1] = 0
print(a)

print('number 2')
a=np.eye(5, k=1)
a[1,2]=2 
a[2,3]=3
a[3,4]=4
print(a)

print('number 3')
X = np.random.rand(5, 10)
Y=np.mean(X[:, :5], axis=1)
print(Y)

print('number 4')
a= np.random.rand(6, 7)
b=a.copy()
b[5]=a[2]
b[2]=a[5]
print(a)
print(b)

print('number 5')
a=np.random.rand(11,11)
a=a.astype('int32')
print(a)

print('number 6')
a=[]
for i in range (-50,50):
    a=np.random.rand(89,67)
cout =0
for k in range (89):
    for n in range(67):
        if a[k,n]!=0:
            cout+=1
print(cout)

print('number 7')
n, m= input().split(' ')
n= int(n)
m= int(m)
table = np.zeros((n,m))
for i in range (n):
    for j in range(m):
        if (i+j)%2!=0:
            table[i, j]=1
print(table)

print('number 8')
a=np.array([float(x) for x in input().split()])
z=[]
for i in range(len(a)):
    if a[i] < 0:
        z.append(floor(a[i]))
    else:
        z.append(ceil(a[i]))
print(z)
print('number 9')
