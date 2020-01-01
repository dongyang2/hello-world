# https://leetcode-cn.com/problems/merge-two-sorted-lists/
# coding: utf-8
# Python 3
# 题意如文件名
# 边界情况：空链表

from interview_q.algorithm.data_structure_node_list import ListNode, build_node_list_by_li, ergodic_node_list


def merge_node_list(ln1: ListNode, ln2: ListNode):
    if ln1 is None and ln2 is None:
        return None
    elif ln1 is None:
        return ln2
    elif ln2 is None:
        return ln1

    head = ListNode(-1)
    if ln1.val > ln2.val:
        head.next = ln2
        front = head
        i1 = head.next
        i2 = ln1
    else:
        head.next = ln1
        front = head
        i1 = head.next
        i2 = ln2

    while i2 is not None:
        if i1 is None:
            front.next = i2
            break
        if i2.val < i1.val:
            front.next = i2
            i2 = i2.next        # 先释放i2现在指向的元素，释放后，i2现在指向的变成了刚才指向的后一个元素
            front = front.next  # 再将front指向i2刚才指向的元素
            front.next = i1
        else:
            i1 = i1.next
            front = front.next

    return head.next


def main():
    ln1 = build_node_list_by_li([])
    ln2 = build_node_list_by_li([2, 4, 6, 8, 10])
    node = merge_node_list(ln1, ln2)
    ergodic_node_list(node)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
