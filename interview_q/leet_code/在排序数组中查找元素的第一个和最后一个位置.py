# https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# coding: utf-8
# Python 3
# 如文件名所示，输入是升序数组，找不到就返回两个-1。没有描述只找到一次怎么返回，先按照返回俩一样的处理。
# 思路：设定两个指针，一个指针找第一个位置，一个指针找最后一个位置。
# 先找输入值，找得到再设定两个指针，然后二分查找第一个位置，再二分查找最后一个位置。
# 边界条件：空数组，由同一个元素若干次复制得到的数组


def average(a: int, b: int):
    return int((a+b)/2)


def find_index_by_half(li: list, key: int):
    """二分查找"""
    n = len(li)
    if n == 0:
        return [-1, -1]

    if key < li[0] or key > li[-1]:
        return [-1, -1]

    start = 0
    end = n-1
    mid = average(start, end)
    while start < end:
        if key > li[mid]:
            start = mid+1
            mid = average(mid, end)
        else:
            end = mid
            mid = average(mid, start)

    if key != li[start]:
        return [-1, -1]

    tmp = start
    if li[0] == key:
        first = 0
    else:
        start = 0
        end = tmp
        mid = average(start, end)
        while start <= end:
            if li[mid] != key and li[mid+1] == key:
                break
            if key > li[mid]:
                start = mid+1
                mid = average(mid, end)
            else:
                end = mid
                mid = average(mid, start)
        first = mid+1

    if li[-1] == key:
        last = n-1
    else:
        start = tmp
        end = n-1
        mid = average(start, end)
        while start <= end:
            if li[mid] == key and li[mid + 1] != key:
                break
            if key == li[mid]:
                start = mid+1
                mid = average(mid, end)
            else:
                end = mid
                mid = average(mid, start)
        last = mid

    return [first, last]


def main():
    li = [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5]
    print(find_index_by_half(li, 5))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
