def diving(__x, __y):
    return __x % __y == 0


def is_chet(__x):
    return diving(__x, 2)


def check(x1, y1, x2, y2):
    input1 = x2 - x1
    input2 = y2 - y1
    ci1 = is_chet(input1)
    ci2 = is_chet(input2)
    xx = ci2 and ci1
    xxi = (not ci2) and (not ci1)
    return xx or xxi


def main():
    x1 = int(input())
    y1 = int(input())
    x2 = int(input())
    y2 = int(input())
    print(check(x1, y1, x2, y2) * "YES",
          (not check(x1, y1, x2, y2)) * "NO", sep="", end="")


if __name__ == '__main__':
    main()
