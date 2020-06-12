# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array-ii/
# coding: utf-8
# Python 3
# 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
#
#
# 思路：用常数空间做这个题，我只想到对每个数字进行计数，当数字发生变化时，计数清零。
# 边界条件：


def clear_li(li):
    n = len(li)
    if n < 2:
        return li
    i = 0
    count = 0
    tmp = li[0]
    while True:
        n = len(li)
        if i == n:
            break
        if li[i] == tmp:
            count += 1
            if count > 2:
                li.pop(i)
            else:
                i += 1
        else:
            tmp = li[i]
            count = 1
            i += 1


def main():
    li = [1, 1, 1, 2, 2, 3]
    clear_li(li)
    print(li)

    li = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    clear_li(li)
    print(li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
