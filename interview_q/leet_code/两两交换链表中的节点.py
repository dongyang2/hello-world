# https://leetcode-cn.com/problems/swap-nodes-in-pairs/
# coding: utf-8
# Python 3
# 交换输入链表中，第i个与第i+1个结点，i=1,3,5,7,9······题中没有说明遇到了奇数个结点怎么办，若奇数，暂不处理最后一个。
# 思路：在草稿纸上一画，按照画的步骤写即可。感觉是简单难度。
# 边界情况：

from interview_q.algorithm.data_structure_node_list import ListNode, build_node_list_by_li, ergodic_node_list


def swap_by_node_pairs(head: ListNode):
    init_node = ListNode(-1)
    init_node.next = head
    # count = 0
    front_node = init_node
    while front_node.next is not None:
        first_node = front_node.next
        if first_node.next is None:
            break
        second_node = first_node.next
        front_node.next = second_node
        first_node.next = second_node.next
        front_node = first_node
        second_node.next = first_node

    return init_node.next


def main():
    head = build_node_list_by_li([1, 2, 3, 4, 5])
    node = swap_by_node_pairs(head)
    print('交换完成')
    ergodic_node_list(node, '->')


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
