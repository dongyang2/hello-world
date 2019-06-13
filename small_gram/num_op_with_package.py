# 调用第三方包实现的number operation
# Python 3
# coding: UTF-8

import numpy


def sort_by_col(arr, col=0):
    """

    :param arr: 待排序的数组
    :type  arr: numpy.array()
    :param col: 列号
    :return:    排序好的数组
    """
    sort_res = arr[arr[:, col].argsort()]
    return sort_res


if __name__ == '__main__':
    import time
    print('-'*15, 'Start', time.ctime(), '-'*15, '\n')

    li1 = [[1, 1], [2, 1], [4, 1], [0, 1]]
    a1 = numpy.array(li1)
    print(sort_by_col(a1))

    print('%s%s %s %s %s' % ('\n', '-'*16, 'End', time.ctime(), '-'*16))
