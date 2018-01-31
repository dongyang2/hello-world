def get_first_ratio(li, ratio):
    len_li = len(li)
    result_num = round(len_li*ratio/10)
    res_li = []
    for h, i in enumerate(li):
        if h < result_num:
            res_li.append(i)
    return res_li


if __name__ == '__main__':
    li1 = [1, 3, 5, 6, 4, 9]
    print(get_first_ratio(li1, 3))
