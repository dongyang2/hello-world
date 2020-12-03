#!python3
# coding: utf-8
# https://leetcode-cn.com/problems/subsets-ii/
# 树的遍历。
# 整体思路：
# 0. 先保证输入有序
# 1. 把输入数组第一个元素当成根节点，树开始生长，把每一条路径加入candidate 数组（不存在时加入），
# 生长终止条件是到达当前输入数组的长度。
# 2. 把当前输入数组的第一个元素删除，得到新数组，对新数组进行步骤1
# 剪枝：子元素比父元素小时，树不再生长
# 相较于直接使用“组合.py” 的代码，这里的思路更因地制宜，且避免了一部分多余操作。


def ergodic_tree(li: list, tmp_li: list, child_i: int, n: int, candidate: list):
    """树的遍历"""
    if tmp_li not in candidate:
        candidate.append(tmp_li)

    # # 终止条件
    # if child_i == n:
    #     return

    for i in range(child_i, n):  # 这里其实隐含了终止条件
        ergodic_tree(li, tmp_li+[li[i]], i+1, n, candidate)


def main():
    li = [1, 4, 2]
    candidate = [[]]
    n = len(li)
    li_sort = sorted(li)
    ergodic_tree(li_sort, [], 0, n, candidate)
    print(candidate)


if __name__ == "__main__":
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
