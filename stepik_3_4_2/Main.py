import struct


def read_file(name):
    f = open(name, "r")
    arr = f.read().split()
    f.close()
    return arr


def process_array(arr):

    dc = dict()
    for e in arr:
        if e.lower() in dc:
            dc[e.lower()] += 1
        else:
            dc[e.lower()] = 1
    mx = 0
    elem = ""
    for e in arr:
        if dc[e.lower()] > mx:
            mx = dc[e.lower()]
            elem = e
    print(elem + ' ' + str(mx))
    return str(elem + ' ' + str(mx))


def print_element(e):
    print(str(len))


def write_file(name, data):
    f = open("out", "w")
    f.write(data)
    f.close()


def main():
    write_file("out", process_array(read_file("file.txt")))


if __name__ == "__main__":
    main()
