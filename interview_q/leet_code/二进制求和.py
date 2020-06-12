# https://leetcode-cn.com/problems/add-binary/
# coding: utf-8
# Python 3
# 输入两个字符串形式的二进制数，输出相加的结果，依然是字符串。
# 输入限定为非负数，且首位不能为零（除了零本身）。
#
# 思路：和“加一.py”一样。
# 边界条件：


def add_str(s1: str, s2: str):
    n1 = len(s1)
    n2 = len(s2)
    if n1 == 0:
        return s2
    if n2 == 0:
        return s1
    li1 = list(s1)
    li2 = list(s2)
    if n1 > n2:
        li = [x for x in li1]
    else:
        li = [x for x in li2]
    i1 = n1-1
    i2 = n2-1
    k = len(li)-1
    jin_yi = False  # 进一
    while k >= 0:
        tmp1 = None
        if i1 >= 0 and i2 >= 0:
            li[k], tmp1 = add_char_by_binary(li1[i1], li2[i2])

        tmp2 = None
        if jin_yi is True:
            li[k], tmp2 = add_char_by_binary(li[k], "1")

        if tmp1 is True or tmp2 is True:
            jin_yi = True
        else:
            jin_yi = False

        k -= 1
        i1 -= 1
        i2 -= 1

    if jin_yi is True:
        return "".join(["1"]+li)
    else:
        return "".join(li)


def add_char_by_binary(c1, c2):
    if c1 == c2:
        if c1 == "1":
            return "0", True
        else:
            return "0", False
    else:
        return "1", False


def main():
    num1 = "1011"
    num2 = "1010"
    print(add_str(num1, num2))

    num1 = "101"
    num2 = "1"
    print(add_str(num1, num2))

    num1 = "101"
    num2 = "11"
    print(add_str(num1, num2))

    num1 = "0"
    num2 = "1"
    print(add_str(num1, num2))

    num1 = "1111"
    num2 = "1111"
    print(add_str(num1, num2))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
