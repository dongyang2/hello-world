# coding: utf-8
# Python 3
#
#
# 描述
# 给定 n 个字符串，请对 n 个字符串按照字典序排列。
#
# 数据范围： 1≤n≤1000  ，字符串长度满足  1≤len≤100
# 输入描述：
# 输入第一行为一个正整数n(1≤n≤1000),下面n行为n个字符串(字符串长度≤100),字符串中只含有大小写字母。
# 输出描述：
# 数据输出n行，输出结果为按照字典序排列的字符串。
#
# 思路：


def sort_str_li(li: list):  # 运行时间 109ms 占用内存 4880KB
    """冒泡排序"""
    n = len(li)
    for i in range(n):
        for j in range(i+1, n):
            if li[i] > li[j]:
                li[i], li[j] = li[j], li[i]

    return li


def main():
    from small_gram.date_op import start_time, end_time

    n = input()
    inp_li = []
    for i in range(int(n)):
        inp_li.append(input())

    start_time()
    for i in sort_str_li(inp_li):
        print(i)
    end_time()


if __name__ == '__main__':
    main()
