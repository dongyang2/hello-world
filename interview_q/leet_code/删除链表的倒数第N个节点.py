# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/solution/
# coding: utf-8
# Python 3
# 题意如文件名所示，且规定i一定合法。
# 思路：双指针。
# 边界情况：只有一个元素，删除它。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_the_i_th_node_from_the_end(head: ListNode, i: int):
    # 创建一个无意义的头指针，让它指向head
    node0 = ListNode(-1)
    node0.next = head
    node1 = node0
    node2 = node0
    count = 0  # 用来维持双指针的距离
    while node2.next is not None:
        if count < i:
            node2 = node2.next
            # if node2 is not None:
            #     print(node2.val)
            count += 1
        else:
            node2 = node2.next
            node1 = node1.next
    tmp = node1.next
    node1.next = tmp.next
    return node0.next


def build_node_list(n: int):
    init_node = ListNode(0)
    j = init_node
    for i in range(n):
        tmp = ListNode(i+1)
        j.next = tmp
        if i == n-1:
            j.next = None
        j = tmp

    return init_node


def ergodic_node_list(node: ListNode):
    while node is not None:
        print(node.val)
        node = node.next


def main():
    head = build_node_list(5)
    node = remove_the_i_th_node_from_the_end(head, 2)
    print('去除完成')
    ergodic_node_list(node)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
