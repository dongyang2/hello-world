# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/
# coding: utf-8
# Python 3
# PyCharm 2018.2.1
# 给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。
#
# 思路：我不理解这题为什么放在“删除排序链表中的重复元素 II”后面。
# 边界条件：空，只有一个元素。
from interview_q.algorithm.data_structure_node_list import ListNode


def clear_sorted_node_list(head: ListNode):
    if head is None:
        return head
    if head.next is None:
        return head
    init_val = head.val-1
    init_node1 = ListNode(init_val)
    init_node1.next = head

    while head.next is not None:
        tmp = head.next
        if head.val == tmp.val:
            head.next = tmp.next
        else:
            head = tmp

    return init_node1.next


def main():
    from interview_q.algorithm.data_structure_node_list import build_node_list_by_li, ergodic_node_list

    li = [1, 1, 2, 2, 3, 6, 6, 7]
    node = build_node_list_by_li(li)
    clear_node = clear_sorted_node_list(node)
    ergodic_node_list(clear_node, sep="->")

    li = []
    node = build_node_list_by_li(li)
    clear_node = clear_sorted_node_list(node)
    ergodic_node_list(clear_node, sep="->")


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
