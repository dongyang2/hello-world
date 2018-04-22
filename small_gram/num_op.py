def get_first_ratio(li, ratio):
    """获得一个一维列表前百分之几（取决于ratio）的所有元素

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


if __name__ == '__main__':
    li1 = [1, 3, 45, 6, 4, 9]
    print(get_first_ratio(li1, 7))

    li2 = [[1.236436, 2.3473724], 3.3472347, [4.324763427, 56], [3.23462, 6.346161]]
    print(li_precision_control(li2, 0))
