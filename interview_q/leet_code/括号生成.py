# https://leetcode-cn.com/problems/generate-parentheses/
# coding: utf-8
# Python 3
# 给出 n 代表生成括号的对数，写出一个函数，使其能够生成所有可能的并且有效的括号组合。
# 错误思路：找规律迭代法。找出了跳台阶的规律。
# 思路：把第一个括号作为根节点，之后每加进一个括号就代表加了一层，最后转换成二叉树合理路径的寻找。
# 边界情况：


def gen_parentheses(n: int):
    li = []
    find_path_new(n, 0, 0, '', li)
    return li


def append_extend(elem, li):
    if elem not in li:
        li.append(elem)


def find_path(n, c1, c2, tmp, li, node):
    """
    找到合理路径
    """
    if c1 == c2 and c1 == n:
        li.append(tmp)
        return
    if c2> c1:
        return

    if node == 'left':
        if c1 < n:
            tmp += '('
            c1 += 1

    if node == 'right':
        if c2 < n:
            tmp += ')'
            c2 += 1

    find_path(n, c1, c2, tmp, li, 'left')
    find_path(n, c1, c2, tmp, li, 'right')


def find_path_new(n, c1, c2, tmp, li):
    """
    找到合理路径
    :param n:   指定括号对的数量
    :param c1:  左括号的数量
    :param c2:  右括号的数量
    :param tmp: 当前可行的路径
    :param li:  存储所有路径
    """

    # 设定终止条件，在每次找到可行路径时，断开递归
    if c1 == c2 and c1 == n:
        li.append(tmp)
        return

    # 右括号不能在某一时刻大于左括号的数量
    if c2 > c1:
        return

    if c1 < n:
        # 注意递归这里，不能把c1+1和tmp+'('写在外面，如下
        #   c1 += 1
        #   tmp += '('
        # 这里想要遍历树，就要在当前结点下直接传递其下一代的值，否则会出现重复的结果。
        # （因为当前结点的c1，c2，tmp都是固定的，下面传到右孩子结点时还要用到当前结点的信息。）
        find_path_new(n, c1+1, c2, tmp + '(', li)

    if c2 < n:
        find_path_new(n, c1, c2+1, tmp + ')', li)


def main():
    li = gen_parentheses(2)
    print(li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
