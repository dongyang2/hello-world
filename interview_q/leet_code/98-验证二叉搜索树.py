# coding: utf-8
# https://leetcode.cn/problems/validate-binary-search-tree/description/
# Python 3
#
#
# 思路：二叉树的中序遍历。注意考虑节点相等的情况
#
#
# 边界条件：单个节点
# 备注：

from interview_q.algorithm.data_structure_leet_code import TreeNode


# # 这个思路不行，l1和l2不是Python容器，无法在函数内修改值
# def ergodic_tree_mid(node: TreeNode, l1, l2, flag):
#     """遍历树(中序)"""
#     if node.left is not None:
#         ergodic_tree_mid(node.left, l1, l2, flag)
#
#     if l1 is None:
#         l1 = node.val
#     else:
#         if l2 is None:
#             l2 = node.val
#         else:  # l1和l2都已存值
#             if l1 > l2:
#                 flag.append(True)  # 为True，不是二叉搜索树
#             l1 = l2
#             l2 = node.val
#
#     if node.left is None and node.right is None:
#         return
#
#     if node.right is not None:
#         ergodic_tree_mid(node.right, l1, l2, flag)


def li2str(li: list):
    return ",".join([str(x) for x in li])


def make_2_li(li: list, ind: int):
    """按li复制出2个新的数组，分别返回左边和右边序列"""
    left_li = li[0:ind]
    right_li = li[ind + 1:]
    return left_li, right_li


def child_tree_dp(start_li: list, dic: dict):
    """根据节点数构造二叉搜索树"""
    if not start_li:
        return [None]

    if len(start_li) == 1:
        return [TreeNode(start_li[0])]

    key = li2str(start_li)
    if key in dic:
        return dic[key]

    li = []
    for i in range(len(start_li)):
        left_li, right_li = make_2_li(start_li, i)  # 这里合理利用了二叉搜索树的性质
        # 遍历所有构造好的子树，插到新创建的根节点里面
        for l_kid in child_tree_dp(left_li, dic):
            for r_kid in child_tree_dp(right_li, dic):
                node_i = TreeNode(start_li[i])
                node_i.left = l_kid
                node_i.right = r_kid
                li.append(node_i)  # 存储所有构造好的子树

    if key not in dic:
        dic[key] = li

    return li


def ergodic_tree_mid_li(node: TreeNode, li: list, flag: set):  # 力扣 44 ms 击败88.19%
    """遍历树(中序)"""
    if node.left is not None:
        ergodic_tree_mid_li(node.left, li, flag)

    li.append(node.val)
    if len(li) > 1:
        if li[0] > li[1]:
            flag.add(True)
            return
        if len(li) > 2:
            li.pop(0)

    if node.left is None and node.right is None:
        return

    if node.right is not None:
        ergodic_tree_mid_li(node.right, li, flag)


def test1(tree):
    tmp_li = []
    f = set()
    ergodic_tree_mid_li(tree, tmp_li, f)
    print(tmp_li)
    print(f)
    if len(f) == 0 and len(tmp_li) > 1:
        if tmp_li[0] > tmp_li[1]:  # 进行最后一次判定
            f.add(True)
    print(f)


# def test2(tree):
#     f = False
#     l1 = None
#     l2 = None
#     ergodic_tree_mid(tree, l1, l2, f)
#     if l1 > l2:
#         f = True
#     print(f)


if __name__ == '__main__':
    from small_gram.date_op import start_time, end_time

    ali = [x for x in range(1, 12)]
    adic = dict()
    tree_li = child_tree_dp(ali, adic)
    a_tree = tree_li[1]

    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node4 = TreeNode(5)
    node5 = TreeNode(4, node2, node4)

    node6 = TreeNode(1)
    node7 = TreeNode(2, node6)

    start_time()
    test1(node5)
    end_time()
