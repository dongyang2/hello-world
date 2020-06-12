# https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/
# coding: utf-8
# Python 3
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
# 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
#
# 思路：先找到最小数，然后使用正常的搜索。
# 边界条件：其实题目已经写了一个边界条件，最小数有很多个怎么办？


def find_one(li: list, target: int):
    n = len(li)
    if n < 1:
        return False
    min_one = find_min(li)
    if target < li[min_one]:
        return False
    if min_one != 0:
        if target > li[min_one-1]:
            return False

    if half_search(li, min_one, n-1, target) is True:
        return True
    else:
        if min_one == 0:
            return False
        return half_search(li, 0, min_one-1, target)


def half_search(li, start, end, target):
    while start != end:
        mid = int((start + end) / 2)
        if target == li[mid]:
            return True
        elif target > li[mid]:
            start = mid+1
        else:
            end = mid
    if li[end] == target:
        return True
    return False


def find_min(li):
    tmp = 0
    for i in range(len(li)):
        if li[i] <= li[tmp]:
            tmp = i
    min_tmp = tmp
    for i in range(tmp):
        if li[tmp-1-i] == li[min_tmp]:
            min_tmp = tmp-1-i
        else:
            break
    return min_tmp


def find_min_by_half(li):
    """用二分查找来寻找数组中的最小值"""
    start = 0
    end = len(li)-1

    while start < end:
        mid = int((start + end) / 2)
        if li[mid] > li[end]:
            start = mid + 1
        else:
            end = mid
    return start


def main():
    # li = [2, 5, 6, 0, 0, 1, 2, 2, 2, 2, 2]
    # print(find_min(li))
    # print(find_one(li, 0))
    # print(find_one(li, 4))

    # li = [1]
    # print(find_one(li, 2))

    # li = [3,1,1]
    # print(find_one(li, 1))

    li = [2, 2, 2, 0, 2]
    print("最小数字的下标 ", find_min_by_half(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
