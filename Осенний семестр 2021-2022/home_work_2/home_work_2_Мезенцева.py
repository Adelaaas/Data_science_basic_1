#задание 1

x1, y1, x2, y2 = map( float, input().split() )
def distance( x1, y1, x2, y2 ):
    dist = ( (x2 - x1)**2 + (y2 - y1)**2 )**0.5
    print(dist)
distance( x1, y1, x2, y2 )

#задание 2

month = int( input() )
s = ""
def season( month ):
    global s
    if month == 12 or month < 3:
        s = "WINTER"
    elif month < 6:
        s = "SPRING"
    elif month < 9:
        s = "SUMMER"
    elif month < 12:
        s = "FALL"
    else:
        s = "error"
    print( s )
season( month )

#задание 3

a = int( input () )
def is_prime( ch ):
    p = 0
    for i in range ( 1, a + 1 ):
        if a % i == 0:
            p += 1
    if p > 2:
        ret = False
    else:
        ret = True
    return ret
print( is_prime( a ) )

#задание 4

base = [int( x ) for x in input().split()]
def reverse_list( lst ):
    ans = []
    for i in range ( len(lst) ):
        ans.append(lst[len(lst)-1-i])
    return ans
print( reverse_list(base) )

#задание 5

print(str.upper('Привет мир!'[3:8]))

#задание 6

base = [int(x) for x in input().split()]
ans = []
for i in range ( len(base) ):
    if i % 2 != 0:
        if len(base) % 2 == 0:
            ans.append(base[len(base)-i])
        else:
            ans.append(base[len(base)-1-i])
    else:
        ans.append(base[i])
print( ans )

#задание 7

ans = []
c = 0
for i in range ( 501 ):
    lst = str(i)
    for j in range ( len(lst) ):
        if lst[j] == "8":
            if i % 7 == 0:
                ans.append(i)
print( ans )

#задание 8

base = [int(x) for x in input().split()]
def more_than_five( lst ):
    ans = []
    for i in range ( len(lst) ):
        if lst[i] > 10 or lst[i] < -10:
            ans.append(lst[i])
    return ans
print( more_than_five(base) )
