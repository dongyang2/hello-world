# https://leetcode-cn.com/problems/count-and-say/
# coding: utf-8
# Python 3
# 从1开始，把字符串念出来。
# 1 被读作  "one 1"  ("一个一") , 即 11。
# 11 被读作 "two 1s" ("两个一"）, 即 21。
# 21 被读作 "one 2",  "one 1" （"一个二" ,  "一个一") , 即 1211。
# 所以此数列前四个数字是[ "1", "11", "21", "1211"]
#
# 思路：一个普通的迭代
# 边界条件：


def outlook_sequence(i: int):
    if i == 1:
        return "1"

    init_s = "1"
    target_s = ""
    while i > 1:
        target_s = ""
        tmp_s = init_s[0]
        count = 0
        for j in init_s:
            if tmp_s == j:
                count += 1
            else:
                target_s += str(count)+tmp_s
                count = 1
                tmp_s = j
        target_s += str(count)+tmp_s
        init_s = target_s
        i -= 1
    return target_s


def main():
    print(outlook_sequence(6))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
