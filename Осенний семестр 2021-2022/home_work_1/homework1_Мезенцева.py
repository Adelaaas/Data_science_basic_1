#задание 1

base = [1, 2, 3, 4, 5, 6, 7]
ans = [i for i in base]
ans2 = [[i] * i for i in base if i % 2 == 0]
print( ans, ans2 )

#задание 2

x, y = map( int, input().split() )
if x >= -1 and x <= 1:
    if y >= -1 and y <= 1:
        print( "YES" )
    else:
        print( "NO" )
else:
    print( "NO" )

#задание 3

A = [12, 12, 55, 1, 2, 4, 7]
B = []
s = -1
for i in range ( 7 ):
    s = A[i] % 2
    if s == 0:
        B.append(A[i])
print( B )

#задание 4

name = input()
names = name + "!"
print( "Привет, ", names )

#задание 5

a = int( input() )
b = a - 1
c = a + 1
print(f"The next number for the number {a} is {c}. The previous number for the number {a} is {b}." )
