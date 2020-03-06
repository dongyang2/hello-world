# https://leetcode-cn.com/problems/remove-element/
# coding: utf-8
# Python 3
# 在使用O(1)空间的情况下，删除数组中与指定的元素相等的元素，然后返回处理后的数组长度。
# 思路：同“删除排序数组中的重复项”
# 边界情况：


def del_elem_simple(li: list, x: int):
    n = len(li)
    if n == 0:
        # raise ValueError('输入数组需要非空')
        return []

    i = 0
    while i < n:
        if li[i] == x:
            li.pop(i)
            n -= 1
        else:
            i += 1
    return li


def main():
    li = [1, 2, 3, 0, 5, 0, 6]
    print(del_elem_simple(li, 0))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
