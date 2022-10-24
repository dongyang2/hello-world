# coding: utf-8
# https://leetcode.cn/problems/unique-binary-search-trees/
# Python 3
#
#
# 思路1：
#   此题是https://leetcode.cn/problems/unique-binary-search-trees-ii/ 的优化版，其实想在上题基础上考察动态规划。
#   先遍历各个节点，然后递归地让每个[除此节点外的左边序列]和[除此节点外的右边序列]都制作一次二叉搜索树。
#   终止条件是左边或右边序列都为空。
#
# 思路2：
#   此题与其说是动态规划题，不如说是找规律题，比起上题（https://leetcode.cn/problems/unique-binary-search-trees-ii/）的建树
#   过程，其实更加考察的是对题目的理解，上题的建树肯定超时，找到规律此题递归表达式求出来了，答案就出来了，只要计算数字即可
#   找规律得到 公式1（递归） g(n) = sigma(i=1->n) g(i-1)*g(n-i)
#
#   公式2 卡特兰数。需要有数学背景才易知道， g(n) = (2(2n+1)/n+2) * g(n-1)
#
#
# 边界条件：空树
# 备注：

from interview_q.algorithm.data_structure_leet_code import TreeNode, ergodic_tree_mid, ergodic_tree_front
from small_gram.date_op import start_time, end_time


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


def make_2_li(li: list, ind: int):
    """按li复制出2个新的数组，分别返回左边和右边序列"""
    left_li = li[0:ind]
    right_li = li[ind + 1:]
    return left_li, right_li


def li2str(li: list):
    return ",".join([str(x) for x in li])


def child_tree_num(n: int, dic: dict):  # leet code 40 ms  击败 37.70%
    if n == 1 or n == 0:  # 题中虽没有0，但为方便计算还是要返回一个值
        return 1

    if n in dic:
        return dic[n]

    num = 0
    for i in range(1, 1 + n):
        num += child_tree_num(i - 1, dic) * child_tree_num(n - i, dic)

    dic[n] = num

    return num


def test1(n: int):
    dic = dict()
    start_li = [i for i in range(1, 1 + n)]
    root_li = child_tree_dp(start_li, dic)
    print(len(root_li))
    # for root in root_li:
    #     li = []
    #     ergodic_tree_front(root, li)
    #     print("前序-", li)


def test_null():
    dic = dict()
    start_li = []
    print(child_tree_dp(start_li, dic))


def test2(n: int):
    dic = dict()
    print(child_tree_num(n, dic))

    # for root in root_li:
    #     li = []
    #     ergodic_tree_front(root, li)
    #     print("前序-", li)


if __name__ == '__main__':
    start_time()
    test2(1)
    end_time()
