# https://leetcode-cn.com/problems/permutations/
# coding: utf-8
# Python 3
# 给定一个无重复元素的数组，求所有元素的排列可能。
# 虽然已经有过“全排列.py”文件了，但是突然发现leetcode上没有提交过，正好自己按照树的遍历再写一次。
#
# 思路：树的遍历。终止条件，待遍历的li长度为1.
# 边界条件：


def ergodic_tree(li: list, tmp_li: list, per_li: list):
    """树的遍历"""
    n = len(li)
    if n == 1:  # 终止条件，即碰到了叶节点
        tmp_li.append(li[0])
        per_li.append(tmp_li)
    else:
        for i in range(len(li)):
            ergodic_tree(pop_i(li, i), insert_in_end(tmp_li, li[i]), per_li)


def pop_i(li, ind):
    """按li复制出一个新的数组，按下标删除元素并返回"""
    new_li = []
    for i in range(len(li)):
        if i != ind:
            new_li.append(li[i])
    return new_li


def insert_in_end(li, val):
    """按li复制出一个新的数组，在尾部添加元素并返回"""
    new_li = [x for x in li]
    new_li.append(val)
    return new_li


def permutation(li):  # leetcode 48ms
    per_li = []
    ergodic_tree(li, [], per_li)
    return per_li


def main():
    li = [1, 2, 3, 4]
    print(permutation(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
