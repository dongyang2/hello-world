# https://leetcode-cn.com/problems/partition-list/
# coding: utf-8
# Python 3
# 给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前，且保留两个分区中每个节点的初始相对位置。
#
# 思路：遍历一次，开辟n 的空间
# 边界条件：空链表

from interview_q.algorithm.data_structure_node_list import ListNode


def depart_node_list(node: ListNode, x: int):
    if node is None:
        return node
    if node.next is None:
        return node
    head1 = ListNode(-1)  # 存小于x的链表部分
    head1_head = ListNode(-1)
    head2 = ListNode(-1)  # 存大于等于x的链表部分
    head2_head = ListNode(-1)
    head1_head.next = head1
    head2_head.next = head2

    while node is not None:
        tmp = ListNode(node.val)
        if node.val >= x:
            head2.next = tmp
            head2 = head2.next
        else:
            head1.next = tmp
            head1 = head1.next
        node = node.next
    head1.next = head2_head.next.next
    return head1_head.next.next


def main():
    from interview_q.algorithm.data_structure_node_list import ergodic_node_list, build_node_list_by_li
    li = [1, 4, 3, 2, 5, 2]
    node = build_node_list_by_li(li)
    node = depart_node_list(node, 3)
    ergodic_node_list(node, "->")

    node = build_node_list_by_li([])
    node = depart_node_list(node, 3)
    ergodic_node_list(node, "->")


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
