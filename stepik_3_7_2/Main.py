import sys


def main(argv=sys.argv):
    s1 = [char for char in input()]
    s2 = [char for char in input()]
    en_dc = dict(zip(s1, s2))
    dec_dc = dict(zip(s2, s1))

    for_encoding = str(input())
    for_decoding = str(input())

    res_en = ""
    res_dec = ""
    for e in for_encoding:
        res_en += en_dc[e]
    for e in for_decoding:
        res_dec += dec_dc[e]
    print(res_en)
    print(res_dec)

if __name__ == "__main__":
    main()
