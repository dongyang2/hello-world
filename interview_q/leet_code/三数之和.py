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
                li.append(tmp_li+j)

    same_index=[]  # 存储和后面某元素相等的当前元素的下标
    new_li = []
    for i in li:
        new_li.append(sorted(i))

    lnl = len(new_li)
    for i in range(lnl):
        for j in range(i+1, lnl):
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
            all_result.append( [cha, li[i]])
    if len(all_result) == 0:
        return None
    return all_result


def main():
    li = [-1, 0, 1, 2, -1, -4]
    print(three_sum(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    # li1 = [-1, -1, 2]
    # li2 = [-1, 0, 1]
    # print(sorted(li1) == sorted(li2))
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
