# https://leetcode-cn.com/problems/plus-one/
# coding: utf-8
# Python 3
# 输入是数组形式的数字，如[1,2,3]表示123，[9,5,8]表示958.输出这个数字加一后的结果。如输入[1,2,3]输出[1,2,4]，输入[9,5,8]输出[9,5,9]。
# 输入限定为非负数，且首位不能为零（除了零本身）。
#
# 思路：没啥思路，感觉就是对[9,9,9]这样的数字进行处理即可。
# 边界条件：


def add_1(li):
    n = len(li)
    if n < 1:
        return li

    if li[-1] != 9:
        li[-1] += 1
        return li
    else:
        i = n-1
        bool_break = False
        while i >= 0:
            if li[i] == 9:
                li[i] = 0
            else:
                li[i] += 1
                bool_break = True
                break
            i -= 1
        if bool_break is True:
            return li
        else:
            return [1] + li


def main():
    num = [8, 9]
    print(add_1(num))

    num = [9, 9]
    print(add_1(num))

    num = [8, 8]
    print(add_1(num))

    num = [0]
    print(add_1(num))

    num = []
    print(add_1(num))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
