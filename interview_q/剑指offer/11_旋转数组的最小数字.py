# coding:utf-8
# Python 3
# 对一个升序数组做一次旋转，找出最小数字。
# 旋转操作就是吧数组最开始的若干个元素搬到数组的末尾。


def find_min(li):
    """书上的意思就是二分查找法。"""
    ll = len(li)
    da = 0  # 前半段数字大
    xiao = ll - 1  # 后半段数字小
    mid = 0
    while da < xiao:
        if xiao - da == 1:
            mid = xiao
            break
        mid = int((da + xiao) / 2)
        if li[mid] <= li[xiao]:  # mid在后半段
            xiao = mid
        else:  # mid在前半段
            da = mid
    return li[mid]


def main():
    tmp = [i for i in range(20, 50)]
    li = tmp[13:] + tmp[:13]
    print(li)
    print(find_min(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
