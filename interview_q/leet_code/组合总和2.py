# https://leetcode-cn.com/problems/combination-sum-ii/
# coding: utf-8
# Python 3
# 给定一个候选数组和一个目标数 target ，找出候选数组中所有加和为 target 的组合。
# 且candidates 中的每个数字只能被选取一次。相同数字不同下标仍然可以被选取。
#
# 思路：树的遍历。具体思路见“组合总数.py”文件。该文件中还给出了相关剪枝优化。
#
# 边界条件：


def all_possible_add(li: list, target, pos_li: list, tmp_li: list):
    he = sum(tmp_li)
    if he < target:
        n = len(li)
        for i in range(n):
            if li[i] + he <= target:
                all_possible_add(li[:i]+li[i+1:], target, pos_li, insert(tmp_li, li[i]))
    elif he == target:
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


def main():
    li = [2, 4, 1, 2, 5]
    pos_li = []
    all_possible_add(li, 4, pos_li, [])
    print(pos_li)

    li = [10, 1, 2, 7, 6, 1, 5]
    pos_li = []
    all_possible_add(li, 8, pos_li, [])
    print(pos_li)

    li = [2, 5, 2, 1, 2]
    pos_li = []
    all_possible_add(li, 5, pos_li, [])
    print(pos_li)

    li = []
    pos_li = []
    all_possible_add(li, 8, pos_li, [])
    print(pos_li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
