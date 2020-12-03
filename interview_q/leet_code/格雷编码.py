#! python3
# coding: utf-8
# https://leetcode-cn.com/problems/gray-code/
# 树的遍历，终止条件 —— 把格雷码都拿到（即达到指定长度）


def gray_code(n: int):
    if n == 0:
        return [0]
    init_li = [0 for _ in range(n)]
    gc_li = []
    ergodic_tree(n, gc_li, init_li)

    gc_li_str = []
    for i in gc_li:
        gc_li_str.append([str(x) for x in i])
    return [int("".join(x), 2) for x in gc_li_str]


def ergodic_tree(n, gray_code_li, tmp_li):
    """树的遍历"""
    if len(gray_code_li) == pow(2, n):
        return

    if tmp_li not in gray_code_li:
        gray_code_li.append(tmp_li)
        for i in range(n):
            ergodic_tree(n, gray_code_li, change_a_bit(tmp_li, i))


def change_a_bit(li, i):
    """按li 复制出一个新的数组，改变（翻转）指定位置的值"""
    new_li = [x for x in li]
    new_li[i] = 1-new_li[i]
    return new_li


def main():
    # print(int("111", 2))  # 二进制转十进制
    # print(change_a_bit([0, 1, 0, 1], 3))
    # print(change_a_bit([0, 1, 0, 1], 2))
    print(gray_code(4))


if __name__ == "__main__":
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
