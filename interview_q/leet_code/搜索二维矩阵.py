# https://leetcode-cn.com/problems/search-a-2d-matrix/submissions/
# coding: utf-8
# Python 3
# 编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：
# 每行中的整数从左到右按升序排列。
# 每行的第一个整数大于前一行的最后一个整数。
#
# 思路：其实这题有个技巧，是我好几个月之前在《剑指offer》书里看到的，就是从右上角或者左下角开始搜索，而不是直觉性地从左上角和右下角开始。
# 可以理解成从左上或者右下就直接相当于遍历数组了，而从右上或左下开始就是利用了数组的特性，进行了分治。
# 边界条件：空数组


def find_one(li, x):
    """在力扣上空间击败了100%的用户。见文件“搜索二维矩阵 力扣结果.jpg”"""
    m = len(li)
    if m == 0:
        return False
    n = len(li[0])
    if n == 0:
        return False
    i = 0
    j = n-1
    have_one = False
    while True:
        if li[i][j] == x:
            have_one = True
            break
        elif li[i][j] > x:
            if j == 0:
                break
            j -= 1
        else:
            if i == m-1:
                break
            i += 1
    # print(i, j)
    return have_one


def main():
    num = [
      [1,   3,  5,  7],
      [10, 11, 16, 20],
      [23, 30, 34, 50]
    ]
    x = 21
    print(find_one(num, x))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
