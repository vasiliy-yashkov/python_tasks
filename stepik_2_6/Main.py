from array import *
import copy


def main():
    # s = list()
    # s.append(int(input()))
    # setsum = s[0]
    # while setsum != 0:
    #     a = int(input())
    #     s.append(a)
    #     setsum += a
    #
    # setsqsum = 0
    # for i in s:
    #     setsqsum += pow(i, 2)
    #
    # print(setsqsum)
    """
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """
    # n = int(input())
    #
    # i = 0
    # s = list()
    # while len(s) < n:
    #     j = 0
    #     while j < i + 1:
    #         s.append(i + 1)
    #         if len(s) >= n:
    #             break
    #         j += 1
    #     if len(s) >= n:
    #         break
    #     i += 1
    #
    # print(' '.join(str(x) for x in s))
    """
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """
    # s = [int(n) for n in input().split(sep=' ')]
    # x = int(input())
    # positions = list()
    # idx = 0
    # for i in s:
    #     if (x == i):
    #         positions.append(idx)
    #     idx += 1
    #
    # if (len(positions) == 0):
    #     print("Отсутствует")
    # else:
    #     print(' '.join(str(x) for x in positions))
    """
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """
    # a = list(list())
    #
    # st = input()
    # while st.lower() != "end":
    #
    #     s = [int(n) for n in st.split(sep=' ')]
    #     a.append(s)
    #     st = input()
    #
    # for i, k in enumerate(a):
    #     j = 0
    #     for l in k:
    #         idx1 = i - 1
    #         idx2 = i + 1
    #         idx3 = j - 1
    #         idx4 = j + 1
    #
    #         if idx1 < 0:
    #             idx1 = len(a) - 1
    #         if idx2 == len(a):
    #             idx2 = 0
    #         if idx3 < 0:
    #             idx3 = len(k) - 1
    #         if idx4 == len(k):
    #             idx4 = 0
    #
    #         sm = a[idx1][j] + a[idx2][j] + a[i][idx3] + a[i][idx4]
    #
    #         print(sm, end=' ')
    #         j += 1
    #     print('')
    #     i += 1

    """
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    """

    n = int(input())
    if n == 1:
        print(1)
        return
    print_matrix(spiral(n, n))


NORTH, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)  # directions
turn_right = {NORTH: E, E: S, S: W, W: NORTH}  # old -> new direction


def spiral(width, height):
    x, y = 0, 0
    dx, dy = NORTH  # initial direction
    matrix = [[None] * width for _ in range(height)]
    count = 0
    while True:
        count += 1
        matrix[y][x] = count

        if (0 <= x + dx < width and 0 <= y + dy < height and
                matrix[y + dy][x + dx] is None):  # can move straight
            x, y = x + dx, y + dy
            if not (0 <= x < width and 0 <= y < height):
                return matrix

        else:

            # try to turn right
            new_dx, new_dy = turn_right[dx, dy]
            new_x, new_y = x + new_dx, y + new_dy
            if matrix[new_y][new_x] is not None:
                return matrix
            x, y = new_x, new_y
            dx, dy = new_dx, new_dy


def print_matrix(matrix):
    width = len(str(max(el for row in matrix for el in row if el is not None)))
    fmt = width
    for row in matrix:
        print(" ".join("_" * width if el is None else str(el) for el in row))


if __name__ == "__main__":
    main()
