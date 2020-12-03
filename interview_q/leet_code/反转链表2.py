#!python3
# coding: utf-8
# https://leetcode-cn.com/problems/reverse-linked-list-ii/
# 反转链表的第m个到第n个元素。仅使用一次扫描。
# 思路：空间换时间
# 建立三个链表，第一存m之前的元素，第二个存倒置的m到n的元素，第三个存n之后的元素。
# 连完前两个链表之后，再继续遍历原链表，连第三个。
# 边界条件：n大于链表长度

from interview_q.algorithm.data_structure_node_list import ListNode, build_node_list_by_li, ergodic_node_list


def reverse_node_list_by_designated_pos(nl: ListNode, m: int, n: int):
    """反转链表的第m个到第n个元素。只扫描一次"""
    tmp_li = []
    index = 1
    head = ListNode(-1)  # 保存结果的指针，指向创建新链表的指针
    node = ListNode(-1)  # 创建新链表的指针
    head.next = node
    while nl is not None:
        tmp_val = nl.val
        if index < m:
            tmp_node = ListNode(tmp_val)
            node.next = tmp_node
            node = node.next
        elif index < n:  # n大于链表长度的时候，一直在运行这里直到退出循环
            tmp_li.append(tmp_val)
        elif index == n:  # n小于等于链表长度时，执行这里直到跑到n
            tmp_node = ListNode(tmp_val)
            node.next = tmp_node
            node = node.next
            nl = nl.next
            break

        nl = nl.next
        index += 1

    k = len(tmp_li)
    for i in range(k):
        tmp_node = ListNode(tmp_li[k - i - 1])
        node.next = tmp_node
        node = node.next

    if index == n:
        node.next = nl

    return head.next.next


def main():
    li = [1, 2, 3, 4, 5]
    nl = build_node_list_by_li(li)
    # nl = build_node_list_by_li([])
    ergodic_node_list(nl, "->")
    nl_reverse = reverse_node_list_by_designated_pos(nl, 2, 4)
    ergodic_node_list(nl_reverse, "->")


if __name__ == "__main__":
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
