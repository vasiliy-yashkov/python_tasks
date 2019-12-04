import sys
import requests


def load_file(addr):
    if not addr.startswith('http'):
        addr = 'https://stepic.org/media/attachments/course67/3.6.3/' + addr
    r = requests.get(addr, allow_redirects=True)
    open('temp.txt', 'wb').write(r.content)
    ff = open('temp.txt', 'r')
    res = ff.read()
    ff.close()
    return res


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
    res = load_file(addr)

    while res.startswith('We') == 0:
        res = load_file(res)

    print(res)


if __name__ == "__main__":
    main()
