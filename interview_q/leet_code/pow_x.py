# https://leetcode-cn.com/problems/powx-n/
# coding:utf-8
# Python 3
# 应该就是快速幂算法


def quick_pow(x, n):
    """我的想法就是把n次乘法换成log(2,n)次乘法"""
    if n == 0:
        return 1
    if n == 1:
        return x
    tmp_n = 1
    tmp_x = x
    while True:
        tmp_n *= 2
        if tmp_n > n:
            tmp_n /= 2
            break
        tmp_x *= tmp_x

    if n - tmp_n == 0:
        return tmp_x
    else:
        return quick_pow(x, n - tmp_n) * tmp_x


def qpow_x(x, n):
    if n >= 0:
        return quick_pow(x, n)
    else:
        return 1 / quick_pow(x, -n)


def main():
    n = 15
    x = 2

    # print(quick_pow(x, n))
    print(qpow_x(2, -2))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
