a = input('Имя, возраст')
a = list(a)
print(a[1:-1])
b = input()
a.append(b)
c = input('Фамилия')
c = list(c)
for i in c:
    a.append(i)
print(a)