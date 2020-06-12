# https://leetcode-cn.com/problems/rotate-list/
# coding: utf-8
# Python 3
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 示例
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
#
# 思路：遍历链表。
# 边界条件：空链表


from interview_q.algorithm.data_structure_node_list import ListNode


def left_move_node_list(head: ListNode, k: int):
    init_head = ListNode(-1)
    init_head.next = head

    new_head_head = ListNode(-1)
    init_head2 = head

    new_head = ListNode(-1)
    new_head_head.next = new_head
    count = 0
    while init_head.val is not None:
        if count == k:
            new_head.next = init_head.next
            init_head.next = None
            break
        count += 1
        init_head = init_head.next

    while new_head.next is not None:
        new_head = new_head.next
    new_head.next = init_head2
    real_new_head = new_head_head.next

    return real_new_head.next


def len_node_list(node: ListNode):
    if node is None:
        return None
    count = 0
    while node is not None:
        count += 1
        node = node.next
    return count


def move(node: ListNode, k: int):
    """k>0时右移，k<0时左移"""
    if node is None:
        return node
    if k == 0:
        return node

    n = len_node_list(node)
    if k > 0:
        k = n - abs(k) % n
    else:
        k = abs(k)

    return left_move_node_list(node, k)


def main():
    from interview_q.algorithm.data_structure_node_list import build_node_list_by_li, ergodic_node_list
    head = build_node_list_by_li([1, 2, 3, 4, 5])
    # ergodic_node_list(head, sep="->")

    # node = left_move_node_list(head, 2)
    node = move(head, 2)
    ergodic_node_list(node, sep="->")

    # print(-9 % 4)  # 见证奇迹的时刻
    head = build_node_list_by_li([0, 1, 2])
    node = move(head, 2)
    ergodic_node_list(node, sep="->")


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
