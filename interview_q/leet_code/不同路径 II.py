# https://leetcode-cn.com/problems/unique-paths-ii/
# coding:utf-8
# Python 3
# 从左下角走到右下角的路径条数，中间可能有障碍物


def diff_path(grid):
    n = len(grid)
    m = len(grid[0])

    li = [[0 for __ in range(m + 1)] for _ in range(n + 1)]
    li[1][1] = 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if grid[i - 1][j - 1] == 1:
                li[i][j] = 0
            else:
                if i == 1 and j == 1:
                    continue
                li[i][j] = li[i - 1][j] + li[i][j - 1]
    # print(li)
    return li[n][m]


def main():
    # li = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    li = [[1]]
    print(diff_path(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
