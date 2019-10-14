# coding: utf-8
# Python 3
# 本题主要是找到一个，而不是全部找出


def get_rep(li):
    """利用二分查找的思路找重复元素。
    元素范围1~len(li)
    时间O(nlogn)，空间是O(1)."""
    ll = len(li)
    if ll <= 0:
        raise ValueError()

    start = 0
    end = ll - 1
    while end >= start:
        middle = int((end - start) / 2) + start
        count = count_range(li, ll, start, middle)
        if end == start:
            if count > 1:
                return start
            else:
                break
        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1
    return False


def count_range(li, l, start, end):
    count = 0
    for i in range(l):
        if li[i] >= start and li[i] <= end:
            count += 1
    return count


def main():
    li = [2, 3, 1, 0, 2, 5, 3]
    print(get_rep(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
