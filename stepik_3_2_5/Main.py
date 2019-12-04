from array import *
import copy

def f(n):
    return n * 100;

def find_results(l):
    hm = dict()
    for el in l:
        if el not in hm:
            hm[el] = f(el)
    return hm


def print_dict(m):
    for el in m:
        print(str(m[el]))


def main():
    l = list()
    n = int(input())
    i = 0
    while i < n:
        l.append(int(input()))
        i += 1

    hm = find_results(l)
    for el in l:
        print(hm[el])


if __name__ == "__main__":
    main()
