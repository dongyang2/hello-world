#!python3
# -*- coding: utf-8 -*-
# 统计当前原神账户里各元素角色数量的按元素的全组合（组合长度为3）结果
# 这个统计，主要是应对“幻想真境剧诗”对于各元素角色数量的限制。方便我进行合理规划。


def combination(li, per_li: list):
    """全组合"""
    n = len(li)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                per_li.append(li[i] + li[j] + li[k])


def pop_i(li, ind):
    """按li复制出一个新的数组，按下标删除元素并返回"""
    new_li = []
    for i in range(len(li)):
        if i != ind:
            new_li.append(li[i])
    return new_li


def insert_in_end(li, val):
    """按li复制出一个新的数组，在尾部添加元素并返回"""
    new_li = [x for x in li]
    new_li.append(val)
    return new_li


def main():
    li = [s for s in "火岩风水雷草冰"]
    dic1 = {"火": 10, "岩": 6, "风": 6, "水": 7, "雷": 8, "草": 5, "冰": 6}
    dic2 = {"火": 10, "岩": 8, "风": 8, "水": 7, "雷": 8, "草": 6, "冰": 7}
    dic3 = {"火": 10, "岩": 7, "风": 6, "水": 7, "雷": 8, "草": 5, "冰": 7}
    print(li)
    p_li = []
    combination(li, p_li)
    print("组合数量 ", len(p_li))

    cnt = 0
    num_limit=22
    for c in p_li:
        num = sum([dic2[k] for k in c])
        if num < num_limit:
            print(f"{c} {num}")
            cnt +=1
    print(cnt)


if __name__ == '__main__':
    main()
