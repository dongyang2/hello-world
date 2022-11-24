# coding: utf-8
# Python 3
#
#
# 描述
# •输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；
#
# •长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
# 输入描述：
# 连续输入字符串(每个字符串长度小于等于100)
#
# 输出描述：
# 依次输出所有分割后的长度为8的新字符串
#
#
# 思路：
#
#
# 边界条件：字符串长度刚好是8的整数
#

import sys


def split_via_8(line: str):  # 运行时间 54ms 占用内存 4696KB
    if len(line) < 1:
        return
    n = int(len(line) / 8) if len(line) % 8 == 0 else int(len(line) / 8) + 1

    for i in range(n):
        tmp_s = line[i * 8:(i + 1) * 8]
        while len(tmp_s) < 8:
            tmp_s += "0"
        print(tmp_s)


def main():
    from small_gram.date_op import start_time, end_time

    start_time()
    for line1 in sys.stdin:
        split_via_8(line1.strip())
    end_time()


if __name__ == '__main__':
    main()
