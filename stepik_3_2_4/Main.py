from array import *
import copy


def words_count(s):
    l = s.lower().split()
    hm = dict()
    for el in l:
        if el in hm:
            hm[el] += 1
        else:
            hm[el] = 1
    return hm


def print_dict(m):
    for el in m:
        print(str(el) + ' ' + str(m[el]))


def main():
    s = input()
    print_dict(words_count(s))


if __name__ == "__main__":
    main()
