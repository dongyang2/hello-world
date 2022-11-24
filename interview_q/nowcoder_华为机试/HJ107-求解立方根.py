# coding: utf-8
# Python 3


def format(num: float):
    s = str(num)
    tenger, dig = s.split(".")
    return float(tenger + "." + dig[:2])


def round(num: float):
    s = str(num)
    tenger, dig = s.split(".")
    if len(dig) < 2:
        return num
    if dig[1] < '5':
        return float(tenger + "." + dig[:1])
    else:
        return float(tenger + "." + str(int(dig[0]) + 1))


def cube_root(num: float):
    if num < 0:
        digit_init = -2.9
    else:
        digit_init = 2.9
    b = 0.0
    mid = 0.0
    last_one = None
    while abs(b - digit_init) > 0.01:
        mid = format((digit_init + b) / 2)
        if last_one == mid:
            break
        tmp = mid * mid * mid
        last_one = mid
        if abs(tmp) < abs(num):
            b = mid
        elif abs(tmp) > abs(num):
            digit_init = mid
        else:
            break
    print(round(mid))


def main():
    n = input()
    cube_root(float(n))


if __name__ == '__main__':
    main()
