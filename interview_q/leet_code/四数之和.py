# https://leetcode-cn.com/problems/4sum/
# coding: utf-8
# Python 3
# 从给定数组中找到四个数字，他们的和等于一个指定数字
# 思路：相比于之前的《三数之和》，此题可以指定数字，因此需要做最大值和最小值优化


def four_sum(li: list, num: int):
    li.sort()
    n = len(li)
    if n < 4:
        return []
    i = 0
    ans = []
    while i < n:
        if i > 0:
            if li[i] == li[i-1]:
                i += 1
                continue
        # 最大值优化。当前最大的四数之和比target要小，就跳过此数
        if num > li[i]+li[-1]+li[-2]+li[-3]:
            i += 1
            continue

        tmp = li[i]
        tmp_li = three_sum(li[i+1:], num - tmp)
        for j in tmp_li:
            ans.append([tmp]+j)
        i += 1

    return ans


def three_sum(nums: list, target: int):
    # 直接拿三数之和的代码，进行了小修改
    ln = len(nums)
    li = []
    for i in range(ln):
        # 最小值优化。当前最小的三数之和已经比target大了，不用找了
        if i < ln-2:
            if nums[i] + nums[i+1] + nums[i+2] > target:
                break

        if i > 0:
            if nums[i] == nums[i - 1]:  # 跳过重复的初始元素
                continue
        res1 = target - nums[i]  # 利用初始元素得到一个差，这个差就是两数之和的target
        j = i + 1
        k = ln - 1
        while j < k:
            he = nums[k] + nums[j]
            if he < res1:
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
            elif he > res1:
                k -= 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
            else:
                li.append([nums[i], nums[j], nums[k]])
                j += 1
                while j < k and nums[j] == nums[j - 1]:
                    j += 1
                k -= 1
                while j < k and nums[k] == nums[k + 1]:
                    k -= 1
    return li


def main():
    nums = [0, 0, 0, 0]
    target = 1
    print(four_sum(nums, target))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
