def get_first_ratio(li, rat, rnd=True):
    """获得一个一维列表前(只看位置不看大小)几成（百分之几十）的所有元素

    :param li:  列表
    :param rat: 比例
    :param rnd: 是否对比例的结果四舍五入，True则将根据rat得到的个数四舍五入，否则按照整数部分来切割

    :return: 前几成的所有元素
    """
    len_li = len(li)
    if rnd is True:
        result_num = round(len_li * rat / 10)
    else:
        result_num = len_li * rat / 10 * 1.0
    res_li = []
    for h, i in enumerate(li):
        if h+1 <= result_num:
            res_li.append(i)
    return res_li


def li_precision_control(li, f, is_str=False):
    """精度控制，将多维列表中所有元素都进行统一的精度控制

    :param li: 多维列表
    :type  li: list
    :param f:  浮点数的控制精度
    :type  f:  int
    :param is_str: 列表里的单个元素是否是字符串
    :type  is_str: bool

    :return: 一个统一精度的列表
    """
    if f < 0:
        print('The precision can not be negative!')
        return False

    len_li = len(li)
    i = 0
    while i < len_li:
        if isinstance(li[i], list):
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


def get_min_2d_list(li):
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
    """返回li中各元素的长度"""
    len_li = []
    for i in li:
        len_li.append(len(i))
    return len_li


def slice_li(li, rat, rnd=True, lst=True):
    """切分序列

    :param  li: 原序列
    :param rat: 比例（几成）
    :param rnd: True则将根据rat得到的个数四舍五入，否则按照整数部分来切割
    :param lst: True则返回切分后的两段，否则返回前面那段

    :return: 切分后的片段，每个片段都包装成列表
    """
    len_li = len(li)
    if rnd is True:
        result_num = round(len_li * rat / 10)
    else:
        result_num = len_li*rat/10*1.0
    prev_li = []
    lat_li = []
    for h, i in enumerate(li):
        if h+1 <= result_num:
            prev_li.append(i)
        else:
            lat_li.append(i)
    if lst is True:
        return prev_li, lat_li
    else:
        return prev_li


def get_min_li(li):
    """获得一维列表中最小元素的值和下标

    :param li: 一维列表

    :return: 最小元素的值，下标
    """
    if len(li) == 0:
        print('The list has nothing.')
        return False
    m = li[0]
    sub = 0
    for ii, i in enumerate(li):
        if m > i:
            m = i
            sub = ii
    return m, sub


def get_shi(num, shi=1):
    """算num所在的十位段，比如255在250段，136在130段
    shi=1 返回十位段
    shi=0 返回没有0的十位段，比如255是25段，3是0段，136是13段，压缩数据"""
    st = str(num)
    ls = len(st)
    if shi == 1:
        if ls == 1:
            return 0
        else:
            du = int(st[:-1])*10
            return du
    else:
        if ls == 1:
            return 0
        else:
            du = int(st[:-1])
            return du


def flatten_li(li):
    """把多维列表各元素放入一个一维列表"""
    tmp_li = []
    for i in li:
        if isinstance(i, list):
            cl = flatten_li(i)
            for j in cl:
                tmp_li.append(j)
        else:
            tmp_li.append(i)
    return tmp_li


def li_op(li, rat=-1, rnd=True, lst=True, f=-1, is_st=False, flat=False, small=-1):
    """整合对多个列表的操作，现可做1切分列表，2精度控制，3展平列表，4返回列表最小值及其下标

    :param li:    输入列表
    :param rat:   切分的比例
    :param rnd:   切分时True则将根据rat得到的个数四舍五入，否则按照整数部分来切割
    :param lst:   切分后True则返回切分后的两段，否则返回前面那段
    :param f:     精度控制
    :param is_st: 精度控制时里面的元素是否为字符串
    :param flat:  展平列表
    :param small: 返回最小值和其下标，m=1时表示li是一维数组，m=2时表示二维数组
    """
    if -1 < rat < 11:
        return slice_li(li, rat, rnd, lst)
    elif rat == -1:
        if f > -1:
            return li_precision_control(li, f, is_st)
        elif f == -1:
            if flat is True:
                return flatten_li(li)
            else:
                if small == 1:
                    return get_min_li(li)
                elif small == 2:
                    return get_min_2d_list(li)
                elif small == -1:
                    print('There is nothing can do.')
                else:
                    print('Can not get the minimum elem with this parameter!')
        else:
            print('The precision is not correct!')
    else:
        print('The cut ratio is not correct!')
    return False


def uniq(source):
    """列表内元素去重"""
    li = []
    for e in source:
        if e not in li:
            li.append(e)
    return li


def merge_core(li_subject, li_label):
    """
    :param li_subject: 必须是完整的二维数组，有id，subject，label
    :param li_label:   两列，第一列是id，第二列是类标
    :return: 合并的数组
    """
    # print(li_subject[:, 0])
    for k1, i in enumerate(li_subject[:, 0][1:]):  # i subject_content_id
        for k2, j in enumerate(li_label[:, 0][1:]):  # j li_label_content_id
            if j == i:
                li_subject[k1+1][2] = li_label[k2+1][1]
                break
    return li_subject


if __name__ == '__main__':
    li1 = [1, 3, 45, 6, 4, 9, 2]
    print(li1[-3:])
    # print(slice_li(li1, 5))
    # print(get_first_ratio(range(10), 3))

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

    # li4 = [[[], [1, 2]], [[4, 5, 6], [3]], [1, 1, 1, 1, 1]]
    # print(li_op(li4, flat=False))
    # top3 = get_size_top_n_li(li4, 3)
    # print(top3)

    # print(get_min_li([]))

    # c2 = [i+1 for i in c]
    # print(c2)

    li5 = [[1, 1], [2, 2], [2, 3], [1, 1]]
    # print(uniq(li5))

    li6 = [(18, 0.06783267), (37, 0.22998421), (62, 0.15872142), (92, 0.045642894), (113, 0.42936638)]
    # print(sorted(li6, key=lambda prob: prob[1]))
