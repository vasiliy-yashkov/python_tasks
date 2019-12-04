from pylab import *
from numpy import *

import matplotlib
import matplotlib.pyplot as plt

import sys


def load_file(name):
    f = open(name, 'r')
    res = f.readlines()
    f.close()
    return res


def process():
    res = load_file('input.txt')

    res_dic = dict()
    i = 0
    while i < 11:
        res_dic[i + 1] = [0, 0]
        i += 1

    for e in res:
        list_line = e.strip().split(sep="\t")
        res_dic[int(list_line[0])][0] += 1
        res_dic[int(list_line[0])][1] += int(list_line[2])

    for n, e in enumerate(res_dic):
        print(str(e), end=' ')
        if res_dic[e][0] == 0:
            print('-', end=' ')
        else:
            print(float(res_dic[e][1]/res_dic[e][0]), end=' ')
        print('')


def main(argv=sys.argv):

    n = random.randn(100000)

    fig, axes = plt.subplots(1, 2, figsize=(12, 4))

    axes[0].hist(n)
    axes[0].set_title("Default histogram")
    axes[0].set_xlim((min(n), max(n)))

    axes[1].hist(n, cumulative=True, bins=50)
    axes[1].set_title("Cumulative detaled histogram")
    axes[1].set_xlim((min(n), max(n)))

    show()


if __name__ == "__main__":
    main()
