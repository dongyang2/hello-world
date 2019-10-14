# 剑指offer 头两题其实是为了c++和c# 写的，我从第三题开始，这里开始有不和语言挂钩的算法。

# coding: utf-8
# Python 3


def find_same_element(li: list):
    """找到数组中所有出现次数超过1的数字"""
    ll = len(li)
    if ll <= 0:
        return False

    # # 当数组内元素的范围在0~ll 之间时，可以使用剑指offer 的这个算法
    # return point_to_offer(li, ll)
    return find_same_element_hash_table(li)


def point_to_offer(li, n):
    """剑指offer法"""
    rep = []
    for i in range(n):
        tmp = li[i]
        while i != tmp:
            if li[tmp] == li[i]:
                rep.append(li[tmp])
                break
            li[i], li[tmp], tmp = li[tmp], li[i], li[tmp]

    return rep


def find_same_element_hash_table(li):
    """哈希表法，比剑指offer法更快，但需要O(n)的空间"""
    se = set()
    rep = set()
    for i in li:
        if i not in se:
            se.add(i)
        else:
            rep.add(i)
    return rep


def main():
    li = [2, 3, 1, 0, 2, 5, 3]
    print(find_same_element(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
