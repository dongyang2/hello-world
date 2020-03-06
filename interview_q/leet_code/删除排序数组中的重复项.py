# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/
# coding: utf-8
# Python 3
# 在使用O(1)空间的情况下，删除有序数组的重复元素，然后返回处理后的数组长度。
# 思路：一个指针用于遍历，一个指针放在尾部元素上。
# 边界情况：空数组


def del_same_elem_simple(li: list):
    n = len(li)
    if n == 0:
        # raise ValueError('输入数组需要非空')
        return []

    i = 0
    while i < n-1:
        if li[i] == li[i+1]:
            li.pop(i+1)
            n -= 1
        else:
            i += 1
    return li


def main():
    li = [1, 2, 3, 3, 5, 6, 6]
    print(del_same_elem_simple(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
