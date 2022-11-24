# https://leetcode-cn.com/problems/4sum/
# coding: utf-8
# Python 3
# 从给定数组中找到四个数字，他们的和等于一个指定数字
# 思路：相比于之前的《三数之和》，此题可以指定数字，因此需要做最大值和最小值优化
# 核心思路还是利用双指针进行搜索。


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


def check_same_4_num(a,b,c,d):
    """检查四个数字，任意两个相同则返回false"""
    se1 = {a,b,c,d}
    if len(se1) == 4:
        return True
    else:
        return False


def four_sum_new(nums: list, target: int):
    """之前的都是2019.12提交的，现在是2022.11.8，之前的思路都忘了。重写一次。
        先尝试使用二数之和的查找思路。
        首先背景是4个循环肯定能找到答案，现在就思考怎么把这四循环给缩短到3循环甚至1循环。
        可以得知 1  <= nums.length <= 200，那么就可以建立40000的一个一维数组，记录最内部两个循环的结果。从此可以缩短到2循环。
        为什么要用平摊的一维数组而非二维数组，是因为方便查找。
    """
    nums.sort()
    n = len(nums)

    hash_li = [float('inf') for _ in range(n*n)]
    # 先建立hash表
    for i in range(n):
        for j in range(i+1, n):
            hash_li[i*n+j] = nums[i] + nums[j]

    answer_li = []
    # 再利用2层循环解题
    for i in range(n):
        if i > 0:
            if nums[i] == nums[i-1]:  # 跳过重复数字
                continue
        for j in range(i+1, n):
            sub = target - nums[i] - nums[j]
            ms = min(hash_li[j*n+1:(j+1)*n])  # 最小边界判断。剪枝。
            if sub < ms:
                break
            if sub in hash_li[j*n+1:]:  # 找到了
                cnt = hash_li[j*n+1:].count(sub)
                last_ind = j*n+1
                for _ in range(cnt):
                    if last_ind + 1 < n*n:
                        ind = hash_li.index(sub, last_ind+1)
                        k = int(ind/n)
                        m = ind % n
                        if k > j and m > j and check_same_4_num(i, j, k, m):  # 如果k或m小于j，说明之前已经遍历过了，此处跳过
                            tmp = sorted([nums[i], nums[j], nums[k], nums[m]])
                            if tmp not in answer_li:
                                answer_li.append(tmp)
                        last_ind = ind
                    else:
                        break
    return answer_li


def four_sum_new_no_sorttmp(nums: list, target: int):
    """ 相较于four_sum_new，剔除了tmp的sort过程和check_same_4_num的过程"""

    nums.sort()
    n = len(nums)

    hash_li = [float('inf') for _ in range(n*n)]
    # 先建立hash表
    for i in range(n):
        for j in range(i+1, n):
            hash_li[i*n+j] = nums[i] + nums[j]

    answer_li = []
    # 再利用2层循环解题
    for i in range(n):
        if i > 0:
            if nums[i] == nums[i-1]:  # 跳过重复数字
                continue
        for j in range(i+1, n):
            sub = target - nums[i] - nums[j]
            ms = min(hash_li[j*n+1:(j+1)*n])  # 最小边界判断。剪枝。
            if sub < ms:
                break
            if sub in hash_li[j*n+1:]:  # 找到了
                cnt = hash_li[j*n+1:].count(sub)
                last_ind = j*n+1
                for _ in range(cnt):
                    if last_ind + 1 < n*n:
                        ind = hash_li.index(sub, last_ind+1)
                        k = int(ind/n)
                        m = ind % n
                        if j < k < m and m > j:  # 如果k或m小于j，说明之前已经遍历过了，此处跳过
                            tmp = [nums[i], nums[j], nums[k], nums[m]]
                            if tmp not in answer_li:
                                answer_li.append(tmp)
                        last_ind = ind
                    else:
                        break
    return answer_li


def four_sum_new_no_sorttmp_limit_i(nums: list, target: int):
    """ 相较于 four_sum_new_no_sorttmp， 加入一个当前i值的判断，可以预先剪枝。
        还是不行，k，m 的搜索还是需要双指针才是最快的。"""
    n = len(nums)
    if n < 4:
        return []

    nums.sort()

    hash_li = [float('inf') for _ in range(n * n)]
    # 先建立hash表
    for i in range(n):
        for j in range(i + 1, n):
            hash_li[i * n + j] = nums[i] + nums[j]

    answer_li = []
    # 再利用2层循环解题
    for i in range(n):
        if i > 0:  # 剪枝1
            if nums[i] == nums[i - 1]:  # 跳过重复数字
                continue

        if nums[i] + nums[-1]+nums[-2]+nums[-3] < target:  # 剪枝2.当前i所能加到的最大和都比target小，不用遍历j 了，跳过
            continue

        if i < n-3:
            if nums[i] + nums[i+1]+nums[i+2]+nums[i+3] > target:  # 剪枝3.当前i所能加到的最小和都比target大了，退出循环
                break
        else:
            break

        for j in range(i + 1, n):
            sub = target - nums[i] - nums[j]
            ms = min(hash_li[j * n + 1:(j + 1) * n])  # 最小边界判断。剪枝。
            if sub < ms:
                break
            if sub in hash_li[j * n + 1:]:  # 找到了
                cnt = hash_li[j * n + 1:].count(sub)
                last_ind = j * n + 1
                for _ in range(cnt):
                    if last_ind + 1 < n * n:
                        ind = hash_li.index(sub, last_ind + 1)
                        k = int(ind / n)
                        m = ind % n
                        if j < k < m and m > j:  # 如果k或m小于j，说明之前已经遍历过了，此处跳过
                            tmp = [nums[i], nums[j], nums[k], nums[m]]
                            if tmp not in answer_li:
                                answer_li.append(tmp)
                        last_ind = ind
                    else:
                        break
    return answer_li


def test1():
    nums = [2, 2, 2, 2, 2]
    target = 8
    # print(four_sum(nums, target))
    # print(four_sum_new(nums, target))
    print(four_sum_new_no_sorttmp(nums, target))


def test2():
    nums = [x for x in range(200)]
    target = 150
    # print(four_sum(nums, target))
    # print(four_sum_new(nums, target))
    print(four_sum_new_no_sorttmp_limit_i(nums, target))


def test3():
    nums = [1,0,-1,0,-2,2]
    target = 0
    print(four_sum_new(nums, target))


def main():
    test2()


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
