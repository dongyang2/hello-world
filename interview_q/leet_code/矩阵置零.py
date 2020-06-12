# https://leetcode-cn.com/problems/set-matrix-zeroes/
# coding: utf-8
# Python 3
# 给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。限定在原地操作。且尝试使用常数空间的方法。
#
# 思路：
# 边界条件：


def rc_zero(li):
    m = len(li)
    n = len(li[0])
    flag = []
    for i in range(m):
        if 0 in li[i]:
            for j in range(n):
                if li[i][j] == 0:
                    flag.append([i, j])
    for i in flag:
        row_zero(li, i[0])
        col_zero(li, i[1])


def row_zero(li, i):
    """把某行所有元素置零"""
    for j in range(len(li[0])):
        li[i][j] = 0


def col_zero(li, j):
    """把某列所有元素置零"""
    for i in range(len(li)):
        li[i][j] = 0


def main():
    li = [
      [1, 1, 1],
      [1, 0, 1],
      [1, 1, 1]
    ]
    rc_zero(li)
    print(li)

    li = [
        [0, 1, 2, 0],
        [3, 4, 5, 2],
        [1, 3, 1, 5]
    ]
    rc_zero(li)
    print(li)

    li = [[]]
    rc_zero(li)
    print(li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
