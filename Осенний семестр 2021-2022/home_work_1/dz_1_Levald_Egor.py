a = [1, 2, 3, 4, 5, 6, 7]
for i in a:
	if i % 2 == 0:
		print([i]*i)


x = int(input())
y = int(input())
if(x>=-1 and x<=1 and y>=-1 and y<=1):
	print("ДА")
else :
	print("НЕТ")
q=list(map(int,input().split()))
v=list()



for i in q:
	if i%2==0:
		v.append(i)
print(v)



h=input()
print(f'Привет, {h}!')



k = int(input())
print(f'The next number for the number {k} is {k+1}. The previous number for the number {k} is {k-1}.')