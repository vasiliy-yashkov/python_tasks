from array import *
import copy


def update_dictionary(d, key, value):
    if key in d:
        v = list(d[key])
        v.append(value)
        d[key] = v
    elif 2 * key in d:
        v = list(d[2 * key])
        v.append(value)
        d[2 * key] = v
    else:
        d[2 * key] = [value]


def main():
    d = {}
    print(update_dictionary(d, 1, -1))  # None
    print(d)  # {2: [-1]}
    update_dictionary(d, 2, -2)
    print(d)  # {2: [-1, -2]}
    update_dictionary(d, 1, -3)
    print(d)  # {2: [-1, -2, -3]}


if __name__ == "__main__":
    main()
