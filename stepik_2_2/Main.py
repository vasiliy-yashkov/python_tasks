def main():
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())

    # while a <= b:
    #     if c != d:
    #         print("\t" + str(c) + "\t" + str(d))
    #     else:
    #         print("\t" + str(c))
    #
    #     a += 1


    cd = range(c, d + 1)

    print('', end='\t')
    for i in cd:
        print(i, end='\t')

    print('\t')

    ab = range(a, b + 1)
    for i in ab:
        print(i, end='\t')

        for j in cd:
            print(i * j, end='\t')
        print('', end='\n')



if __name__ == "__main__":
    main()
