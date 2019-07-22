class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1 = list_node_to_str(l1)
        int1 = str_to_int(s1)
        s2 = list_node_to_str(l2)
        int2 = str_to_int(s2)
        add = str(int1 + int2)
        tmp_s = ''
        for s_i in add[::-1]:
            tmp_s += s_i

        return str_to_list_node(tmp_s)


def str_to_list_node(s: str):
    if len(s) == 0:
        raise ValueError('请输入非空字符串')
    tmp_li = []
    start_node = ListNode(int(s[0]))
    if len(s) == 1:
        return start_node
    else:
        count = 0
        for i in s[1:]:
            now_node = ListNode(int(i))
            if count == 0:
                start_node.next = now_node
                count = 1
            else:
                last_node.next = now_node
            last_node = now_node
        return start_node


def list_node_to_str(ln: ListNode):
    if ln.val is None:
        raise ValueError('请输入非空链表')
    s = ''
    while ln.next is not None:
        s += str(ln.val)
        ln = ln.next
    s += str(ln.val)
    return s


def str_to_int(s: str):
    """逆序遍历字符串，将每个字符转为整数"""
    if len(s) == 0:
        raise ValueError('请输入非空字符串')
    tmp_s = ''
    for s_i in s[::-1]:
        tmp_s += s_i
    return int(tmp_s)