import sys


def main(argv=sys.argv):
    dc = dict()
    n = int(input())
    while n > 0:
        l = input().split(';')
        if l[0] in dc:
            dc[l[0]][0] += 1
            if int(l[1]) > int(l[3]):
                dc[l[0]][1] += 1
                dc[l[0]][4] += 3
            if int(l[1]) == int(l[3]):
                dc[l[0]][2] += 1
                dc[l[0]][4] += 1
            if int(l[1]) < int(l[3]):
                dc[l[0]][3] += 1
        else:
            tl = [0 for i in range(5)]
            tl[0] = 1
            if int(l[1]) > int(l[3]):
                tl[1] += 1
                tl[4] += 3
            if int(l[1]) == int(l[3]):
                tl[2] += 1
                tl[4] += 1
            if int(l[1]) < int(l[3]):
                tl[3] += 1
            dc[l[0]] = tl

        if l[2] in dc:
            dc[l[2]][0] += 1
            if int(l[3]) > int(l[1]):
                dc[l[2]][1] += 1
                dc[l[2]][4] += 3
            if int(l[1]) == int(l[3]):
                dc[l[2]][2] += 1
                dc[l[2]][4] += 1
            if int(l[3]) < int(l[1]):
                dc[l[2]][3] += 1
        else:
            tl = [0 for i in range(5)]
            tl[0] = 1
            if int(l[3]) > int(l[1]):
                tl[1] += 1
                tl[4] += 3
            if int(l[1]) == int(l[3]):
                tl[2] += 1
                tl[4] += 1
            if int(l[3]) < int(l[1]):
                tl[3] += 1
            dc[l[2]] = tl

        n -= 1

    for cnt, name in enumerate(dc):
        print(name + ':', end=' ')
        for e in dc[name]:
            print(str(e), end=' ')
        print('')


if __name__ == "__main__":
    main()
