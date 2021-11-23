def f(x1,x2,y1,y2):
	return ((x1-x2)**2+(y1-y2)**2)**0.5
x1,x2,y1,y2=map(int,input().split())
print(f(x1,x2,y1,y2))

def h(a):
	global s
	if(a==12 or a>=1 and a<=2):
		s="Зима"
	elif(a>=3 and a<=5):
		s="Весна"
	elif(a>=6 and a<=8):
		s="Лето"
	elif(a>=9 and a<=11):
		s="Осень"
d=int(input())
h(d)
print(s)

def p(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0 :
            return False    
    return True
g=int(input())
print(p(g))

def v(c):
	d=c[::-1]
	return d
c=list(map(int,input().split()))
c=v(c)
print(c)

l="Привет мир!"
print(l[3:8])

e=list(map(int,input().split()))
for i in range(len(e)//2):
	if(i%2==1):
		e[i],e[len(e)-1-i]=e[len(e)-1-i],e[i]
print(e)

for i in range(501):
	if(i%7==0 and (i%10==8 or i/10%10==8 or i/100==8)):
		print(i)

def more_than_five(lst):
	vq=[]
	for i in lst:
		if(abs(i)>10):
			vq.append(i)
	return vq
xz=list(map(int,input().split()))
print(more_than_five(xz))