# https://leetcode-cn.com/problems/permutations/
# coding:utf-8
# Python 3


def permutation(li: list, start: int, m: int, ans: list):
    """网上解法1."""
    # print('start', start)
    if start == m - 1:
        # print(li)
        ans.append(li.copy())
    else:
        for i in range(start, m):
            # print(i, start)
            li[start], li[i] = li[i], li[start]
            permutation(li, start + 1, m, ans)
            li[start], li[i] = li[i], li[start]


# def dfs(nums, index, pre, used, res):
#     if index == len(nums):
#         res.append(pre.copy())
#         return
#
#     for i in range(len(nums)):
#         if not used[i]:
#             # 如果没有用过，就用它
#             used[i] = True
#             pre.append(nums[i])
#
#             # 在 dfs 前后，代码是对称的
#             dfs(nums, index + 1, pre, used, res)
#
#             used[i] = False
#             pre.pop()


def permutation_m(li: list, start: int, m: int, ans: list, ll: int):
    """根据网上解法1做的得到n个数中m个数的排列"""
    if start == ll - 1 and li[-m:] not in ans:
        ans.append(li[-m:].copy())
    else:
        for i in range(start, ll):
            li[start], li[i] = li[i], li[start]
            permutation_m(li, start + 1, m, ans, ll)
            li[start], li[i] = li[i], li[start]


def main():
    n = 4
    li = [i for i in range(n)]
    ans = []
    # permutation(li, 0, n, ans)
    # # print(len(ans))
    # print(ans)
    #
    # # 然后是找到n个数中m个数的排列，如[1,2,3]里面找两个，结果是12,13,23,21,31,32
    # m_li = []
    # m = 2
    # for i in range(len(ans)):
    #     if ans[i][-m:] not in m_li:
    #         m_li.append(ans[i][-m:])
    # print(m_li)
    #
    # # used = [False] * len(li)
    # # ans = []
    # # dfs(li, 0, [], used, ans)
    # # print(len(ans))
    # # print(ans)

    permutation_m(li, 0, 4, ans, n)
    print(ans)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
