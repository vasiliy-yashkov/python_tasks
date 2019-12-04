def lcd(n1, n2):
    if n1 == n2:
        return n1
    d = n1 - n2
    if d < 0:
        d = -d
        div = lcd(n1, d)
    else:
        div = lcd(n2, d)
    return div


def lcm(n1, n2):
    return int(n1 * n2 / lcd(n1, n2))


def main():
    # x = int(input())
    # sum = x
    # while x != 0:
    #     x = int(input())
    #     sum += x
    #
    # print(sum)
    x = int(input())
    y = int(input())

    print(lcm(x, y))

if __name__ == "__main__":
    main()
