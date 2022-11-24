# coding: utf-8
# Python 3
#
#
# 思路：
#
#
# 边界条件：
#

import sys


def len_of_last_word(line: str):  # 运行时间53ms 占用内存4592KB
    li = line.split(" ")
    print(len(li[-1]))


def main():
    from small_gram.date_op import start_time, end_time

    start_time()
    for line in sys.stdin:
        len_of_last_word(line.strip())
    end_time()


if __name__ == '__main__':

    main()
