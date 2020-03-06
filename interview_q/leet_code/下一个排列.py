# https://leetcode-cn.com/problems/next-permutation/
# coding: utf-8
# Python 3
# 找到当前输入在全排列中的按字典序的下一个形态，如果输入是字典序最后一个形态，则输出第一个形态。如“123”的下一个排列是“132”。
# 思路：找规律，在草稿纸中写出“123456”全排列后，找当前排列与下一个排列之间有什么规律。
# 发现，从后往前找，先把最后一个数字设为对比数，然后找到第一个比对比数小的数字，此数字位置为i，他俩位置交换，然后把i后面所有的数字做成升序。
# 如果找不到比最后一个数小的，则把对比数前移一位，以此类推。
# 边界情况：空。有相同数字。

# 上面的思路错了，无法应对有相同数字的情况，下面是网上的思路
# 1.数组从后向前遍历，遇到第一个nums[i]>nums[i-1]情况，交换num[i-1]与其后最小的、比num[i-1]大的数，然后从i开始进行排序
# 2.如果不存在这种nums[i]>nums[i-1]情况，转置


def next_one(li: list):
    n = len(li)

    # 题目规定无返回
    # if n < 1:
    #     raise ValueError("输入不能是空数组")
    # elif n == 1:
    #     return li

    j = n-1
    while j != 0:
        if li[j] > li[j-1]:
            tmp = find_bigger_one_than_i(li, j-1)
            li[tmp], li[j-1] = li[j-1], li[tmp]
            sort_by_i(li, j-1)
            break
        j -= 1

    if j == 0:
        sort_by_i(li, -1)


def sort_by_i(li, i):
    # 把下标i之后的元素进行一次排序，且在当前数组中操作
    for j in range(i+1, len(li)):
        for k in range(j+1, len(li)):
            if li[j] > li[k]:
                li[k], li[j] = li[j], li[k]


def find_bigger_one_than_i(li, i):
    # 找到仅仅比下标i的数字更大的数字的下标
    tmp = i+1
    for j in range(i+1, len(li)):
        if li[i] < li[j] < li[tmp]:
            tmp = j
    return tmp


def main():
    # li = [1, 2, 8, 7, 5, 4, 6]
    # # sort_by_i(li, 2)
    # # print(li)
    # print(find_bigger_one_than_i(li, 1))

    li = [0, 2, 3, 2, 0]
    # li = [3, 2, 1]
    next_one(li)
    print(li)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
