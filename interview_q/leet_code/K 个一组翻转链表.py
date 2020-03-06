# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/
# coding: utf-8
# Python 3
# 输入一个链表，指定一个整数k，颠倒由其第i,i+1,i+2...i+k-1个结点组成的子链表的顺序，i=1,2,3······
# 若最后几个元素小于k个，则不做处理。
# 思路：相较于“两两交换链表中的节点”一题，此题只多了翻转链表这个操作。
# 边界情况：

from interview_q.algorithm.data_structure_node_list import ListNode, build_node_list_by_li, ergodic_node_list


def reverse_a_node_list(nl: ListNode, n):
    # 在知道链表长度的情况下，以移动结点的方式翻转链表。此函数也可用作翻转前n个元素。
    if n == 1:
        return nl

    init_node = ListNode(-1)
    init_node.next = nl

    # 第i次循环，把原链表倒数第i个元素移动到新链表第i的位置。只需要循环n-1次是因为那一次已经把第1个元素给放到新链表的最后了。
    front_node = init_node
    for i in range(n-1):
        tmp_front = front_node.next
        for _ in range(n-i-2):  # 找到倒数第i个元素的前一个元素
            tmp_front = tmp_front.next
        tmp = tmp_front.next
        tmp_front.next = tmp.next
        tmp.next = front_node.next
        front_node.next = tmp
        front_node = tmp
    return init_node.next


def reverse_node_list_by_k(nl: ListNode, k: int):
    # 常数个额外空间，代表着无法把链表按每k个进行截取再放入reverse NodeList函数里。
    init_node = ListNode(-1)
    init_node.next = nl

    front = init_node
    while front.next is not None:
        front_x = front
        first_node = front.next
        count = 0
        while front_x.next is not None:  # 让front_x跑到每k个的最后一个元素
            if count == k:
                break
            front_x = front_x.next
            count += 1
        if count < k:
            break

        for i in range(k - 1):
            tmp_front = front.next
            for _ in range(k - i - 2):  # 找到倒数第i个元素的前一个元素
                tmp_front = tmp_front.next
            tmp = tmp_front.next
            tmp_front.next = tmp.next
            tmp.next = front.next
            front.next = tmp
            front = tmp
        front = first_node

    return init_node.next


def main():
    li = [1, 2, 3, 4, 5, 6]
    head = build_node_list_by_li(li)
    # node = reverse_a_node_list(head, len(li)-1)
    # print('翻转完成')
    # ergodic_node_list(node)

    node = reverse_node_list_by_k(head, 3)
    print('按k翻转完成')
    ergodic_node_list(node, '->')


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))

