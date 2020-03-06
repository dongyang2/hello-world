# https://leetcode-cn.com/problems/permutations-ii/
# coding: utf-8
# Python 3
# 给定一个可能有重复元素的数组，求所有元素的排列可能。
#
# 思路：树的遍历。修改自文件“全排列_自己写.py"文件。
# 相较于上个文件，此文件先对给定输入数组排序，然后在遍历结点时，跳过了重复元素。不然也可以开辟一个空间看这个结点的值是否遍历过。
# 边界条件：


def ergodic_tree_skip_in_sorted_li(li: list, tmp_li: list, per_li: list):
    """树的遍历。对排序的li跳过重复元素法。力扣 44ms"""
    n = len(li)
    if n == 1:  # 终止条件，即碰到了叶节点
        tmp_li.append(li[0])
        per_li.append(tmp_li)
    else:
        tmp = li[0]
        for i in range(len(li)):
            if i == 0:
                ergodic_tree_skip_in_sorted_li(pop_i(li, i), insert_in_end(tmp_li, li[i]), per_li)
            elif li[i] != tmp:
                ergodic_tree_skip_in_sorted_li(pop_i(li, i), insert_in_end(tmp_li, li[i]), per_li)
                tmp = li[i]


def ergodic_tree_skip_same_elem(li: list, tmp_li: list, per_li: list):
    """树的遍历。开辟记录数组空间跳过重复元素法。力扣 44ms"""
    n = len(li)
    if n == 1:  # 终止条件，即碰到了叶节点
        tmp_li.append(li[0])
        per_li.append(tmp_li)
    else:
        no_same_elem_li = []
        for i in range(len(li)):
            if li[i] not in no_same_elem_li:
                ergodic_tree_skip_same_elem(pop_i(li, i), insert_in_end(tmp_li, li[i]), per_li)
                no_same_elem_li.append(li[i])


def pop_i(li, ind):
    """复制出一个新的数组，按下标删除元素并返回"""
    new_li = []
    for i in range(len(li)):
        if i != ind:
            new_li.append(li[i])
    return new_li


def insert_in_end(li, val):
    """复制出一个新的数组，在尾部添加元素并返回"""
    new_li = [x for x in li]
    new_li.append(val)
    return new_li


def permutation(li):
    per_li = []
    # # 下面两种方法时间在力扣上差不多，说明输入数组比较短
    # ergodic_tree_skip_in_sorted_li(sorted(li), [], per_li)
    ergodic_tree_skip_same_elem(li, [], per_li)
    return per_li


def main():
    li = [1, 1, 3, 2]
    print(permutation(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
