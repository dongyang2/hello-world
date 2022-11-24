# coding: utf-8
# Python 3
#
#
# 描述
# 写出一个程序，接受一个由字母、数字和空格组成的字符串，和一个字符，然后输出输入字符串中该字符的出现次数。（不区分大小写字母）
# 数据范围： 1≤n≤1000
# 输入描述：
# 第一行输入一个由字母和数字以及空格组成的字符串，第二行输入一个字符。
#
# 输出描述：
# 输出输入字符串中含有该字符的个数。（不区分大小写字母）
#
#
# 思路：
#
#
# 边界条件：注意第一行的结尾有可能是空格
#


def show_frequency(line: str, lin2: str):  # 运行时间44ms 占用内存4540KB
    s1 = line.lower()
    s2 = lin2.lower()
    print(s1.count(s2))


def main():
    from small_gram.date_op import start_time, end_time

    start_time()
    line1 = input()
    line2 = input()

    show_frequency(line1, line2)
    end_time()


if __name__ == '__main__':
    main()
