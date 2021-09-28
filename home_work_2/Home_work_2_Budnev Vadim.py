
def run_main():
    print("Номер 1")
    print("Введите x1,y1,x2,y2 через 'Enter'")
    distance(int(input()),int(input()),int(input()),int(input()))
    print("Номер 2")
    print("Введите номер месяца")
    season(int(input()))
    print("Номер 3")
    print("Введите число")
    is_prime(int(input()))
    print("Номер 4")
    print("Введите элементы списка")
    reverse_list(list(map(int, input().split())))
    print("Задание 5")
    text = "Привет мир"
    print(text[3:8].upper())
    print("Задание 6")
    l = list(map(int, input().split()))
    l2 = [i for i in l]
    if len(l) % 2 != 0:
        for i in range(1, len(l), 2):
            l2[i] = l[-i - 1]
    else:
        for i in range(1, len(l), 2):
            l2[i] = l[-i]
    print(l2)
    print("Задание 7")

    for i in range(501):
        if i % 10 == 8 or i // 10 % 10 == 8:
            if i % 7 == 0:
                print(i)

    print("Задание 8")
    more_than_five(list(map(int, input().split())))

def distance(x1, y1, x2, y2):
    s = (((x2 - x1) ** 2) + ((y2 - y1) ** 2)) ** (1/2)
    print(s)

def season(month):
    if (month >= 1 and month <3) or month == 12:
        print("Зима")
    elif month >= 3 and month < 6:
        print("весна")
    elif month >= 6 and month < 9:
        print("Лето")
    elif month >= 9 and month < 12:
        print("Осень")

def is_prime(x):
    count = 0
    for i in range(1, x+1):
        if x % i == 0:
            count += 1
    if count > 2 or count == 1 or count == 0:
        print("False")
    else:
        print("True")


def reverse_list(lst):
    lst = lst[::-1]
    print(lst)

def more_than_five(lst):
    print([i for i in lst if abs(i)>10])

if __name__ == '__main__':
    run_main()

