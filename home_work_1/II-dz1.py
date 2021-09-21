#1
spisok = [1,2,3,4,5,6,7]
enn = [[i]*i for i in spisok if i % 2 == 0]
print(enn,'\n')
#2
x,y = map(int,input().split())
if x >= -1 and x <= 1 and y <= 1 and y >= -1:
    print('da')
else:
    print('net')
#3
ghgh = [1,2,3,4,5,6,7,8,9]
o = []
for i in range(len(ghgh)):
    if ghgh[i] % 2 == 0:
        o.append(ghgh[i])
print(o)
#4
print('Vvedite svoe imia')
a = str(input())
print('Привет,', a,'!')
#5
a = int(input())
b = a - 1
c = a + 1
print('The next number for the number',a,'is',c,'.','The previous number for the number',a,'is',b,'.')