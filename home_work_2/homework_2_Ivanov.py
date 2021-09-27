if False:
     #1
    x1,y1,x2,y2 = map(int,input().split())
    def distance(x1_, y1_, x2_, y2_):
        l = ((x2_-x1_)**2+(y2_-y1_)**2)**0.5
        return l
    length = distance(x1, y1, x2, y2)
    print(length)
    #2
    month = int(input())

    def isf(num, a, b, c):
        return num == a or num == b or num == c

    def season(month):
        if isf(month, 12, 1, 2):
            return "zima"
        if isf(month, 3, 4, 5):
            return "vesna"
        if isf(month, 6, 7, 8):
            return "leto"
        return "osen\'"
    print(season(month))
    #3
    num = int(input())
    def  is_prime(num):
        if num ==0 or num == 1:
            return False
        for i in range(2, int(num**0.5 + 1)):
            if num % i == 0:
                return False
        return True
    print(is_prime(num))
    #4
    lst = [8, 1, 0, 4]
    def reverse_list(lst):
        lst = lst[::-1]
        return lst
    print(reverse_list(lst))
    #5
    word = "Привет, мир"
    print(word.upper()[5:9])
    #6
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    def f(x):
        y = x[::-1]
        for i in range(len(y)):
            if i % 2 == 0:
                y[i] = x[i]
        return y
    print(f(x))
    #7
    for i in range(500):
        y = i
        while y != 0:
            g = y % 10
            y //= 10
            if g == 8 and i % 7 == 0:
                print(i, " ")
#8
arr = [111, 18, 3, 7, 76, 5, -11, 4, -3]
def more_than_five(lst):
    spisok = []
    for i in range(len(lst)):
        if abs(lst[i]) > 10:
            spisok.append(lst[i])
    return spisok
print(more_than_five(arr))
