# coding: utf-8
# Python 3
#
#
# 描述
# 功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
#
#
# 数据范围 1≤n≤2×10^{9} + 14
#
# 输入描述：
# 输入一个整数
#
# 输出描述：
# 按照从小到大的顺序输出它的所有质数的因子，以空格隔开。
#
# 思路：从2开始整除“输入”，一步步拆解“输入”。 技巧，遍历是否为质数时，不遍历2~n-1，而是遍历 2~ int(根号n)+1

import sys
import math


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True


def prime_elem(line: str):  # 运行时间   占用内存
    inp_num = int(line)
    li = []
    if inp_num < 2:
        return li

    prime_li = []  # 存质数，避免重复计算
    i = 2
    while inp_num != 1:
        if is_prime(inp_num):
            li.append(str(inp_num))
            break
        if inp_num % i == 0:
            if i in prime_li:
                inp_num = int(inp_num / i)
                li.append(str(i))
            else:
                if is_prime(i):
                    inp_num = int(inp_num / i)
                    li.append(str(i))
                    prime_li.append(i)
                else:
                    print(f"no way {i}, inp_num {inp_num}")
                    i += 1
        else:
            i += 1
    return li


def main():
    from small_gram.date_op import start_time, end_time

    line = input()

    start_time()
    print(is_prime(int(line)))
    print(" ".join(prime_elem(line)))
    end_time()


if __name__ == '__main__':
    main()
