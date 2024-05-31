#!python3
# coding: utf-8
# https://leetcode.cn/problems/search-a-2d-matrix-ii/
#
# 思路：回溯。先往右走，走不动了就往下走，当往下走和往右走都碰壁时，从下一行开始重新向右走。
#   结束触发条件—— 1.走到最后一行，且这一行中没有此数；2.走完所有数字，没有此数
#
# 思路2：认真审题。因为此题只要返回是否有，而不是返回坐标，所以直接二分法遍历所有行。
#   优化条件 —— 本行最后一个元素小于target即跳过；2.本行开始元素大于target
#
# 边界条件：


def bi_search(li, target):
    """二分查找。输入参数li 要求升序排列"""
    n = len(li)
    start = 0
    end = n
    last_mid = -1
    while start < end:
        mid = int((start + end) / 2)
        if mid == last_mid:  # python总是向下取整，当有一个数字不在数组中且其值大小处于两连续元素中间时，会死循环。要靠这一句解锁
            break
        last_mid = mid

        if li[mid] < target:
            start = mid
        elif li[mid] > target:
            end = mid
        else:
            return True

    return False


def search_matrix(li: list, target: int):  # leetcode 时间164 ms 击败82.34% 内存21.2 MB 击败52.49%
    n = len(li)
    if n < 1:
        print("input error!")
        return False

    m = len(li[0])
    if m < 1:
        print("input error!")
        return False

    for i in range(n):
        if target > li[i][m - 1]:
            continue
        if target < li[i][0]:
            break
        if bi_search(li[i], target):
            return True
    return False


def test1():
    # li = [11, 12,19]
    # print(bi_search(li, 20))

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20
    print(search_matrix(matrix, target))


def test2():
    n = 1000
    matrix = [[y * n + x for x in range(n)] for y in range(n)]
    target = 89999
    # print(matrix[299][299])
    print(search_matrix(matrix, target))


def test3():
    matrix = [[]]
    target = 0
    # print(matrix[299][299])
    print(search_matrix(matrix, target))


def main():

    test2()


if __name__ == '__main__':
    from small_gram.date_op import start_time, end_time

    start_time()
    main()
    end_time()
