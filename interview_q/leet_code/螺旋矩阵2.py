# https://leetcode-cn.com/problems/spiral-matrix-ii/
# coding: utf-8
# Python 3
# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
#
# 思路：此题比起“螺旋矩阵.py”文件，变简单了，因为螺旋矩阵不保证是正方形，所以这题的情况只是上题的特殊情况。
# 那么，使用上题的代码，改一改，得到可以制作螺旋长方形的代码。
# 边界条件：

def write_clockwise(n, m):
    """n是横轴，m是纵轴"""
    if n < 1 or m < 1:
        return []

    size = m*n+1  # 这里加一是因为每次执行“上下左右”中的一步后，count会等于下一个将要填进li的数字，所以当count==n*m+1时才应该结束循环

    li = []
    for _ in range(m):
        li.append([0 for _ in range(n)])

    m = m-1
    i = 0
    j = 0
    li[i][j] = 1
    count = 1

    while True:
        count = move(li, i, j, n, count, "you")
        if count == size:
            break
        n -= 1
        j += n
        i += 1
        count = move(li, i, j, m, count, "xia")
        if count == size:
            break
        m -= 1
        i += m
        j -= 1
        count = move(li, i, j, n, count, "zuo")
        if count == size:
            break
        n -= 1
        j -= n
        i -= 1
        count = move(li, i, j, m, count, "shang")
        if count == size:
            break
        m -= 1
        i -= m
        j += 1
    return li


def you(li, i, j, n, erl):
    for k in range(n):
        li[i][j+k] = erl
        erl += 1
    return erl


def xia(li, i, j, n, erl):
    for k in range(n):
        li[i+k][j] = erl
        erl += 1
    return erl


def zuo(li, i, j, n, erl):
    for k in range(n):
        li[i][j-k] = erl
        erl += 1
    return erl


def shang(li, i, j, n, erl):
    for k in range(n):
        li[i-k][j] = erl
        erl += 1
    return erl


def move(li, i, j, n, count, ins):
    if ins == "shang":
        return shang(li, i, j, n, count)
    elif ins == "xia":
        return xia(li, i, j, n, count)
    elif ins == "zuo":
        return zuo(li, i, j, n, count)
    else:
        return you(li, i, j, n, count)


def see_see(li):
    for i in li:
        print(i)


def main():
    # k = 5
    # print(write_clockwise(k, k))
    # see_see(write_clockwise(1, 1))
    see_see(write_clockwise(3, 4))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
