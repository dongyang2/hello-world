#!python3
# coding: utf-8
# https://leetcode.cn/problems/clone-graph/
#
# 思路：广度优先搜索
#
# 边界条件：


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


def test():
    node3 = Node(3)
    node2 = Node(2)
    node1 = Node(1, [node2, node3])
    node2.neighbors = [node1, node3]
    node3.neighbors = [node1, node2]
    copy_g(node1)


def copy_g(g: Node):
    node_set = list()
    node_val_set = list()
    # print(g.val)
    node = ergodic_tree(g, node_set, node_val_set)
    print(node_val_set)
    return node


# def ergodic_tree(g: Node, node_set: list, node_val_set: list):
#     if g.val in node_val_set:  # 已经在里面了
#         ind = node_val_set.index(g.val)
#         return node_set[ind]
#
#     node = Node(g.val)  # new node
#     nbors = []
#     for elem in g.neighbors:
#         nbors.append(ergodic_tree(elem, node_set, node_val_set))
#     node.neighbors = nbors
#     node_val_set.append(g.val)
#     node_set.append(node)
#
#     return node


def ergodic_tree(g: Node, node_set: list, node_val_set: list):
    if g.val in node_val_set:  # 已经在里面了
        ind = node_val_set.index(g.val)
        return node_set[ind]

    node = Node(g.val)  # new node
    node_val_set.append(g.val)
    node_set.append(node)

    nbors = node.neighbors
    for elem in g.neighbors:
        nbors.append(ergodic_tree(elem, node_set, node_val_set))

    return node


def test1():
    # li = [11, 12,19]
    # print(bi_search(li, 20))

    matrix = [[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24],
              [18, 21, 23, 26, 30]]
    target = 20


def test2():
    n = 1000
    matrix = [[y * n + x for x in range(n)] for y in range(n)]
    target = 89999
    # print(matrix[299][299])


def test3():
    matrix = [[]]
    target = 0
    # print(matrix[299][299])


def main():
    test()


if __name__ == '__main__':
    from small_gram.date_op import start_time, end_time

    start_time()
    main()
    end_time()
