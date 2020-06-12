# https://leetcode-cn.com/problems/spiral-matrix/
# coding: utf-8
# Python 3
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 思路：此题考察数组操作。顺时针遍历可以看成有个指针重复执行从左往右，从上往下，从右往左，从下往上的操作。
# 边界条件：


def ergodic_clockwise(li):
    m = len(li)-1
    if m < 0:
        return []
    n = len(li[0])
    size = (m+1)*n
    i = 0
    j = 0
    erl = []  # ergodic li
    while True:
        move(li, i, j, n, erl, "you")
        if bool_continue(erl, size) is True:
            break
        n -= 1
        j += n
        i += 1
        move(li, i, j, m, erl, "xia")
        if bool_continue(erl, size) is True:
            break
        m -= 1
        i += m
        j -= 1
        move(li, i, j, n, erl, "zuo")
        if bool_continue(erl, size) is True:
            break
        n -= 1
        j -= n
        i -= 1
        move(li, i, j, m, erl, "shang")
        if bool_continue(erl, size) is True:
            break
        m -= 1
        i -= m
        j += 1
    return erl


def you(li, i, j, n, erl):
    for k in range(n):
        erl.append(li[i][j+k])


def xia(li, i, j, n, erl):
    for k in range(n):
        erl.append(li[i+k][j])


def zuo(li, i, j, n, erl):
    for k in range(n):
        erl.append(li[i][j-k])


def shang(li, i, j, n, erl):
    for k in range(n):
        erl.append(li[i-k][j])


def move(li, i, j, n, erl, ins):
    if ins == "shang":
        shang(li, i, j, n, erl)
    elif ins == "xia":
        xia(li, i, j, n, erl)
    elif ins == "zuo":
        zuo(li, i, j, n, erl)
    else:
        you(li, i, j, n, erl)


def bool_continue(li, size):
    if len(li) != size:
        return False
    else:
        return True


def main():
    k = 5
    li = []
    tmp_li = []
    for i in range(k * k):
        if (i + 1) % k == 0:
            tmp_li.append(i)
            li.append(tmp_li)
            tmp_li = []
        else:
            tmp_li.append(i)
    li = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12]]
    # li = [[1]]
    print(ergodic_clockwise(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
