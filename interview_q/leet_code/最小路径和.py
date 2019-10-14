# https://leetcode-cn.com/problems/minimum-path-sum/
# coding:utf-8
# Python 3


def diff_path(li):
    n = len(li)
    m = len(li[0])

    for i in range(1, m):  # 因为限定只能向右或者向下走，所以第一行的数字没法变
        li[0][i] += li[0][i - 1]
    for i in range(1, n):
        li[i][0] += li[i - 1][0]

    for i in range(1, n):
        for j in range(1, m):
            zuo = li[i][j - 1]
            shang = li[i - 1][j]
            if shang >= zuo:
                li[i][j] += zuo
            else:
                li[i][j] += shang
    print(li)
    return li[n - 1][m - 1]


def main():
    li = [[1,2],[5,6],[1,1]]
    # li = [[1]]
    print(diff_path(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
