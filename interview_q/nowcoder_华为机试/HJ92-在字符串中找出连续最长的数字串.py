# coding: utf-8
# Python 3
import sys


# 注意边界条件——只有字母的情况
def longest_num_substr(s: str, num_li: list):
    sub_li = []
    tmp_str = ''
    for i in range(len(s)):
        if s[i] in num_li:
            tmp_str += s[i]

            if i == len(s) - 1:
                sub_li.append(tmp_str)
        else:
            if tmp_str != "":
                sub_li.append(tmp_str)
                tmp_str = ''
    # print(sub_li)
    longest_length = 0
    if sub_li:
        longest_length = max([len(s) for s in sub_li])
    # print(longest_length)
    concat_str = ""
    for elem in sub_li:
        if len(elem) == longest_length:
            concat_str += elem
    print(f"{concat_str},{longest_length}")


def main():
    li = [str(x) for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]]
    for line in sys.stdin:
        longest_num_substr(line.strip(), li)


if __name__ == '__main__':
    main()
