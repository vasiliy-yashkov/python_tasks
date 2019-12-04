def main():
    # a = input().split(sep=' ')
    # sum = int(a[0])
    # for i in range(1, len(a)):
    #     sum += int(a[i])
    # print(sum)
    """
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """
    # a = [int(n) for n in input().split(sep=' ')]
    # res = ''
    # for i in range(0, len(a)):
    #     if i == 0:
    #         if len(a) > 2:
    #             res += str(a[i + 1] + a[len(a) - 1])
    #         elif len(a) == 2:
    #             res = str(str(a[i + 1] * 2) + ' ' + str(a[i] * 2))
    #             break
    #         else:
    #             res = str(a[i])
    #     elif i == len(a) - 1:
    #         res += str(a[i - 1] + a[0])
    #     else:
    #         res += str(a[i - 1] + a[i + 1])
    #     res += ' '
    # print(res)
    """
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """
    a = [int(n) for n in input().split(sep=' ')]
    a.sort()

    seen = {}
    dupes = []
    s = ''
    for x in a:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                dupes.append(x)
                s += str(x)
                s += ' '
            seen[x] += 1
    print(s)

if __name__ == "__main__":
    main()
