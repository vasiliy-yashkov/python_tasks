def main():
    a = str(input())
    # sum = 0
    # for i in a:
    #     if i == 'C' or i == 'G':
    #         sum += 1
    # print((sum / len(a)) * 100)
    c = 0
    st = 0
    res = ''
    idx = 0
    for i in a:
        if st == 0:
            st += 1
            c += 1
            # res += i
        elif st <= len(a):
            ch = a[st - 1]
            if ch == i:
                c += 1
            else:
                res += a[idx]
                res += str(c)
                c = 1
                idx = st
            st += 1
    res += str(a[len(a) - 1])
    res += str(c)
    print(res)

    # students = ['Ivan', 'Masha', 'Sasha']
    # students += ['Olga']
    # students += 'Olga'
    #
    # print(len(students))
    #
    # a = [1, 2, 3]
    # b = a
    #
    # print(b)
    #
    # a[1] = 10
    # print(b)
    #
    # b[0] = 20
    # print(a)
    #
    # a = [5, 6]
    # print(b)

if __name__ == "__main__":
    main()
