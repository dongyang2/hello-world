# https://leetcode-cn.com/problems/3sum/
# utf-8
# Python 3


def three_sum(nums: list):
    li = []
    ll = len(nums)
    for i in range(ll):
        tmp_li = [nums[i]]
        target = 0 - nums[i]
        ts = two_sum(nums[i + 1:], target)
        if ts is not None:
            for j in ts:
                li.append(tmp_li + j)

    same_index = []  # 存储和后面某元素相等的当前元素的下标
    new_li = []
    for i in li:
        new_li.append(sorted(i))

    lnl = len(new_li)
    for i in range(lnl):
        for j in range(i + 1, lnl):
            if new_li[i] == new_li[j]:
                # print(i, li[i], li[j])
                same_index.append(i)
                break
    # print(li, same_index)
    for i in same_index[::-1]:
        li.pop(i)
    return li


def two_sum(li: list, target: int):
    """
    :param li:     输入数组
    :param target: 指定两数之和的那个值
    """
    ll = len(li)
    all_result = []
    for i in range(ll):
        cha = target - li[i]
        tmp = li[i + 1:]
        if cha in tmp:
            all_result.append([cha, li[i]])
    if len(all_result) == 0:
        return None
    return all_result


def three_sum_two_pointer(nums: list):
    nums.sort()
    ln = len(nums)
    li = []
    for i in range(ln):
        if nums[i] > 0:  # 大于零直接跳出
            break
        if i > 0:
            if nums[i] == nums[i - 1]:  # 跳过重复的初始元素
                continue
        res1 = 0 - nums[i]  # 利用初始元素得到一个差，这个差就是两数之和的target
        for j in range(i + 1, ln):
            res2 = res1 - nums[j]
            tmp = nums[j + 1: ln]
            if res2 in tmp:  # 第一次是否在数组的验证
                need_li = [nums[i], nums[j], res2]
                if need_li not in li:  # 第二次是否在数组的验证
                    li.append(need_li)
            if nums[j] > res1:
                break
    return li


def three_sum_three_pointer(nums: list):
    # 和上面一样，只是用第三个指针替换了制作tmp数组的部分。
    # 看来双指针替换制作tmp数组，时间还是不错的，并且
    # 1 指针可以跳过重复元素。
    # 2 不需要进行两次是否在数组的验证。
    nums.sort()
    ln = len(nums)
    li = []
    for i in range(ln):
        if nums[i] > 0:  # 大于零直接跳出
            break
        if i > 0:
            if nums[i] == nums[i - 1]:  # 跳过重复的初始元素
                continue
        res1 = 0 - nums[i]  # 利用初始元素得到一个差，这个差就是两数之和的target
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
    # li = [-1, 0, 1, 2, -1, -4]
    li = [-7, -10, -1, 3, 0, -7, -9, -1, 10, 8, -6, 4, 14, -8, 9, -15, 0, -4, -5, 9, 11, 3, -5, -8, 2, -6, -14, 7, -14,
          10, 5, -6, 7, 11, 4, -7, 11, 11, 7, 7, -4, -14, -12, -13, -14, 4, -13, 1, -15, -2, -12, 11, -14, -2, 10, 3,
          -1, 11, -5, 1, -2, 7, 2, -10, -5, -8, -10, 14, 10, 13, -2, -9, 6, -7, -7, 7, 12, -5, -14, 4, 0, -11, -8, 2,
          -6, -13, 12, 0, 5, -15, 8, -12, -1, -4, -15, 2, -5, -9, -7, 12, 11, 6, 10, -6, 14, -12, 9, 3, -10, 10, -8, -2,
          6, -9, 7, 7, -7, 4, -8, 5, -4, 8, 0, 3, 11, 0, -10, -9]
    # li = [-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6]
    li = [-2,0,1,1,1,1,2]

    print(three_sum_three_pointer(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    # li1 = [-1, -1, 2]
    # li2 = [-1, 0, 1]
    # print(sorted(li1) == sorted(li2))
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
