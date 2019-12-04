import sys
import requests

def main(argv = sys.argv):
    # s = ""
    # f = True
    # for e in argv:
    #     if f:
    #         f = False
    #         continue
    #     s += (str(e) + ' ')
    # print(s)
    f = open('file.txt', 'r')
    addr = f.readline().strip()
    r = requests.get(addr, allow_redirects=True)
    open('temp.txt', 'wb').write(r.content)
    ff = open('temp.txt', 'r')

    res = ff.read().splitlines()

    print(len(res))


if __name__ == "__main__":
    main()
