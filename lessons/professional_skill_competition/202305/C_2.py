# coding: utf-8
# Python 3
# 饼状图统计销量数据


import pandas as pd
from small_try.plot_try.plt_draw import draw_pie


def main():
    path = "F:/wsl_linux/download/phone_data.txt"
    data = pd.read_csv(path, ",", encoding="utf-8")
    # print(data)

    all_sales = dict()
    for _, elem in data.iterrows():
        album_name = elem[0]
        sales = elem[3]
        # print(album_name, sales)

        if album_name in all_sales:
            all_sales[album_name] += sales
        else:
            all_sales[album_name] = sales
    # print(all_sales)

    sale_sum = sum(all_sales.values())
    # print(sale_sum)
    li = [[x, all_sales[x]] for x in all_sales.keys()]
    li.sort(key=lambda x: x[1], reverse=True)
    # print(li[:5])

    dic = dict()
    for i in li[:5]:
        dic[i[0]] = round(i[1] * 1.0 / sale_sum, 4)
    print(dic)
    draw_pie(dic)


if __name__ == '__main__':
    main()
