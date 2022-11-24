# coding: utf-8
# Python 3


def walk(n: int, li: list):
    """从前往后推，仅维护第i个下标的最长序列，后面的数字访问前面的所有下标时，仅对第i个下标保存的最长序列的最后一个数字负责"""
    saved_past_li = []
    # final_max_len = 1
    for i in range(0, n):
        cur_max_li = [li[i]]  # 存储当前下标能够到的最长序列
        cur_max = 1  # 当前数字所能带来的基本序列长度
        for j in range(i):  # 访问前面下标保存的所有最长序列
            if li[i] > saved_past_li[j][-1]:
                if len(saved_past_li[j]) + 1 > cur_max:  # 保留"前面有一个序列加本数字后"序列长度最大的那一个序列
                    cur_max_li = saved_past_li[j] + [li[i]]
                    cur_max = len(saved_past_li[j]) + 1
        saved_past_li.append(cur_max_li)
    l = max([len(s) for s in saved_past_li])
    # print(saved_past_li)
    print(l)


def main():
    n = input()
    s = input()
    li = [int(x) for x in s.strip().split(" ")]
    walk(int(n), li)


if __name__ == '__main__':
    main()
