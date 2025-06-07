# coding: utf-8
# python 3
# 画图

import sys
import os
import matplotlib.pyplot as plt


def draw_scatter(data: list, title_name: str = ""):
    """散点图"""
    plt.figure(dpi=200)
    plt.title(title_name)
    num_dots = len(data)

    plt.scatter(range(num_dots), data)
    # plt.xticks(num_dots/100)
    plt.grid(axis="y")  # 显示网格线，且只显示y轴的线
    plt.show()


def draw_plot(data: list, title_name: str = ""):
    """折线图"""
    plt.figure(dpi=150)
    plt.title(title_name)  # title() 要写在figure()后面
    num_dots = len(data)
    plt.plot(range(num_dots), data)
    plt.xticks(range(num_dots))
    # plt.grid()      # 同时显示x与y轴的网格线
    plt.grid(axis="y", linestyle="--")
    plt.show()


def draw_bar(data: dict, title_name=""):
    """柱状图"""
    font = {"family": "FangSong"}
    # 设置字体，虽然感觉只改sans-serif，但应该够了
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.title(title_name)

    plt.bar(data.keys(), data.values())
    # plt.xlabel("分段", fontdict=font)  # xlabel 指对x轴的介绍
    for key in data.keys():
        plt.text(key, data[key], data[key], ha='center', fontdict=font)

    plt.show()


def get_percent(numerator, denominator):
    answer = round(numerator * 1.0 / denominator, 10)
    return str(answer * 100) + "%"


def get_percent_num(numerator, denominator):
    return round(numerator * 1.0 / denominator, 5)


def draw_plot_diy_xy(data: list, x_tick, y_tick, title_name: str = ""):
    """折线图，定制x轴与y轴上的刻度数字"""
    plt.figure(dpi=150)
    plt.title(title_name)  # title() 要写在figure()后面
    num_dots = len(data)
    plt.plot(range(num_dots), data)
    plt.xticks(x_tick)
    plt.yticks(y_tick)
    plt.grid(linestyle="--")
    plt.show()


def draw_parallel_bar(data: list, x_tick, label, scale, title_name=""):
    """画并列柱状图
    :param data         必须是[[],[]] 这种元素为“子列表[]” 的list 的形式，“子列表[]” 里的元素就是并列在一起的柱子
    :param title_name   图片标题
    :param x_tick       x轴显示的刻度文字
    :param label        与“子列表[]” 长度必须一样，表示并列在一起的柱子中各个柱子的名字
    :param scale        对某个柱子的缩放比例。与“子列表[]” 长度必须一样
    """
    import numpy
    plt.figure(dpi=200)
    plt.title(title_name)

    n = len(label)
    if n != len(data[0]):
        print("函数输入参数label 长度与数据不一致!")
        return
    if len(scale) != len(data[0]):
        print("函数输入参数scale 长度与数据不一致!")
        return

    color_li = ["yellow", "red", "blue", "green", "purple", "brown", "white", "cyan"]
    total_width = 0.8  # 在x轴上总共占用的宽度
    lc = len(color_li)

    np_data = numpy.array(data)
    cor = range(len(np_data))  # x坐标
    width = total_width / n
    font = {"family": "Fira Code", "size": "6"}
    for i in range(n):
        x_cor = [j + width * i for j in cor]
        y_cor = np_data[:, i]
        if i == 0:
            plt.bar(x_cor, y_cor / scale[i], width=width, label=label[i], fc=color_li[i % lc], tick_label=x_tick)
        else:
            plt.bar(x_cor, y_cor / scale[i], width=width, label=label[i], fc=color_li[i % lc])
        for k in range(len(x_cor)):
            plt.text(x_cor[k], y_cor[k] / scale[i], y_cor[k], ha='center', fontdict=font)
    plt.yticks([])  # 因为使用了尺度缩放，所以不显示y轴坐标
    plt.legend()  # 显示对每个柱子的说明，就是把label中的名字与图里的柱子对应起来的小说明
    plt.show()


def draw_pie(data: dict, title_name=""):
    plt.rcParams['font.sans-serif'] = ['SimHei']  # 设置字体，虽然感觉只改sans-serif，但应该够了
    plt.title(title_name)

    li = [str(key) + ": " + str(data[key]) for key in data.keys()]
    plt.pie(data.values(), labels=li)

    plt.show()


def draw_bar_dynamic(data: dict, save_path, title_name="", resolution=(1920, 1080), dpi=200):
    """柱状图 根据输入数据动态调整 柱子宽度
    resolution 图片分辨率
    """
    font = {"family": "WenQuanYi Zen Hei"}  # Ubuntu字体 sudo apt install fonts-wqy-zenhei
    # 设置字体，虽然感觉只改sans-serif，但应该够了
    # Ubuntu字体  sudo apt install fonts-noto-cjk
    plt.rcParams['font.sans-serif'] = ['Noto Sans CJK SC', 'WenQuanYi Zen Hei']
    plt.clf()  # 清空当前画布
    plt.title(title_name)

    plt.figure(figsize=(resolution[0] / dpi, resolution[1] / dpi))

    # plt画出来的横轴长度只和最终最大数字有关 它会根据最大值进行缩放 我就需要相应地进行一个缩放
    max_num = max(data.keys())
    bars = plt.bar(data.keys(), data.values(), width=5 * max_num / dpi)

    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2., height, f'{height}', ha='center', va='bottom', fontdict=font)

    plt.savefig(save_path, dpi=dpi, bbox_inches='tight', transparent=False)


def main():
    # draw_bar({})
    # li = [x+1 for x in range(10)]
    # draw_plot(li)

    num_list = [[1.5, 10], [0.6, 20], [7.8, 30], [6, 10]]
    # print(num_list)
    # import numpy
    # nl = numpy.array(num_list)
    # print(nl[:,1])
    # x_tick = ['Monday', 'Tuesday', 'Friday', 'Sunday']
    # label = ["boy", "girl"]
    # scale = [1, 5]
    # draw_parallel_bar(num_list, x_tick, label, scale)


if __name__ == "__main__":
    import time

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    now_path = os.getcwd()
    # print(now_path)
    sys.path.append(now_path)
