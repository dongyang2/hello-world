import sys

import copy


# 每个物品都有【进，不进】两个可选状态，转化成二叉树的遍历
def ergodic_tree(goods_li: list, buy_it: bool, i: int, rest_money: int, rest_room: int, buy_li: list, sat_end: int,
                 satisfy_li: list):  # 这种方法确实可以的到正确答案，但在牛客网超时超内存
    if rest_room == 0:
        return

    if i == len(goods_li):
        satisfy_li.append(sat_end)
        return

    if buy_it:
        elem = goods_li[i]
        money = elem[0]
        cur_w = elem[1]

        if money > rest_money:
            satisfy_li.append(sat_end)
            return
        depend = elem[2]
        if depend == 0:
            sat_end += money * cur_w
        else:  # 有依赖
            if depend in buy_li:  # 依赖已经进了，可以让当前物品进入
                sat_end += money * cur_w
            else:
                if rest_room > 1:  # 依赖没进，这次进俩
                    depend_elem = goods_li[depend]
                    depend_money = depend_elem[0]
                    if depend_money + money > rest_money:
                        satisfy_li.append(sat_end)
                        return
                    depend_w = depend_elem[1]
                    sat_end += depend_w * depend_money + money * cur_w
                    buy_li.append(depend)
                    rest_room -= 1
                    rest_money -= depend_money
                else:  # 包的空间不够，当前物品不进入
                    satisfy_li.append(sat_end)
                    return

        buy_li.append(i)
        rest_money -= money
        rest_room -= 1

    ergodic_tree(goods_li, True, i + 1, rest_money, rest_room, copy.deepcopy(buy_li), sat_end, satisfy_li)
    ergodic_tree(goods_li, False, i + 1, rest_money, rest_room, copy.deepcopy(buy_li), sat_end, satisfy_li)


class Node:
    def __init__(self, ind, money, weight):
        self.ind = ind
        self.money = money
        self.w = weight
        self.kids = []

    def add_kid(self, elem):
        self.kids.append(elem)

    def get_kids(self):
        return self.kids


# 相较于ergodic_tree，通过控制树高缩短时间复杂度。
# 即每层只遍历主件，因为题目限定主件最多2个附件，多个附件仅是附带情况，每层节点数为4，但树高变小
def ergodic_tree_less_height(goods_li: list, buy_it: int, i: int, rest_money: int, rest_room: int,
                             sat_end: int, satisfy_li: list):  # 这个方法也能行，依然超内存
    if rest_room == 0:
        return

    node = goods_li[i]
    money = node.money
    cur_w = node.w
    if buy_it == 0:  # 放入主件
        if money > rest_money:
            satisfy_li.append(sat_end)
            return
        sat_end += cur_w * money
        rest_room -= 1
        rest_money -= money
    elif buy_it > 0:
        kid0 = node.kids[0]
        k0_money = kid0[0]
        k0_w = kid0[1]
        if buy_it == 1 and rest_room > 1 and money + k0_money <= rest_money:  # 放入单个主件和单个附件
            sat_end += cur_w * money + k0_w * k0_money
            rest_money -= k0_money + money
            rest_room -= 2
        elif buy_it == 2 and rest_room > 2:  # 放入单个主件和两个附件
            k1_money = node.kids[1][0]
            if money + k0_money + k1_money <= rest_money:
                sat_end += cur_w * money + k0_w * k0_money + node.kids[1][1] * k1_money
                rest_money -= k0_money + k1_money + money
                rest_room -= 3
            else:
                satisfy_li.append(sat_end)
                return
        elif buy_it == 3 and rest_room > 1:  # 放入单个主件和单个附件的第二种情况
            k1_money = node.kids[1][0]
            if money + k1_money <= rest_money:
                sat_end += cur_w * money + node.kids[1][1] * k1_money
                rest_money -= k1_money + money
                rest_room -= 2
            else:
                satisfy_li.append(sat_end)
                return
        else:
            satisfy_li.append(sat_end)
            return

    if i == len(goods_li) - 1:
        satisfy_li.append(sat_end)
        return

    ergodic_tree_less_height(goods_li, -1, i + 1, rest_money, rest_room, sat_end, satisfy_li)
    ergodic_tree_less_height(goods_li, 0, i + 1, rest_money, rest_room, sat_end, satisfy_li)
    if len(goods_li[i + 1].kids) == 1:
        ergodic_tree_less_height(goods_li, 1, i + 1, rest_money, rest_room, sat_end, satisfy_li)
    elif len(goods_li[i + 1].kids) == 2:
        ergodic_tree_less_height(goods_li, 1, i + 1, rest_money, rest_room, sat_end, satisfy_li)
        ergodic_tree_less_height(goods_li, 2, i + 1, rest_money, rest_room, sat_end, satisfy_li)
        ergodic_tree_less_height(goods_li, 3, i + 1, rest_money, rest_room, sat_end, satisfy_li)


