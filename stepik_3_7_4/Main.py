import sys


def main(argv=sys.argv):
    op_count = int(input())
    list_dir = list()
    while op_count > 0:
        list_dir.append(input().strip().split())
        op_count -= 1
    xc = 0
    yc = 0
    for cnt, direct in enumerate(list_dir):
        if direct[0] == 'север':
            yc += int(direct[1])
        elif direct[0] == 'восток':
            xc += int(direct[1])
        elif direct[0] == 'юг':
            yc -= int(direct[1])
        else:
            xc -= int(direct[1])
    print(str(xc) + ' ' + str(yc))


if __name__ == "__main__":
    main()
