# https://leetcode-cn.com/problems/unique-paths/
# coding:utf-8
# Python 3
# 从左下角走到右下角的路径条数


def diff_path(m, n):
    if m == 0 and n == 0:
        return 0
    if m == 1 and n == 0:
        return 0
    if m == 0 and n == 1:
        return 0
    # if m == 1 and n == 1:  # 题目设定m=1，n=1 输出1
    #     return 0
    if n == 1:
        return 1
    if m == 1:
        return 1

    li = [[0 for __ in range(m + 1)] for _ in range(n + 1)]
    li[2][1] = 1  # m=1 n=2
    li[1][2] = 1  # m=2 n=1
    li[1][1] = 0  # m=1 n=1
    # print(li)
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if j < n + 1 and i < m + 1:
                if li[j][i] != 0:
                    li[i][j] = li[j][i]
                else:
                    li[i][j] = li[i - 1][j] + li[i][j - 1]
            else:
                li[i][j] = li[i - 1][j] + li[i][j - 1]
    # print(li)
    return li[n][m]


def main():
    print(diff_path(3, 2))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
