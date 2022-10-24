# coding: utf-8
# https://leetcode.cn/problems/interleaving-string/
# Python 3
#
#
# # 0 <= s1.length, s2.length <= 100
# # 0 <= s3.length <= 200
# # s1、s2、和 s3 都由小写英文字母组成
#
# 思路：回溯法。
#
#
# 边界条件：题中自动给了 s1,s2,s3都是空时，为true
# 备注：


def ergodic_tree(s1: str, s2: str, s3: str, i, j, k, f):
    if k == len(s3) and i == len(s1) and j == len(s2):
        f = 1
        return 1

    if i == len(s1) and s2[j] != s3[k]:
        return 0
    if j == len(s2) and s1[i] != s3[k]:
        return 0

    if s1[i + 1] == s3[k + 1]:
        ergodic_tree(s1, s2, s3, i + 1, j, k + 1, f)
    if s2[j + 1] == s3[k + 1]:
        ergodic_tree(s1, s2, s3, i, j + 1, k + 1, f)

    # if ergodic_tree(s1, s2, s3, i + 1, j, k + 1, f) == 0:
    #     ergodic_tree()

    # return 0


def cross_str(s1: str, s2: str, s3: str):
    i = -1
    j = -1
    k = 0
    turn = 0
    # if s1[i] != s3[k] and s2[j] != s3[k]:
    #     return False
    while k != len(s3):
        # if s1[i+1] != s3[k] and s2[j+1] != s3[k]:
        #     break

        if i == len(s1) and j == len(s2):
            break

        if turn == 0:
            if i < len(s1):
                if s1[i + 1] == s3[k]:
                    i += 1
                    k += 1
                else:
                    turn = 1
            else:
                turn = 1
        else:
            if j < len(s2) and s2[j + 1] == s3[k]:
                j += 1
                k += 1
            else:
                turn = 0

    if k == len(s3) and i == len(s1) and j == len(s2):
        return True
    return False


def bottom_to_up_dp(s1: str, s2: str, s3: str):
    """
    https://leetcode.cn/problems/interleaving-string/solutions/335561/lei-si-lu-jing-wen-ti-zhao-zhun-zhuang-tai-fang-ch/
    """
    m = len(s1)
    n = len(s2)
    if m + n != len(s3):
        return False
    if s1[0] != s3[0] and s2[0] != s3[0]:
        return False

    # 结果数组初始化
    dp = [[False for x in range(m + 1)] for y in range(n + 1)]  # n 行 m 列
    dp[0][0] = True

    # 方便迈出前几步（尤其是第一步）
    for i in range(1, m + 1):
        if s1[i - 1] == s3[i - 1]:
            dp[0][i] = True
        else:
            break
    for i in range(1, n + 1):
        if s2[i - 1] == s3[i - 1]:
            dp[i][0] = True
        else:
            break

    # 核心-动态规划，存前两步（上面或者左边）可以到达的状态。我还以为可以回溯呢，结果人家暴力遍历了
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1] or dp[i][j - 1] and s1[j - 1] == s3[i + j - 1])

    return dp[n][m]


def ergodic_internet(s1: str, s2: str, s3: str, i, j, k, li: list):
    """ 网络上的思路，是我一开始想要做的方式，只是真的没想到是靠二维数组实现。自己对树的遍历还是经验不足呀。
    https://leetcode.cn/problems/interleaving-string/solutions/911891/guan-fang-ti-jie-de-si-lu-xiu-zheng-bu-c-nmc6/
    """
    if li[i][j]:
        return

    status = False
    if i < len(s1) and s1[i] == s3[k]:
        status = True
        ergodic_internet(s1, s2, s3, i + 1, j, k, li)
    if j < len(s2) and s2[j] == s3[k]:
        status = True
        ergodic_internet(s1, s2, s3, i, j + 1, k, li)

    if status:
        li[i][j] = True
    else:
        return


def test1():
    s1 = "aa"
    s2 = "bb"
    s3 = "abab"
    print(bottom_to_up_dp(s1, s2, s3))
    # print(f)


def test2():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    f = 0
    ergodic_tree(s1, s2, s3, 0, 0, 0, f)
    print(f)


def test3():
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    f = [[False for x in range(len(s2)+1)] for _ in range(len(s1)+1)]
    ergodic_internet(s1, s2, s3, 0, 0, 0, f)
    print(f)



if __name__ == '__main__':
    from small_gram.date_op import start_time, end_time

    start_time()
    test1()
    end_time()
