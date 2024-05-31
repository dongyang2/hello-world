#!python3
# coding: utf-8
# https://leetcode.cn/problems/find-peak-element/
#
# 思路：要求时间复杂度是 O(log n),故只有二分法可以了
#
# 边界条件：
# 1.峰值在开始和结尾处；
# 2.只有一个或两个元素


def peek(li):  # leetcode 44 ms
    n = len(li)
    if n == 2:
        if li[0] > li[1]:
            return 0
        else:
            return 1
    start = 0
    end = n
    mid = 0
    while start < end:
        mid = int((start + end) / 2)
        if mid == 0:
            break
        if mid == n - 1:
            break
        if li[mid - 1] < li[mid]:
            if li[mid] > li[mid + 1]:  # 找到了
                break
            else:
                start = mid
        else:
            end = mid

    return mid


def test1():
    li = [11, 12, 19]
    print(peek(li))


def test2():
    li = [10]
    print(peek(li))


def main():
    # li = [1, 2, 3, 4]
    # print(peek(li))
    test1()


if __name__ == '__main__':
    from small_gram.date_op import start_time, end_time

    start_time()
    main()
    end_time()
