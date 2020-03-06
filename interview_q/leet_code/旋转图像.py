# https://leetcode-cn.com/problems/rotate-image/
# coding: utf-8
# Python 3
# 顺时针旋转输入图像。要求在原输入数组上进行修改。
#
# 思路：既然是在原数组上进行修改，那么可以使用“大风车”法进行递归操作。不用函数递归也可以写成while形式。
# 边界条件：


def rotate(li: list, sls, sle):
    """

    :param li:      矩阵
    :param sls:     边长开始点
    :param sle:     边长结束点
    :return:
    """
    n = sle-sls
    floor = sls
    if n < 1:
        return
    else:
        tmp_li = []
        for i in range(sls+1, sle+1):
            tmp_li.append(li[floor][i])
            li[floor][i] = 0

        # 开~始~旋转!（脑补萨满232风怒机械）
        for i in range(n):
            tmp_li[i], li[floor+i+1][sle] = li[floor+i+1][sle], tmp_li[i]
        for i in range(n):
            tmp_li[i], li[sle][sle-i-1] = li[sle][sle-i-1], tmp_li[i]
        for i in range(n):
            tmp_li[i], li[sle-i-1][sls] = li[sle-i-1][sls], tmp_li[i]
        for i in range(n):
            tmp_li[i], li[sls][sls+i+1] = li[sls][sls+i+1], tmp_li[i]

        sls += 1
        sle -= 1
        rotate(li, sls, sle)


def lets_rotate(li):
    rotate(li, 0, len(li)-1)


def rotate_while_version(li):
    """上面的递归也可以写成while的形式"""
    sls = 0
    sle = len(li)-1
    n = sle - sls

    while n >= 1:
        tmp_li = []
        for i in range(sls+1, sle+1):
            tmp_li.append(li[sls][i])
            li[sls][i] = 0

        # 开~始~旋转!（脑补萨满232风怒机械）
        for i in range(n):
            tmp_li[i], li[sls+i+1][sle] = li[sls+i+1][sle], tmp_li[i]
        for i in range(n):
            tmp_li[i], li[sle][sle-i-1] = li[sle][sle-i-1], tmp_li[i]
        for i in range(n):
            tmp_li[i], li[sle-i-1][sls] = li[sle-i-1][sls], tmp_li[i]
        for i in range(n):
            tmp_li[i], li[sls][sls+i+1] = li[sls][sls+i+1], tmp_li[i]

        sls += 1
        sle -= 1
        n = sle - sls

    return li


def main():
    # li = [
    #     [1, 2, 3],
    #     [4, 5, 6],
    #     [7, 8, 9]
    # ]
    # lets_rotate(li)
    # print(li)

    k = 4
    li = []
    tmp_li = []
    for i in range(k*k):
        if (i+1) % k == 0:
            tmp_li.append(i)
            li.append(tmp_li)
            tmp_li = []
        else:
            tmp_li.append(i)
    # print(li)
    # lets_rotate(li)
    # print(li)
    print(rotate_while_version(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
