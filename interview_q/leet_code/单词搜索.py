# https://leetcode-cn.com/problems/word-search/
# coding: utf-8
# Python 3
# 给定一个二维网格和一个单词，找出该单词是否存在于网格中。
# 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。
#
# 思路：找到第一个字母后，进行四叉树的遍历。
# 边界条件：


def search(li, s):
    n = len(li)
    if n == 0:
        return False
    m = len(li[0])

    first_letter = []
    for i in range(n):
        for j in range(m):
            if li[i][j] == s[0]:
                first_letter.append([i, j])

    for let in first_letter:
        flag_li = []
        bool_find_it = ergodic_tree(li, let[0], let[1], flag_li, s, 0)
        if bool_find_it is True:
            return True
    return False


def ergodic_tree(li, i, j, fl, s, si):
    if 0 <= i < len(li) and 0 <= j < len(li[0]):
        if [i, j] not in fl:
            if li[i][j] == s[si]:
                tmp_fl = add(fl, i, j)
                if si + 1 == len(s):
                    return True
                else:
                    si += 1
                    # 下面这一句是本篇代码的精华，or 关键字可以让我们试探性地往前伸一脚，发现不对，就立即把脚缩回来
                    return ergodic_tree(li, i + 1, j, tmp_fl, s, si) or ergodic_tree(li, i, j + 1, tmp_fl, s, si) or \
                        ergodic_tree(li, i - 1, j, tmp_fl, s, si) or ergodic_tree(li, i, j - 1, tmp_fl, s, si)
    return False


def add(li, i, j):
    # 与所有树的遍历一样，需要开辟新空间以应对遍历时遇到的不同子树
    return li+[[i, j]]


def main():
    # li = []
    # li2 = li + [[0, 0]]
    # print(li2)
    # li3 = li2 + [[1, 2]]
    # print(li3)

    li = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    s = "ABCCED"
    print(search(li, s))

    s = "ABCB"
    print(search(li, s))

    s = "SEE"
    print(search(li, s))

    li = [["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]]
    s = "AAB"
    print(search(li, s))

    li = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
    s = "ABCESEEEFS"
    print(search(li, s))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
