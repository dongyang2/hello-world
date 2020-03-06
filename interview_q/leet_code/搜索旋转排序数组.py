# hhttps://leetcode-cn.com/problems/search-in-rotated-sorted-array/
# coding: utf-8
# Python 3
# 对于一个经历了一次“旋转”的数组，找到一个数并返回该数的下标。此数组内无重复元素。要求时间复杂度为O(log n).
# “旋转”的数组表示，从一个点将数组截成两半，然后把前半部分拼接到后半部分。
# 如[1,2,3,4]可旋转为[3,4,1,2]，也可以旋转为[4,1,2,3]
#
# 思路：在纸上一画，把可能性分为四种情况，就可以转化为二分了。
# 边界情况： 空数组，只有一个元素的数组，只有两个元素的数组。输入数组不旋转的情况。（居然还有不旋转的情况，鄙视······）
#
# 上面思路是错的，现在更正一下。我一开始以为找到“切割点”或者“拼接点”需要遍历数组，这样就要O(n)的复杂度，
# 看了答案后才发现，可以二分查找最小的值······找到拼接点，再找输入值，就轻松多了。


def find_elem_by_half(li: list, key: int, start, end):
    """升序数组二分查找"""
    if key < li[start] or key > li[end]:
        return -1

    mid = average(start, end)
    while start < end:
        if key > li[mid]:
            start = mid+1
            mid = average(mid, end)
        else:
            end = mid
            mid = average(mid, start)

    if key == li[start]:
        return start
    else:
        return -1


def average(a: int, b: int):
    return int((a+b)/2)


def get_index(li, key):
    """给二分查找做一个外部“照顾”处理，对某些边界条件直接进行返回"""
    if len(li) == 0:
        return -1
    if len(li) == 1:
        if key == li[0]:
            return 0
        else:
            return -1

    start = 0
    end = len(li)-1

    if li[end] == key:
        return end
    if li[start] == key:
        return start

    if li[start] < li[end]:
        return find_elem_by_half(li, key, start, end)
    else:
        min_ind = find_min_by_half(li)
        if li[start] > key >li[end]:
            return -1
        elif key > li[start]:
            return find_elem_by_half(li, key, start, min_ind-1)
        else:
            return find_elem_by_half(li, key, min_ind, end)


def find_min_by_half(li):
    """用二分查找来寻找数组中的最小值"""
    start = 0
    end = len(li)-1
    mid = average(start, end)

    while start < end:
        if li[mid] > li[end]:
            start = mid + 1
            mid = average(mid, end)
        else:
            end = mid
            mid = average(mid, start)
    return start


def main():
    # li = [1, 2, 4, 5, 6, 7]
    # li = [1, 2]
    # print(find_elem_by_half(li, 7, 2, len(li)-1))

    # li = [4, 5, 6, 7, 0, 1, 2]
    # li = [1]
    # li = [3, 1]
    li = [4, 5, 6, 7, 8, 1, 2, 3]
    # print(find_min_by_half(li))

    # for i in li:
    #     print(whole(li, i))

    print(get_index(li, 9))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
