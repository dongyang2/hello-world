# https://leetcode-cn.com/problems/first-missing-positive/
# coding: utf-8
# Python 3
# 给定一个未排序的整数数组，找出其中没有出现的最小的正整数。数组中可能有负整数。
# 限定时间复杂度应为O(n)，空间为O(1)。
#
# 思路：
# 边界条件：空数组
#
# 网上的思路：将数组本身视为哈希表，修改数组令数组下标对应的元素值等于下标+1，
# 最后扫描一遍数组，判定第一个元素值不为下标+1的下标为缺失的第一个正整数对应的下标。
# 此思路平均时间复杂度为O(n)。
# 核心部分可见《剑指offer》（何海涛）第二版P39。也可以参考我的“剑指offer文件夹”内3_1.py文件。


def missing_number_internet(li):
    n = len(li)
    if n == 0:
        return 1

    for i in range(n):
        while li[i] != i+1 and 0 < li[i] < n:  # 核心部分
            j = li[i]-1
            if li[j] != li[i]:
                li[i], li[j] = li[j], li[i]
            else:
                break

    if li[0] != 1:
        return 1

    tmp = 0
    for i in range(n):
        if li[i] != i+1:
            tmp = i+1
            break

    if tmp == 0:  # 处理后的数组正好是1~n
        return n+1
    return tmp


def main():
    li = [2, 4, 1, 0, 5]
    print(missing_number_internet(li))

    li = [3, 1, 2, 7, 6, 4, 5]
    print(missing_number_internet(li))

    li = [12, 10]
    print(missing_number_internet(li))

    li = [1, 2, 0]
    print(missing_number_internet(li))

    # 此测试用例证明了有重复元素会死循环
    li = [2, 4, 1, 2, 5]
    print(missing_number_internet(li))

    li = []
    print(missing_number_internet(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
