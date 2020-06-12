# https://leetcode-cn.com/problems/merge-intervals/
# coding: utf-8
# Python 3
#
# 输入: [[1,3],[2,6],[8,10],[15,18]]
# 输出: [[1,6],[8,10],[15,18]]
# 解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#
# 输入: [[1,4],[4,5]]
# 输出: [[1,5]]
# 解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
#
# 思路：排序之后扫描。注意多个可合并的情况，且注意当前区间可能远大于后面的区间。
# 启发式方法：写代码时发现可以只对合并后的区间(ans)做维护或处理。简化了代码。
# 没想到这样的处理不仅加快了处理速度，而且空间占用也很小，第一次看到力扣上还有击败了100%的情况（见“合并区间 力扣结果.jpg”文件）。
# 边界条件：空数组


def merge_interval(li: list):
    n = len(li)
    if n == 0:
        return []
    if n == 1:
        return li

    li_sorted = sorted(li, key=lambda a: a[0])
    ans = [li_sorted[0]]
    i = 1
    while i < n:
        if ans[-1][1] >= li_sorted[i][0]:
            up_bound = max(ans[-1][1], li_sorted[i][1])
            ans[-1][1] = up_bound
        else:
            ans.append(li_sorted[i])
        i += 1
    return ans


def main():
    # li = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # li = [[1, 3], [2, 4], [4, 5], [6, 7]]
    # li = [[1, 7], [2, 4], [4, 5], [9, 17]]
    # li = [[1, 4], [0, 0]]
    li = [[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]]
    print(merge_interval(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
