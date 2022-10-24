# coding: utf-8
# https://leetcode.cn/problems/unique-binary-search-trees-ii/
# Python 3
#
#
# 思路：
#   其实就是树的生成，和全排列的区别是啥？区别是对数据结构的理解，并且这里和数组全排列还是有区别的
#   先遍历各个节点，然后递归地让每个[除此节点外的左边序列]和[除此节点外的右边序列]都制作一次二叉搜索树。
#   终止条件是左边或右边序列都为空。
# 边界条件：空树
# 备注：


from interview_q.algorithm.data_structure_leet_code import TreeNode, ergodic_tree_mid, ergodic_tree_front
from small_gram.date_op import start_time, end_time


def make_2_li(li: list, ind: int):
    """按li复制出2个新的数组，分别返回左边和右边序列"""
    left_li = li[0:ind]
    right_li = li[ind + 1:]
    return left_li, right_li


# def ergodic_tree(start_li:list,node:TreeNode, flag,permutation_li:list):
#
#
#     for i in range(len(start_li)):
#         node_i = TreeNode(start_li[i])
#         # node.val = TreeNode(start_li[i])
#         if flag == "left":
#             node.left = node_i
#         elif flag == "right":
#             node.right = node_i
#         else:
#             node.val = start_li[i]
#
#         left_li, right_li = make_2_li(start_li, i)
#         ergodic_tree(left_li, node,"left", permutation_li)
#         ergodic_tree(right_li, node,"right", permutation_li)


# def make_tree(lnode:TreeNode, rnode:TreeNode, root:TreeNode, node:TreeNode, start_li:list, permutation_li:list):
#     if len(start_li)== 3 and lnode.val < node.val < rnode.val:
#         node.left = lnode
#         node.right = rnode
#         permutation_li.append(root)
#         return
#
#     if len(start_li)== 2:
#         node0 = TreeNode(start_li[0])
#         node1 = TreeNode(start_li[1])
#
#         if start_li[0] < start_li[1]:
#             node1.left = node0
#         else:
#             node0.left = node1

def check_flag_insert(root: TreeNode, node: TreeNode, flag):
    if flag == "left":
        root.left = node
    elif flag == "right":
        root.right = node


def make_tree3(start_li: list, node: TreeNode, root: TreeNode, permutation_li: list):
    if len(start_li) == 2:
        if start_li[0] < node.val < start_li[1]:
            node.left = TreeNode(start_li[0])
            node.right = TreeNode(start_li[1])
            return

    if len(start_li) == 1:
        if start_li[0] < node.val:
            node.left = TreeNode(start_li[0])
            return
        else:
            node.right = TreeNode(start_li[1])
            return

    for i in range(len(start_li)):
        left_li, right_li = make_2_li(start_li, i)
        node_i = TreeNode(start_li[i])

        if root.left is not None:
            if start_li[i] < root.val:
                root.left = node_i
                if left_li:
                    make_tree3(left_li, node_i, root, permutation_li)
            else:
                if right_li:
                    make_tree3(right_li, node_i, root, permutation_li)
        elif root.right is not None:
            if start_li[i] < root.val:
                root.left = node_i
                if left_li:
                    make_tree3(left_li, node_i, root, permutation_li)
            else:
                root.right = node_i
                if right_li:
                    make_tree3(right_li, node_i, root, permutation_li)
        else:
            pass


# import copy
# def make_tree4(start_li: list, node: TreeNode, permutation_li: list, j: int):
#     if not start_li:
#         return
#
#     if len(start_li) == 2:
#         if start_li[0] < node.val < start_li[1]:
#             node.left = TreeNode(start_li[0])
#             node.right = TreeNode(start_li[1])
#             return
#
#     for i in range(len(start_li)):
#         new_node = copy.deepcopy(permutation_li[j])
#         left_li, right_li = make_2_li(start_li, i)
#         node_i = TreeNode(start_li[i])
#         if start_li[i] < node.val:
#             node.left = node_i
#         else:
#             node.right = node_i
#
#         # new_node
#         k = len(permutation_li) + i  # 指示当前新建根节点的位置
#
#         make_tree4(left_li, node_i, permutation_li, k)
#         make_tree4(right_li, node_i, permutation_li, k)


# 发现受数据结构所限。自顶向下实现不了，主要是根节点的维护和复制比较难实现，只有自底向上（从叶子节点到根节点）
# 下面都是自底向上法
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


def li2str(li: list):
    return ",".join([str(x) for x in li])


def test2(n: int):
    start_li = [x for x in range(1, 1 + n)]
    root_li = child_tree(start_li)
    print(len(root_li))
    # for root in root_li:
    #     # li = []
    #     # ergodic_tree_mid(root, li)
    #     # print("中序-", li)
    #
    #     li = []
    #     ergodic_tree_front(root, li)
    #     print("前序-", li)


def test_null():
    start_li = []
    print(child_tree(start_li))


def test3(n):
    dic = dict()
    start_li = [x for x in range(1, 1 + n)]
    root_li = child_tree_dp(start_li,dic)
    print(len(root_li))

if __name__ == '__main__':
    start_time()
    test3(5)
    end_time()
