# https://leetcode-cn.com/problems/search-insert-position/
# coding: utf-8
# Python 3
# 给定一个升序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它应该被插入的位置。
# 数组中元素各不相同。
# 思路：
# 边界条件：


def average(a: int, b: int):
    return int((a+b)/2)


def search_or_insert(li, key):
    n = len(li)
    if n == 0:
        return 0

    if key < li[0]:
        return 0

    if key > li[-1]:
        return n

    start = 0
    end = n - 1
    mid = average(start, end)
    while start < end:
        if key > li[mid]:
            start = mid + 1
            mid = average(mid, end)
        else:
            end = mid
            mid = average(mid, start)

    return start


def main():
    li = [1, 2, 4, 5]
    print(search_or_insert(li, 4))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
