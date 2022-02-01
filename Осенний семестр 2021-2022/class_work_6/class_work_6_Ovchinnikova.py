import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print('Задание №1')
def square(a):
  p=a*4
  s=a*a
  d=2**(0.5)*a
  return p, s, d
print(square(int(input())))
print()

print('Задание №2')
print('Введите a=')

a=list(map(int,input().split()))
print('Введите b=')
b=list(map(int,input().split()))
c=[]
o=False
for i in range(0,len(a)):
  for j in range(0,len(b)):
    if (a[i]==b[j]):
      o=False
      break
    else:
      o=True
  if (o==True):
    c.append(a[i])
  o=False
print(c)

print('Задание №3')
print('Введите x через пробел: ')
x = list(map(int,input().split()))
x = np.array(x)
max=-1
for i in range(1, len(x)):
  if (x[i]>=max and x[i-1]==0):
    max=x[i]
    p=i;
#if (x[0]>max and x[1]==0):
  #max = x[1]
if (max==-1 and x[p]!=-1):
  print('NO')
else:
  print(max)

print('Задание №4.1')
df = pd.read_csv("C:\\Users\\Lenovo\\Desktop\\titanic.csv")
print(df)
print(df['Age'].mean())
print()

print('Задание №4.3')
print(df.isna().sum().sum())

print('Задание №4.4')
print(df[df['Fare'].max()])

print('Задание №4.2')
X=['0','1']
Y=[len(df[df[' Survived'] == ' 0']), len(df[df[' Survived'] == ' 1'])]
fig, ax = plt.setplots()
ax.bar(X, Y)
plt.show()

