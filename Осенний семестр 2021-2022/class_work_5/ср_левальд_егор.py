import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#from google.colab import files

a,b,c,d=map(float,input().split())
print(((a-c)**2+(b-d)**2)**0.5)



e=list(map(int,input().split()))
g=list(map(int,input().split()))
c=list()
for i in range(len(e)):
	if e[i]%2==0:
		c.append(e[i]*g[i])
	else:
		c.append(e[i]+g[i])
print(c)



f=list(map(int,input().split()))
x=np.array(f)
h=10000000000000000000000000000000000
for i in range(len(f)-1):
	if(x[i]<h and x[i+1]==0 and x[i]!=0):
		h=x[i]
print(h)





#uploaded = files.upload()
df = pd.read_csv("income_evaluation.csv")
m = 0
for i in df[' education'].isna():
	if i == False:
		m+=1
print(m)
k=list(df["age"])
j=list(df[" sex"])
u=0
y=0
p=0
for i in k:
	p+=int(i)
for i in j:
	if j=="Male":
		u+=1
	else:
		y+=1
o=list(df[" race"])
t=-10
for i in range(o):
	if(k[i]>t and o[i]=="White"):
		t=k[i]
print(t)
fig, ax = plt.subplots()
ax.bar(u, y)
fig.set_facecolor('floralwhite')
plt.show()
print(p/len(k))
df.drop(df[df[' income']=="<=50K"].index,inplace=True)
print(df)