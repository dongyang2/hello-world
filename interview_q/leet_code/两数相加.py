# https://leetcode-cn.com/problems/add-two-numbers/
# utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def ergodic(ln: ListNode):
    li = []
    while ln.next is not None:
        li.append(str(ln.val))
        ln = ln.next
    return li


# 搞不懂这个Python链表怎么实现的
def add_two_num(l1: ListNode, l2: ListNode):
    s1 = ''.join(ergodic(l1)).__reversed__()
    s2 = ''.join(ergodic(l2)).__reversed__()
    num1 = int(s1)
    num2 = int(s2)
    add = num1+num2
    ln = ListNode()
    for i in add:
        ln.val = i
        ln = ln.next
    return ln


