# https://leetcode-cn.com/problems/implement-strstr/
# coding: utf-8
# Python 3
# 在不用乘法、除法和 mod 运算符的情况下，计算两数相除。被除数绝对值小于除数时题中未给出说明。
# 思路：类似于“pow_x”。
# 边界情况：限定了输出数字大小，为[−2^31,  2^31 − 1]。超出范围返回2^31-1。


def divide_imitate(a: int, b: int):
    if b == 0:
        raise ValueError('除数不能为零')

    if a > 0 and b > 0 or a < 0 and b < 0:
        flag = False
    else:
        flag = True

    a = absolute(a)
    b = absolute(b)
    if flag is True:
        c = -recursive(a, b)
    else:
        c = recursive(a, b)

    if c < -2147483648 or c > 2147483647:
        # raise ValueError('超出整形范围')
        return 2147483647

    return c


def absolute(x: int):
    if x > 0:
        return x
    else:
        return -x


def recursive(a, b):
    if a < b:
        return 0

    i = 1
    multi = b
    while (multi+multi) < a:
        multi += multi
        i += i

    return i + recursive(a-multi, b)


def main():
    a = -2147483648
    b = -1
    print(divide_imitate(a, b))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
