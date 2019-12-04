import struct


def read_file(name):
    f = open(name, "r")
    dc = dict()
    for cnt, line in enumerate(f):
        l = line.strip().split(sep=';')
        dc[l[0]] = l[1:]
    f.close()
    return dc


def process_dict(dc):
    list_avg = list()
    sm_a = 0
    sm_b = 0
    sm_c = 0
    cnt = 0
    for cnt, name in enumerate(dc):
        sm = 0
        for nm, e in enumerate(dc[name]):
            sm += int(e)
            if nm == 0:
                sm_a += int(e)
            if nm == 1:
                sm_b += int(e)
            if nm == 2:
                sm_c += int(e)
        list_avg.append(float(sm / (nm + 1)))
    avg_a = float(sm_a / (cnt + 1))
    avg_b = float(sm_b / (cnt + 1))
    avg_c = float(sm_c / (cnt + 1))
    for e in list_avg:
        print(str(e))
    print(str(avg_a) + ' ' + str(avg_b) + ' ' + str(avg_c))



def print_element(e):
    print(str(len))


def write_file(name, data):
    f = open("out", "w")
    f.write(data)
    f.close()


def main():
    # write_file("out", process_dict(read_file("file.txt")))
    process_dict(read_file("file.txt"))

if __name__ == "__main__":
    main()
