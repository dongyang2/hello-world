# coding: utf-8
# Python 3
#
#
# 描述
# 写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。
#
# 数据范围：保证结果在 1≤n≤2^{31}-1
#
# 输入描述：
# 输入一个十六进制的数值字符串。
#
# 输出描述：
# 输出该数值的十进制字符串。不同组的测试用例用\n隔开。
#
#
# 思路：
#
#
# 边界条件：

import sys


def mapper(s: str):
    """将16进制的数字对应到10进制"""
    if s.lower() == "a":
        return 10
    elif s.lower() == "b":
        return 11
    elif s.lower() == "c":
        return 12
    elif s.lower() == "d":
        return 13
    elif s.lower() == "e":
        return 14
    elif s.lower() == "f":
        return 15
    else:
        return int(s)


def trans(line: str):  # 运行时间 44ms 占用内存 4648KB
    if line.startswith("0x") or line.startswith("0X"):
        line = line[2:]
    n = 0
    num = 0
    while n < len(line):
        num += mapper(line[n]) * pow(16, len(line)-n-1)
        n += 1
    print(num)


def trans_py(line: str):  #
    print(int(line, 16))


def main():
    from small_gram.date_op import start_time, end_time

    start_time()
    for line1 in sys.stdin:
        trans_py(line1.strip())
        trans(line1.strip())
    end_time()


if __name__ == '__main__':
    main()
