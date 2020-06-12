# https://leetcode-cn.com/problems/jump-game/
# coding: utf-8
# Python 3
# 给定一个非负整数数组，你最初位于数组的第一个位置。数组中的每个元素代表你在该位置可以跳跃的最大长度。
# 判断你是否能够到达最后一个位置。
# 没有说明空数组算True还是False
#
# 思路：树的遍历。终止条件一是跳出去了，终止条件二是遇到了0，终止条件三是跳到终点了。
# 优化方法，一是从最大的数字开始跳，二是利用动态规划思想，记住无法跳到终点的点，以实现剪枝。
# 边界条件：空数组，长度很短的数组。
#
# 我上面的思路会超时。
# 网上的思路：设定一个变量，存入能跳到的最远的距离，持续更新。
# 这个思路有个技巧，在于，每到一个位置，能不能跳到后面某个位置，只取决于当前位置的数值，
# 若能超过终点，则肯定能到达终点。从这里看，我上面的思路就是有个小错误的。


def jump(li):
    n = len(li)
    if n == 0:
        return False
    if n == 1:
        return True

    flag_li = ["ok" for _ in li]
    # arrive = []
    arrive = [False]
    ergodic_tree(li, 0, 0, n, arrive, flag_li)
    # if 1 in arrive:
    #     return True
    # else:
    #     return False
    return arrive[0]


def ergodic_tree(li, point, res, n, arr, fl):
    point = point + res
    if point == n - 1:
        # arr.append(1)
        arr[0] = True
    elif point > n:
        fl[point-res] = "-"
    else:
        now_num = li[point]
        if now_num != 0:
            pr = min(n-point-1, now_num)  # point range
            for i in range(pr):
                res = pr-i
                if fl[point+res] != "-":
                    ergodic_tree(li, point, res, n, arr, fl)

                if arr[0] is True:
                    break
            if "ok" not in fl[point+1: point+pr]:
                fl[point] = "-"
        else:
            fl[point] = "-"


def jump_internet(li):
    distance = 0
    for i in range(len(li)):
        if i > distance:
            return False
        distance = max(distance, i+li[i])
    return True


def main():
    # li = [2, 3, 1, 1, 4]
    li = [8, 2, 4, 4, 4, 9, 5, 2, 5, 8, 8, 0, 8, 6, 9, 1, 1, 6, 3, 5, 1, 2, 6, 6, 0, 4, 8, 6, 0, 3, 2, 8, 7, 6, 5, 1,
          7, 0, 3, 4, 8, 3, 5, 9, 0, 4, 0, 1, 0, 5, 9, 2, 0, 7, 0, 2, 1, 0, 8, 2, 5, 1, 2, 3, 9, 7, 4, 7, 0, 0, 1, 8,
          5, 6, 7, 5, 1, 9, 9, 3, 5, 0, 7, 5]
    # li = [3, 2, 1, 0, 4]
    print(jump_internet(li))


if __name__ == '__main__':
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    main()
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
