# https://leetcode-cn.com/problems/multiply-strings/
# coding: utf-8
# Python 3
# 如文件名。题目要求不能直接转化为整数进行计算。且数字长度不超过110位。
# 思路：应该是想考字符串的遍历。
# 边界条件：


def multiply(s1, s2):  # leetcode 248ms
    n1 = len(s1)
    n2 = len(s2)
    ans = 0
    for i in range(n1):
        tmp = 0
        for j in range(n2):
            tmp += multiply_char(s1[i], s2[j])*pow(10, n2-1-j)
        tmp *= pow(10, n1-1-i)
        ans += tmp
    return str(ans)


def multiply_char(c1, c2):
    """单个字符相乘"""
    return int(c1)*int(c2)


def main():
    s1 = "123"
    s2 = "456"
    print(multiply(s1, s2))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
