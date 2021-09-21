#a = input('Ввести имя: ')
#a = list(a)
#a = a[1:-1]

#b = input('Ввести класс: ')
#a.append(b)

#c = input('Ввести фамилию: ')
#a+=c
#print(a)
#1
j = [1, 2, 3, 4, 5, 6, 7]
u = [[i]*i for i in j if i % 2 == 0]
print(j[i], u)


#2
x = int(input())
y = int(input())
if -1<= x <= 1 and -1 <= y <= 1:
    print('Принадлежит')
else:
    print('Не принадлежит')

#3
a = input()
a.split()
a = list(a)
b = []
for i in a:
    if i%2==0:
        b.append(i)
print(b)

#4
n = input()
print('Привет', n, '!')


#5
a
k= int(input())
print('The next number for the number', str(k), 'is', str(k+1)+'.', 'The previous number for the number', str(k), 'is', str(k-1)+'.')
