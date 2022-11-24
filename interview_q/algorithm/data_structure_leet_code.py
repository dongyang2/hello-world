# Python 3
# coding:utf-8
# 备注： 中序遍历——左中右，前序遍历——中左右，后续遍历——左右中


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ergodic_tree_mid(node: TreeNode, li: list):
    """遍历树(中序)"""
    if node.left is not None:
        ergodic_tree_mid(node.left, li)

    li.append(node.val)
    if node.left is None and node.right is None:  # 叶子结点
        return

    if node.right is not None:
        ergodic_tree_mid(node.right, li)


def ergodic_tree_front(node: TreeNode, li: list):
    """遍历树(前序)"""

    li.append(node.val)
    if node.left is None and node.right is None:
        return

    if node.left is not None:
        ergodic_tree_front(node.left, li)
    if node.right is not None:
        ergodic_tree_front(node.right, li)


def make_2_li(li: list, ind: int):
    """按li复制出2个新的数组，分别返回左边和右边序列"""
    left_li = li[0:ind]
    right_li = li[ind + 1:]
    return left_li, right_li


def child_tree(start_li: list):  # leet code 60 ms
    """根据节点数构造二叉搜索树"""
    if not start_li:
        return [None]

    if len(start_li) == 1:
        return [TreeNode(start_li[0])]

    # if len(start_li) == 3:
    #     if start_li[0] < start_li[1] < start_li[2]:
    #         return [TreeNode(start_li[1], TreeNode(start_li[0]), TreeNode(start_li[2]))]

    li = []
    for i in range(len(start_li)):
        left_li, right_li = make_2_li(start_li, i)  # 这里合理利用了二叉搜索树的性质
        # 遍历所有构造好的子树，插到新创建的根节点里面
        for l_kid in child_tree(left_li):
            for r_kid in child_tree(right_li):
                node_i = TreeNode(start_li[i])
                node_i.left = l_kid
                node_i.right = r_kid
                li.append(node_i)  # 存储所有构造好的子树

    return li
