# https://leetcode-cn.com/problems/maximum-subarray/
# coding:utf-8
# Python 3


def max_sum(li):
    """一步走一个格子，每一步保存当前格子与之前最大子序和加和的最大的子序和"""
    ms = [li[0]]  # 保留每一步的最大子序和
    for i in range(1, len(li)):
        # 以[-2,1,-3,4,-1,2,1,-5,4]为例，当i走到5时，之前i=4拿到的就是4和-1的和，再加上当前的2，就得到最大子序和5，
        # 然后i=6时，加上了1，得到最终最大子序和6.
        ms.append(max(li[i], li[i] + ms[i - 1]))
    return max(ms)


def max_sum_quick(li):
    # 消除数组的使用，消除max的使用，消除len和range的使用
    mss = 0  # 保留每一步的最大子序和
    ms = li[0]  # 保留最大子序和
    for i in li:
        # 下式第一种思路，li[i]>=li[i]+mss.
        # 第二种思路，mss小于零，li[i]加了之后当前子序和自然会减小，所以不如不减
        if mss <= 0:
            mss = i
        else:
            mss += i
        if mss > ms:
            ms = mss
    return ms


def main():
    li = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sum_quick(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
