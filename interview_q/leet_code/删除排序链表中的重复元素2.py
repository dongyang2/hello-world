# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii/
# coding: utf-8
# Python 3
# PyCharm 2018.2.1
# 给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。
#
# 思路：
# 边界条件：
from interview_q.algorithm.data_structure_node_list import ListNode


def del_all_same_node_list(head: ListNode):
    if head is None:
        return head
    if head.next is None:
        return head
    init_val = head.val-1
    init_node1 = ListNode(init_val)
    init_node1.next = head
    init_node2 = ListNode(init_val)
    init_node2.next = init_node1
    count = 0

    while init_node1.next is not None:
        tmp = init_node1.next
        while tmp.next is not None:
            tmp_next = tmp.next
            if tmp.val == tmp_next.val:
                tmp = tmp_next
                count += 1
            else:
                break
        if count == 0:
            init_node1 = init_node1.next
        else:
            init_node1.next = tmp.next
            count = 0

    return init_node2.next.next


def main():
    from interview_q.algorithm.data_structure_node_list import build_node_list_by_li, ergodic_node_list
    li = [1, 1, 2, 2, 3, 6, 6, 7]
    node = build_node_list_by_li(li)
    clear_node = del_all_same_node_list(node)
    ergodic_node_list(clear_node, sep="->")

    li = []
    node = build_node_list_by_li(li)
    clear_node = del_all_same_node_list(node)
    ergodic_node_list(clear_node, sep="->")


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
