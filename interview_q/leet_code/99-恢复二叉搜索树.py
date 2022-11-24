# coding: utf-8
# https://leetcode.cn/problems/recover-binary-search-tree/
# Python 3
#
#
# 思路：考察二叉树的中序遍历。注意考虑节点相等的情况。
#   其实和验证二叉搜索树是一个思路，只是需要存储不满足条件的节点值。
#   具体地，在草稿纸中画出几种“已被交换”的条件，然后总结出以下情况：
#       1.存在一组前后不一致的节点。此时组内交换即可。
#       2.存在两组前后不一致的节点。此时交换第一组的第一个和第二组的第二个。
#
# 边界条件：单个节点
# 备注：上述思路其实就是O（1）空间，符合力扣要求

from interview_q.algorithm.data_structure_leet_code import TreeNode, ergodic_tree_mid


def ergodic_tree_mid_recover(root: TreeNode, li: list, sl: list):
    if root.left is not None:
        ergodic_tree_mid_recover(root.left, li, sl)

    if len(li) < 2:
        li.append(root)
    else:
        if li[0].val > li[1].val:
            sl.append((li[0], li[1]))
        li.append(root)
        li.pop(0)
    if root.left is None and root.right is None:
        return

    if root.right is not None:
        ergodic_tree_mid_recover(root.right, li, sl)


def recover_binary_tree(root: TreeNode):  # 力扣 时间64 ms 击败52.19% 内存15.3 MB 击败81.66%
    li1 = []
    sl = []
    ergodic_tree_mid_recover(root, li1, sl)
    if len(li1) > 1:
        if li1[0].val > li1[1].val:
            sl.append((li1[0], li1[1]))
    print("特殊数组", sl, "\n 特殊数组长度 ", len(sl))
    if len(sl) > 0:
        if len(sl) == 1:
            sl[0][0].val, sl[0][1].val = sl[0][1].val, sl[0][0].val
        else:
            sl[0][0].val, sl[1][1].val = sl[1][1].val, sl[0][0].val


def test1():
    pass


def main():
    from small_gram.date_op import start_time, end_time

    node1 = TreeNode(1)
    node3 = TreeNode(3)
    node2 = TreeNode(2, node1, node3)
    node4 = TreeNode(4)
    node5 = TreeNode(5, node2, node4)

    # 节点交换
    # tmp1 = node2
    # tmp2 = node4
    # tmp2.val, tmp1.val = tmp1.val, tmp2.val
    li = []
    ergodic_tree_mid(node5, li)
    print("中序遍历", li)
    recover_binary_tree(node5)
    li3 = []
    ergodic_tree_mid(node5, li3)
    print("修复后", li3)

    node6 = TreeNode(2)
    node7 = TreeNode(1, node6)

    start_time()
    recover_binary_tree(node7)
    end_time()

    recover_binary_tree(node6)


if __name__ == '__main__':
    main()
