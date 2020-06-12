# https://leetcode-cn.com/problems/subsets/
# coding: utf-8
# Python 3
# 给定一组不含重复元素的整数数组，返回该数组所有可能的子集，包括空集。
#
# 思路：直接使用“组合.py”文件的函数。
# 优化方法，观察输入n=10时的结果，发现后面的结果等于输入数组与前面的结果的差集。如，长度为9的子集，一定等于长度为10的子集减长度为1的子集的结果。
# 边界条件：


def erg_new_new(li, k, tmp, com):
    n = len(tmp)
    if n == k:
        com.append(tmp)
    else:
        for i in range(len(li)):
            if n > 0 and li[i] < tmp[-1]:
                continue
            elif n <= k-1:
                    # erg_new_new(li[i+1:], k, append_val(tmp, li[i]), com)
                    erg_new_new(li[i + 1:], k, tmp+[li[i]], com)


def combination(li, k):
    n = len(li)
    if k > n or k == 0:
        return []
    if k == 1:
        return [[x] for x in li]
    if k == n:
        return [li]
    com = []
    erg_new_new(li, k, [], com)
    return com


def sub_set(li):
    ss = [[[]]]
    sorted_li = sorted(li)
    n = len(li)
    half = int(n/2)
    for i in range(1, half+1):
        ss.append(combination(sorted_li, i))
    if n % 2 == 0:
        start_reverse = n-half+1
    else:
        start_reverse = n-half
    for i in range(start_reverse, n+1):
        tmp = []
        for j in ss[n-i]:
            tmp.append(difference(li, j))
        ss.append(tmp)
    ans = []
    for i in ss:
        ans += i
    return ans


def difference(li, sub_li):
    return [x for x in li if x not in sub_li]


def main():
    tmp = []
    tmp += []
    print(tmp)

    tmp = [[]]
    tmp += []  # 原来Python默认把数组加空数组处理成了不连接（即不会多加一个空数组）
    print(tmp)

    tmp = [[]]
    tmp += [[]]  # 想加空数组要这么操作。
    print(tmp)

    tmp = [[]]
    tmp += [[1], [2]]
    print(tmp)

    li1 = [1, 3, 5, 6]
    li2 = [4, 6]
    print(difference(li1, li2))

    li1 = [1, 3, 5, 6]
    li2 = []
    print(difference(li1, li2))

    n = 20
    li = [x+1 for x in range(n)]
    # print(combination(li, 5))
    print(sub_set(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
