from array import *
import copy


# def f(n):
#     if n <= -2:
#         return 1 - pow((n + 2), 2)
#     elif -2 < n <= 2:
#         return -n / 2
#     elif n > 2:
#         return pow((n - 2), 2) + 1

def modify_list(l):
    i = len(l) - 1
    while i >= 0:
        if l[i] % 2 == 0:
            l[i] = int(l[i] / 2)
        else:
            l.remove(l[i])
        i -= 1


def main():
    # n = float(input())
    # print(f(n))
    lst = [1, 2, 3, 4, 5, 6]
    print(modify_list(lst))  # None
    print(lst)  # [1, 2, 3]
    modify_list(lst)
    print(lst)  # [1]

    lst = [10, 5, 8, 3]
    modify_list(lst)
    print(lst)  # [5, 4]

    lst = [1, 3, 5, 7]
    modify_list(lst)
    print(lst)  # [5, 4]

if __name__ == "__main__":
    main()
