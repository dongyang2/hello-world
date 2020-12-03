#! python3
# coding: utf-8
# https://leetcode-cn.com/problems/merge-sorted-array/


def merge(nums1: list, m: int, nums2: list, n: int):
    """
    Do not return anything, modify nums1 in-place instead.*
    """
    if n > 0 and m > 0:
        i, j = 0, 0
        while i < n:
            if nums1[j] <= nums2[i]:
                if j < n + m - 1:
                    if is_pure_zero(nums1, j + 1):  # 判断j 是否已经走到纯0 的位置
                        while i < n:
                            nums1[j + 1], nums2[i] = nums2[i], nums1[j + 1]
                            j += 1
                            i += 1
                j += 1
            else:
                k = 0
                while i + k < n:
                    if nums2[i + k] <= nums1[j]:
                        k += 1
                    else:
                        break
                move(j, nums1, m + i, k)
                for o in range(k):
                    nums2[i + o], nums1[j + o] = nums1[j + o], nums2[i + o]
                # nums1[j] = nums2[i]
                i += k
                j += k
    elif m == 0 and n > 0:  # 特殊情况
        for i in range(n):
            nums1[i] = nums2[i]


def move(start, li, end, limit):
    tmp = [0 for _ in range(start, end)]
    for i in range(start, end):
        li[i], tmp[i - start] = tmp[i - start], li[i]

    for i in range(start + limit, end + limit):
        tmp[i - start - limit], li[i] = li[i], tmp[i - start - limit]


def is_pure_zero(li, start):
    is_true = True
    for i in range(start, len(li)):
        if li[i] != 0:
            is_true = False
            break
    return is_true


def main():
    nums1 = [2, 5, 6, 0, 0, 0]
    nums2 = [1, 2, 3]
    merge(nums1, 3, nums2, 3)
    print(nums1)

    nums1 = [1, 7, 8, 0, 0, 0]
    nums2 = [4, 5, 6]
    merge(nums1, 3, nums2, 3)
    print(nums1)

    nums1, m, nums2, n = [0], 0, [1], 1
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, m, nums2, n = [1, 2], 2, [0], 0
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, m, nums2, n = [0, 0], 0, [1, 2], 2
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, m, nums2, n = [-12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 1, \
                         [-49, -45, -42, -41, -40, -39, -39, -39, -38, -36, -34, -34, -33, -33, -32, -31, -29, -28, -26,
                          -26, -24, -21, -20, -20, -18, -16, -16, -14, -11, -7, -6, -5, -4, -4, -3, -3, -2, -2, -1, 0,
                          0, 0, 2, 2, 6, 7, 7, 8, 10, 10, 13, 13, 15, 15, 16, 17, 17, 19, 19, 20, 20, 20, 21, 21, 22,
                          22, 24, 24, 25, 26, 27, 29, 30, 30, 30, 35, 36, 36, 36, 37, 39, 40, 41, 42, 45, 46, 46, 46,
                          47, 48], 90
    merge(nums1, m, nums2, n)
    print(nums1)

    nums1, m, nums2, n = [-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 2], 3
    merge(nums1, m, nums2, n)
    print(nums1)


if __name__ == "__main__":
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
