# coding: utf-8
# https://leetcode.cn/problems/binary-tree-inorder-traversal/
# Python 3
#
#
# 思路：
# 边界条件：空树
# 备注： 中序遍历——左中右，前序遍历——中左右，后续遍历——左右中


# # Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def ergodic_tree(node: TreeNode, li: list):
    if isinstance(node.val, TreeNode):
        ergodic_tree_mid(node.val, li)
    else:
        li.append(node.val)


def ergodic_tree_mid(node: TreeNode, li: list):
    """遍历树(中序)"""
    if node.left is not None:
        ergodic_tree_mid(node.left, li)
    li.append(node.val)
    if node.left is None and node.right is None:
        return
    if node.right is not None:
        ergodic_tree_mid(node.right, li)


def inorder_traversal(root: TreeNode):
    if root.val is None or root is None:
        return []
    li = []
    ergodic_tree_mid(root, li)
    return li


def test1():
    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node4 = TreeNode(4)
    node5 = TreeNode(5, node2, node4)
    print(inorder_traversal(node5))


def test2():
    node3 = TreeNode(3)
    node2 = TreeNode(2, node3, None)
    node1 = TreeNode(1, None, node2)
    print(inorder_traversal(node1))


if __name__ == '__main__':
    test1()
