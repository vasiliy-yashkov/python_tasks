def main():
    a = int(input())
    b = int(input())

    r = range(a, b + 1)
    sum = 0
    col = 0
    for i in r:
        if i % 3 == 0:
            sum += i
            col += 1

    print(sum / col)


if __name__ == "__main__":
    main()
