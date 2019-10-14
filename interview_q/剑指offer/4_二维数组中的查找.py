# coding: utf-8
# Python 3
# 在二维数组中找一个数，这个二维数组设定是从左到右递增，且从上到下递增。


def bool_find(li, num):
    """关键是从右上角或者左下角开始"""
    n = len(li)
    if n <= 0:
        raise ValueError("输入数组 {}需要非空".format(li))
    try:
        m = len(li[0])
        if m == 0:
            raise ValueError("输入数组 {}需要是二维的".format(li))
    except TypeError:
        raise ValueError("输入数组 {}需要是二维的".format(li))

    found = False
    i = 0
    j = m - 1
    while i < n and j >= 0:
        if li[i][j] == num:
            found = True
            break
        elif li[i][j] > num:
            j -= 1
        else:
            i += 1
    return found


def main():
    li = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    print(bool_find(li, 3))
    # print(len(li[0]))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
