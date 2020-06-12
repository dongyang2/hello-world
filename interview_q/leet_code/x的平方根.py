# https://leetcode-cn.com/problems/sqrtx/
# coding: utf-8
# Python 3
# 如文件名。输入限定为非负整数。
#
# 思路：小学数学方法。二分查找。
# 边界条件：


def sqrt_x(x: int):
    if x == 1:
        return 1
    if x == 0:
        return 0

    start = 0.0
    end = x
    mid = (start+end)/2.0
    for _ in range(100):
        if mid*mid > x:
            end = mid
        elif mid*mid < x:
            start = mid
        else:
            break
        mid = (start + end) / 2.0

    return mid


def main():
    x = 2
    print(sqrt_x(x))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
