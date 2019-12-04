def read_file(name):
    f = open(name, "r")
    s = f.read()
    f.close()
    return s


def process_line(line):
    res = ""
    tmp_str_d = ""
    sym = ""
    prev_sym = ""
    dig_ready = False
    first = True
    for e in line:
        if e.isdigit():
            tmp_str_d += e
        else:
            prev_sym = sym
            sym = e
            if not first:
                dig_ready = True
            first = False
        if dig_ready:

            i = 0
            tmp_d = int(tmp_str_d)
            while i < tmp_d:
                res += prev_sym
                i += 1
            tmp_str_d = ""
            dig_ready = False
    i = 0
    tmp_d = int(tmp_str_d)
    while i < tmp_d:
        res += sym
        i += 1
    return res


def print_dict(m):
    for el in m:
        print(str(m[el]))


def write_file(name, data):
    f = open("out", "w")
    f.write(data)
    f.close()


def main():
    write_file("out", process_line(read_file("file.txt")))


if __name__ == "__main__":
    main()
