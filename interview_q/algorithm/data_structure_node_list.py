# 链表
# Python 3
# coding:utf-8


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_node_list(n: int):
    # 建立一个“自然数”链表
    init_node = ListNode(0)
    j = init_node
    for i in range(n):
        tmp = ListNode(i+1)
        j.next = tmp
        if i == n-1:
            j.next = None
        j = tmp
    return init_node


def ergodic_node_list(node: ListNode, sep=''):
    # 遍历链表
    # node = build_node_list(5)
    if node is None:
        return None
    while node is not None:
        if sep != '':
            if node.next is not None:
                print(node.val, end=sep)
            else:
                print(node.val)
        else:
            print(node.val)
        node = node.next


def build_node_list_by_li(li: list):
    n = len(li)
    if n == 0:
        return None
    init_node = ListNode(li[0])
    j = init_node
    for i in range(n-1):
        tmp = ListNode(li[i+1])
        j.next = tmp
        j = tmp
    return init_node


def reverse_a_node_list(nl: ListNode, n):
    # 在知道链表长度的情况下，以移动结点的方式翻转链表。此函数也可用作翻转前n个元素。
    if n == 1:
        return nl
    elif n < 1:
        raise ValueError('链表的长度需要大于0')

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


def main():
    # node = build_node_list(5)
    li = [1, 2, 3, 4, 5]
    node = build_node_list_by_li(li)
    # if node is None:
    #     print('none.')
    ergodic_node_list(node, sep='->')


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
