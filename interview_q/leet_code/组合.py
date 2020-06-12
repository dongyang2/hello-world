# https://leetcode-cn.com/problems/combinations/
# coding: utf-8
# Python 3
# 给定两个整数 n 和 k，返回 1 ... n 中所有可能的 k 个数的组合。
#
# 思路：树的遍历。
# 边界条件：


def ergodic_tree(li, k, tmp, com):
    """力扣时间3388 ms"""
    n = len(tmp)
    if n < k:
        for i in range(len(li)):
            if n == 0:
                new_tmp = append_val(tmp, li[i])
                if len(new_tmp) == k:
                    if new_tmp not in com:
                        com.append(new_tmp)
                else:
                    ergodic_tree(pop_i(li, i), k, new_tmp, com)
            elif li[i] > tmp[-1]:
                new_tmp = append_val(tmp, li[i])
                if len(new_tmp) == k:
                    if new_tmp not in com:
                        com.append(new_tmp)
                else:
                    ergodic_tree(pop_i(li, i), k, new_tmp, com)


def erg_new(li, k, tmp, com):
    """力扣时间3404 ms"""
    n = len(tmp)
    if n == k:
        # if tmp not in com:  # 把这一行注释后，本地运行combination(31, 4)的时间由8秒变为1秒以内，力扣上却没有变化。
            com.append(tmp)

    for i in range(len(li)):
        if n > 0 and li[i] < tmp[-1]:
            continue
        elif n <= k-1:
                erg_new(pop_i(li, i), k, append_val(tmp, li[i]), com)


def erg_new_new(li, k, tmp, com):
    """不使用自己写的pop函数的同时利用了ergodic_tree中就考虑到但做得不完美的剪枝。力扣时间1232 ms"""
    n = len(tmp)
    if n == k:
        com.append(tmp)
    else:
        for i in range(len(li)):
            if n > 0 and li[i] < tmp[-1]:
                continue
            elif n <= k-1:
                    # erg_new_new(li[i+1:], k, append_val(tmp, li[i]), com)
                    erg_new_new(li[i + 1:], k, tmp+[li[i]], com)


def combination(n, k):
    if k > n or k == 0:
        return []
    li = [x+1 for x in range(n)]
    # print(li)
    com = []
    erg_new_new(li, k, [], com)
    print(com)
    # return com


def pop_i(li, i):
    n = len(li)
    return [li[x] for x in range(n) if x != i]


def append_val(li, val):
    return li+[val]


def main():
    # num = [8, 9]
    # print(pop_i(num, 1))

    combination(4, 2)
    combination(5, 2)
    # combination(31, 4)


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
