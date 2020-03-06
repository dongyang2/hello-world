# https://leetcode-cn.com/problems/combination-sum/
# coding: utf-8
# Python 3
# 给定一个无重复元素的候选数组和一个目标数 target ，找出候选数组中所有加和为 target 的组合。
# 且candidates 中的数字可以无限制重复被选取。
#
# 思路：树的遍历。因为候选列表中的元素可以被无限次重复选择，所以树深为无限，需设立终止条件。
# 终止条件1是找到了，终止条件2是当前和值比target大。
#
# 边界条件：


def all_possible_add(li: list, target, pos_li: list, tmp_li: list):
    he = sum(tmp_li)
    if he < target:
        for i in li:
            if i + he <= target:  # 简单的剪枝
                all_possible_add(li, target, pos_li, insert(tmp_li, i))
    elif he == target:
        # copy_tmp = [x for x in tmp_li]
        if tmp_li not in pos_li:
            pos_li.append(tmp_li)


def insert(li: list, key: int):
    """此函数有两个功能，
    第一个功能显而易见就是为了把数字按照升序插到它该在的地方，
    第二个功能就是创建了新空间，这样就能保证在同一层的子节点只放入tmp_li一次。"""

    n = len(li)
    new_li = []
    bool_insert = False
    for i in range(n):
        if li[i] < key:
            new_li.append(li[i])
        else:
            if bool_insert is False:
                new_li.append(key)
                bool_insert = True
            new_li.append(li[i])

    if bool_insert is False:  # li中所有元素都比key小
        new_li.append(key)

    return new_li


def all_possible_add_in_sorted_li(li, target):
    """针对上面的递归遍历，进行进一步的剪枝。
    此方法在leetcode上面测试，为224ms，起初级剪枝是628ms，不剪枝是2564ms。"""
    li = sorted(li)
    pos_li = []
    ergodic_tree(li, target, pos_li, [], None)
    return pos_li


def ergodic_tree(li, target, pos_li, tmp_li, last_one):
    """li要求必须是升序的"""
    he = sum(tmp_li)
    if he < target:
        for i in li:
            if last_one is None:
                ergodic_tree(li, target, pos_li, insert(tmp_li, i), i)
            elif i >= last_one:  # 这种剪枝方法能够剪掉所有之前遍历过的路径
                ergodic_tree(li, target, pos_li, insert(tmp_li, i), i)
    elif he == target:
        # copy_tmp = [x for x in tmp_li]
        if tmp_li not in pos_li:
            pos_li.append(tmp_li)


def main():
    li = [1, 2, 4, 5]
    # li = [2]
    # print(insert(li, 5))

    # pos_li = []
    # all_possible_add(li, 4, pos_li, [])
    # print(pos_li)
    print(all_possible_add_in_sorted_li(li, 4))

    li = [2, 3, 6, 7]
    # pos_li = []
    # all_possible_add(li, 7, pos_li, [])
    # print(pos_li)
    print(all_possible_add_in_sorted_li(li, 7))

    li = [2, 3, 5]
    # pos_li = []
    # all_possible_add(li, 8, pos_li, [])
    # print(pos_li)
    print(all_possible_add_in_sorted_li(li, 8))

    li = []
    # pos_li = []
    # all_possible_add(li, 8, pos_li, [])
    # print(pos_li)
    print(all_possible_add_in_sorted_li(li, 2))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
