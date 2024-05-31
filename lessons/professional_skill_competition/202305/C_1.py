# coding: utf-8
# Python 3
# 柱状图统计销量数据


import pandas as pd
from small_try.plot_try.plt_draw import draw_bar


def main():
    path = "F:/wsl_linux/download/phone_data.txt"
    data = pd.read_csv(path, ",", encoding="utf-8")
    # print(data)
    all_sales = dict()
    for _, elem in data.iterrows():
        album_name = elem[2]
        sales = elem[3]
        # print(album_name, sales)

        if album_name in all_sales:
            all_sales[album_name] += sales
        else:
            all_sales[album_name] = sales
    # print(all_sales)

    draw_bar(all_sales)


if __name__ == '__main__':
    main()
