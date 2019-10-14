# https://leetcode-cn.com/problems/3sum-closest/
# utf-8
# Python 3


def three_sum_three_pointer(nums: list, target: int):
    nums.sort()
    ln = len(nums)
    he_min = nums[0] + nums[1] + nums[2]
    min_abs = abs(nums[0] + nums[1] + nums[2] - target)
    for i in range(ln):

        found_it = False
        for j in range(i + 1, ln):

            for k in range(j + 1, ln):
                if i == 0 and j == 1 and k == 2:
                    continue
                he = nums[k] + nums[j] + nums[i]
                now_abs = abs(he - target)
                if now_abs < min_abs:
                    min_abs = now_abs
                    he_min = he
                elif now_abs == 0:
                    return he
            if found_it is True:
                break
        if found_it is True:
            break
    return he_min


def three_sum_three_pointer_new(nums, target):
    # 还是用到了网上的双指针，上面的解法是n三方，双指针是n平方。
    nums.sort()
    ln = len(nums)
    he_min = nums[0] + nums[1] + nums[2]
    min_abs = abs(nums[0] + nums[1] + nums[2] - target)

    if min_abs == 0 or ln == 3:
        return he_min

    for i in range(ln):
        j = i + 1
        k = ln - 1
        while j < k:
            he = nums[k] + nums[j] + nums[i]
            if he > target:
                k -= 1
            elif he < target:
                j += 1
            else:
                return he
            now_abs = abs(he - target)
            if now_abs < min_abs:
                min_abs = now_abs
                he_min = he

    return he_min


def main():
    li = [1, 1, 1, 1]

    # li2 = [x for x in range(13, 100000000)]
    # li = li+li2

    print(three_sum_three_pointer_new(li, 0))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    # li1 = [-1, -1, 2]
    # li2 = [-1, 0, 1]
    # print(sorted(li1) == sorted(li2))
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
