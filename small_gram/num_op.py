def get_first_ratio(li, ratio):
    """获得一个一维列表前(只看位置不看大小)百分之几（取决于ratio）的所有元素

    :param li: 列表
    :type li: list
    :param ratio: 比例

    :return: 前百分之几的所有元素
    """
    len_li = len(li)
    result_num = round(len_li * ratio / 10)
    res_li = []
    for h, i in enumerate(li):
        if h < result_num:
            res_li.append(i)
    return res_li


def li_precision_control(li, f, is_str=False):
    """精度控制，将多维列表中所有元素都进行统一的精度控制

    :param li: 多维列表
    :type li: list
    :param f: 浮点数的控制精度
    :type f: int
    :param is_str: 列表里的单个元素是否是字符串
    :type is_str: bool

    :return: 一个统一精度的列表
    """
    if f < 0:
        print('The precision can not be negative!')
        return False

    len_li = len(li)
    i = 0
    while i < len_li:
        if type(li[i]) is list:
            li[i] = li_precision_control(li[i], f, is_str)
        else:
            if f == 0:
                if is_str is False:
                    li[i] = round(float(li[i]))
                else:
                    li[i] = str(round(float(li[i])))
            else:
                if is_str is False:
                    li[i] = round(float(li[i]), f)
                else:
                    li[i] = str(round(float(li[i]), f))
        i += 1
    return li


def get_min_from_2d_list(li):
    """获得二维列表中最小元素的值和下标

    :param li 二维数组
    :type li  list

    :return 二维列表中最小元素的值，行标，列标
    """
    m = li[0][0]
    subs1 = 0
    subs2 = 0
    for ii, i in enumerate(li):
        for jj, j in enumerate(i):
            if m > j:
                m = j
                subs1 = ii
                subs2 = jj
    return m, subs1, subs2


def get_size_top_n_li(li, n):
    """li是二维数组，本函数获得长度最大的n个一维数组"""
    len_l = len(li)
    if len_l < n:
        return False
    ll = get_li_size(li)
    i = 0
    while i < len_l:
        j = i+1
        while j < len_l:
            if ll[j] >= ll[i]:
                tmp = ll[i]
                ll[i] = ll[j]
                ll[j] = tmp
                tp = li[i]
                li[i] = li[j]
                li[j] = tp
            j += 1
        i += 1
    top_n = []
    for i, j in enumerate(li):
        if i < n:
            top_n.append(j)
    return top_n


def get_li_size(li):
    """li是二维数组"""
    len_li = []
    for i in li:
        len_li.append(len(i))
    return len_li


if __name__ == '__main__':
    # li1 = [1, 3, 45, 6, 4, 9]
    # print(get_first_ratio(li1, 7))
    #
    # li2 = [[1.236436, 2.3473724], 3.3472347, [4.324763427, 56], [3.23462, 6.346161]]
    # print(li_precision_control(li2, 0))

    c = [-10, -5, 0, 5, 3, 10, 15, -20, 25]

    # print((min(c)))
    # print(c.index(max(c)))

    li3 = [[1, 2, 3, 0.1], [0.2, 0.1, 2], [3, 0.05, 0.2]]
    # print(get_min_from_2d_list(li3))

    # 二维字典，添加字典元素
    # cc = {}
    # tm = {1: 1}
    # cc[1] = tm
    # tm = {2: 1}
    # cc[2] = tm

    # 二维字典，添加数组元素
    # cc = {}
    # tmp = []
    # edge1 = (1, 2)
    # edge2 = (1, 3)
    # edge3 = (2, 2)
    # tmp.append(2)
    # tmp.append(3)
    # cc[edge1[0]] = tmp
    # print(cc[1][1])

    # 一维字典，添加元素
    # cc = {}
    # a1 = (1, 2)
    # a2 = (3, 4)
    # cc[a1[0]] = a1[1]
    # cc[a2[0]] = a2[1]
    # print(cc)

    li4 = [[], [1, 2], [4, 5, 6], [3], [1, 1, 1, 1, 1]]
    # top3 = get_size_top_n_li(li4, 3)
    # print(top3)
