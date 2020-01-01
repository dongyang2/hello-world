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


def ergodic_node_list(node: ListNode):
    # 遍历链表
    # node = build_node_list(5)
    if node is None:
        return None
    while node is not None:
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


def main():
    # node = build_node_list(5)
    node = build_node_list_by_li([])
    # if node is None:
    #     print('none.')
    ergodic_node_list(node)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
