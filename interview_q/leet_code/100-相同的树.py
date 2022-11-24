# coding: utf-8
# https://leetcode.cn/problems/same-tree/
# Python 3
#
#
# 思路：前序遍历+中序遍历，或后序遍历+中序遍历
#
#
# 边界条件：空节点，值一样的树
# 备注：规定两树节点数范围 [0, 100] ，水题。第100题！超简单，啦啦啦！
# kao !! 有个边界条件-空节点，值一样的树
# 是我小看这题了！！！成功率25% ！！！一点儿也不水！！！
#
# 优化方法：可以两棵树一起遍历。

from interview_q.algorithm.data_structure_leet_code import TreeNode


def ergodic_tree_mid(node: TreeNode, li: list):
    """遍历树(中序)"""
    if node.left is not None:
        ergodic_tree_mid(node.left, li)
    if node.left is None and node.right is not None:
        li.append("null")

    li.append(node.val)
    if node.left is None and node.right is None:  # 叶子结点
        return

    if node.right is not None:
        ergodic_tree_mid(node.right, li)
    if node.right is None and node.left is not None:
        li.append("null")


def ergodic_tree_front(node: TreeNode, li: list):
    """遍历树(前序)"""
    li.append(node.val)
    if node.left is None and node.right is None:
        return

    if node.left is not None:
        ergodic_tree_front(node.left, li)
    if node.left is None and node.right is not None:
        li.append("null")

    if node.right is not None:
        ergodic_tree_front(node.right, li)
    if node.right is None and node.left is not None:
        li.append("null")


def same_tree(node1: TreeNode, node2: TreeNode):  # 力扣 时间44 ms 击败16.26% 内存15.2 MB 击败5.2%
    if node1 is None:
        if node2 is None:
            return True
        else:
            return False
    else:
        if node2 is None:
            return False

    li1 = []
    ergodic_tree_mid(node1, li1)
    li2 = []
    ergodic_tree_front(node1, li2)

    li3 = []
    ergodic_tree_mid(node2, li3)
    li4 = []
    ergodic_tree_front(node2, li4)
    print("li1 ", li1, "\nli2", li2, "\nli3 ", li3, "\nli4", li4)
    if li1 == li3 and li2 == li4:
        return True

    return False


def main():
    from small_gram.date_op import start_time, end_time
    node1 = TreeNode(1)
    node2 = TreeNode(2, node1)
    node3 = TreeNode(3, node2)
    node4 = TreeNode(4, node3)
    node5 = TreeNode(5, None, node4)

    node6 = TreeNode(5, None, node4)

    node7 = TreeNode(1)
    node8 = TreeNode(1, node7)

    node9 = TreeNode(1, None, node7)

    start_time()
    print(same_tree(node8, node9))
    end_time()


if __name__ == '__main__':
    main()
