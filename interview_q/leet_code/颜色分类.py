# https://leetcode-cn.com/problems/sort-colors/
# coding: utf-8
# Python 3
# 给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。
# 此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。
#
# 思路：此题居然在描述下方把一种效率很高的原地修改思路给写出来了，那我这里就不重复了。直接按照要求，写出常数空间且只遍历一遍的方法。
# 拿时间换空间，只遍历一遍，维护一个字典，对每个元素进行计数，然后把它插入到计数位置所在地方。
# 这种方法也只有在你知道了输入数组中有哪几个数字的时候才有用。
# 进一步优化，可以把数组取消，变为三个指针，占用空间更小。
# 再进一步优化，只用两个指针记录两个数，对这两个数进行位置操作，另一个数自然是在正确排序的位置上。
# 边界条件：


def classify_colors(li):
    n = len(li)
    if n == 0 or n == 1:
        return

    dic = [0, 0, 0]
    for i in range(n):
        if li[i] == 0:
            insert_in_li(li, dic[0], i)
            dic[0] += 1
            dic[1] += 1
            dic[2] += 1
        elif li[i] == 1:
            insert_in_li(li, dic[1], i)
            dic[1] += 1
            dic[2] += 1
        else:
            insert_in_li(li, dic[2], i)
            dic[2] += 1


def insert_in_li(li: list, to: int, come: int):
    n = len(li)
    if to > n-1 or to < 0 or come > n-1 or come < 0:
        return li
    if to >= come:
        return li

    for i in range(to, come):
        li[i], li[come] = li[come], li[i]


def main():
    num = [1, 0]
    classify_colors(num)
    print(num)

    li = [2, 0, 2, 1, 1, 0]
    classify_colors(li)
    print(li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