# 相较于 ergodic_tree_less_height，通过删除 satisfy_li 组件来实现节约内存
def ergodic_tree_less_height_less_room(goods_li: list, buy_it: int, i: int, rest_money: int, rest_room: int,
                                       sat_end: int):
    if rest_room == 0:
        return sat_end

    node = goods_li[i]
    money = node.money
    cur_w = node.w
    if buy_it == 0:  # 放入主件
        if money > rest_money:
            return sat_end
        sat_end += cur_w * money
        rest_room -= 1
        rest_money -= money
    elif buy_it > 0:
        kid0 = node.kids[0]
        k0_money = kid0[0]
        k0_w = kid0[1]
        if buy_it == 1 and rest_room > 1 and money + k0_money <= rest_money:  # 放入单个主件和单个附件
            sat_end += cur_w * money + k0_w * k0_money
            rest_money -= k0_money + money
            rest_room -= 2
        elif buy_it == 2 and rest_room > 2:  # 放入单个主件和两个附件
            k1_money = node.kids[1][0]
            if money + k0_money + k1_money <= rest_money:
                sat_end += cur_w * money + k0_w * k0_money + node.kids[1][1] * k1_money
                rest_money -= k0_money + k1_money + money
                rest_room -= 3
            else:
                return sat_end

        elif buy_it == 3 and rest_room > 1:  # 放入单个主件和单个附件的第二种情况
            k1_money = node.kids[1][0]
            if money + k1_money <= rest_money:
                sat_end += cur_w * money + node.kids[1][1] * k1_money
                rest_money -= k1_money + money
                rest_room -= 2
            else:
                return sat_end

        else:
            return sat_end

    if i == len(goods_li) - 1:
        return sat_end

    if len(goods_li[i + 1].kids) == 0:
        return max(ergodic_tree_less_height_less_room(goods_li, -1, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 0, i + 1, rest_money, rest_room, sat_end))
    elif len(goods_li[i + 1].kids) == 1:
        return max(ergodic_tree_less_height_less_room(goods_li, -1, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 0, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 1, i + 1, rest_money, rest_room, sat_end))
    elif len(goods_li[i + 1].kids) == 2:
        return max(ergodic_tree_less_height_less_room(goods_li, -1, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 0, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 1, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 2, i + 1, rest_money, rest_room, sat_end),
                   ergodic_tree_less_height_less_room(goods_li, 3, i + 1, rest_money, rest_room, sat_end))


def ergodic_tree_less_height_less_room_no_recursion(goods_li: list, rest_money: int, rest_room: int):
    """我发现每一步都是可计算的，完全没必要递归，直接迭代计算就行，只差一个存结果的数组了"""




def main():
    from small_gram.date_op import start_time, end_time

    money, room = input().strip().split(" ")
    li = [[0, 0, 0]]
    for line in sys.stdin:
        li.append([int(x) for x in line.strip().split(" ")])
    dic = dict()
    for i, elem in enumerate(li):
        dep = elem[2]
        if dep == 0:
            node = Node(i, elem[0], elem[1])
            dic[i] = node
    for elem in li:
        dep = elem[2]
        if dep != 0:
            node = dic[dep]
            node.kids.append(elem)
    sat_li = []
    inpli = [x for x in dic.values()]

    start_time()

    print(ergodic_tree_less_height_less_room(inpli, -1, 0, int(money), int(room), 0))
    end_time()


if __name__ == '__main__':
    main()
