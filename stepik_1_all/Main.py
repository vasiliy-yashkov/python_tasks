from math import sqrt


def main():
    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # print(pow(2014.0, 14))
    # print(7 // 3)
    # x = int(input())
    # y = int(input())
    # z = int(input())
    # a = x // 60;
    # b = x - a * 60;
    # a += y;
    # b += z;
    # c = b // 60;
    # a += c;
    # b -= c * 60;

    # print(a)
    # print(b)
    # a = 1
    # b = 2
    # print ((a and b) or ((not a) and (not b)))

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # x = 5
    # y = 10
    # print (y > x * x or y >= 2 * x and x < y)

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # a = True
    # b = False
    # print (a and b or not a and not b)

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # a = int(input())
    # b = int(input())
    # h = int(input())
    #
    # if h >= a and h <= b:
    #     print ("Это нормально")
    # elif h < a:
    #     print("Недосып")
    # else:
    #     print("Пересып")

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # y = int(input())

    # print(y % 4)
    # print(y % 100)
    # print(y % 400)

    # if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
    #     print("Високосный")
    # else:
    #     print("Обычный")

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # print("239" < "30" and 239 < 30)
    # print("239" < "30" and 239 > 30)
    # print("239" > "30" and 239 < 30)
    # print("239" > "30" and 239 > 30)
    # print("123" + "42")

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # a = int(input())
    # b = int(input())
    # c = int(input())
    #
    # p = (a + b + c) / 2
    #
    # x = float(sqrt(p * (p - a) * (p - b) * (p - c)))
    #
    # print(x)

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # a = int(input())
    #
    # if (a > -15 and a <= 12) or (a > 14 and a < 17) or (a >= 19):
    #     print("True")
    # else:
    #     print("False")

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # x = float(input())
    # y = float(input())
    # op = input()
    #
    # if op == "+":
    #     print(x + y)
    # elif op == "-":
    #     print(x - y)
    # elif op == "*":
    #     print(x * y)
    # elif op == "/":
    #     if y == 0:
    #         print("Деление на 0!")
    #     else:
    #         print(x / y)
    # elif op == "pow":
    #     print(pow(x, y))
    # elif op == "mod":
    #     if y == 0:
    #         print("Деление на 0!")
    #     else:
    #         print(x % y)
    # elif op == "div":
    #     if y == 0:
    #         print("Деление на 0!")
    #     else:
    #         print(x // y)

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # type = input()
    #
    # if type == "треугольник":
    #     a = int(input())
    #     b = int(input())
    #     c = int(input())
    #     p = (a + b + c) / 2
    #
    #     x = float(sqrt(p * (p - a) * (p - b) * (p - c)))
    #
    #     print(x)
    # elif type == "прямоугольник":
    #     a = int(input())
    #     b = int(input())
    #     x = a * b
    #
    #     print(x)
    # else:
    #     a = int(input())
    #     print(3.14 * pow(a, 2))

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # a = int(input())
    # b = int(input())
    # c = int(input())
    #
    # max = a
    # min = a
    # if b > max:
    #     max = b
    # if b < min:
    #     min = b
    # if c > max:
    #     max = c
    # if c < min:
    #     min = c
    # print(max)
    # print(min)
    # print(a + b + c - max - min)

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    # n = int(input())
    #
    # if n == 0:
    #     print(str(n) + " программистов")
    # elif n % 10 == 0 or n % 10 == 5 or n % 10 == 6 or n % 10 == 7 or n % 10 == 8 or n % 10 == 9 or (n >= 11 and n <=19) or (n >= 111 and n < 119) or (n >= 211 and n < 219) or (n >= 311 and n < 319) or (n >= 411 and n < 419) or (n >= 511 and n < 519) or (n >= 611 and n < 619) or (n >= 711 and n < 719) or (n >= 811 and n < 819) or (n >= 911 and n < 919):
    #     print(str(n) + " программистов")
    # elif n % 10 == 1 and n != 11:
    #     print(str(n) + " программист")
    # elif n % 10 == 2 or n % 10 == 3 or n % 10 == 4:
    #     print(str(n) + " программиста")

    '''
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    '''

    x = str(input())
    sum1 = int(x[0]) + int(x[1]) + int(x[2])
    sum2 = int(x[3]) + int(x[4]) + int(x[5])
    if sum1 == sum2:
        print('Счастливый')
    else:
        print('Обычный')

if __name__ == "__main__":
    main()