#!python3
# -*- coding: utf-8 -*-
# 原神 - 提纳里 收益曲线
# 激化反应的公式很复杂，提纳里有个精通提伤的机制，导致会影响乘区的两个部分
import matplotlib.pyplot as plt
def draw_plot(data: list, title_name: str="", has_x= False):
    """折线图"""
    plt.figure(dpi=150)
    plt.title(title_name)   # title() 要写在figure()后面
    num_dots = len(data)
    plt.plot(range(num_dots), data)
    if has_x:
        plt.xticks(range(num_dots))
    plt.grid()      # 同时显示x与y轴的网格线
    plt.grid(axis="y", linestyle="--")
    plt.show()

def final_score(lv,jh_type,jt,gj,zj_lv,baojilv,baojishanghai=1.2,beizi="草伤"):
    """最终激化反应伤害，不算抗性区、防御区
    """
    lv_dic = {20: 80.6, 40: 207.4, 50: 323.6, 60: 492.9, 70: 765.6, 80: 1077.4, 90: 1446.9}  # 等级系数
    jh_dic = {"超激化": 1.15, "蔓激化": 1.25}  # 不同的激化是不同的反应倍率
    at_dic = {80:236, 90:268}  # 基础攻击
    zj_dic = {6:338.1,7:362.4,8:386.7,9:411}  # 重击倍率

    jihua_zengshang_qu = lv_dic[lv] * jh_dic[jh_type]*(1+ 5.0*jt/(jt+1200))
    basic_damage = gj*zj_dic[zj_lv] + jihua_zengshang_qu

    zengshang = 1 +  jt * 0.06
    if beizi == "草伤":
        zengshang = zengshang+0.466
    baoji = baojilv*(1+baojishanghai)
    return basic_damage*zengshang*baoji


def main():
    lv = 80
    zhongji_lv = 8
    jihua = "蔓激化"

    gj_curve = []
    for gj in range(20):
        gj_curve.append(final_score(lv, jihua, 50, gj*50, zhongji_lv, 0.6))
    # draw_plot(gj_curve)

    jt_curve = []
    jt = 50
    for i in range(50):
        jt += i*20
        jt_curve.append(final_score(lv, jihua, jt, 600, zhongji_lv, 0.6))
    draw_plot(jt_curve)


def test():
    """看下精通加成区到底是啥曲线"""
    jt = 0
    li= []
    for i in range(1000):
        jt += i*1
        li.append(1+ 5.0*jt/(jt+1200))
    draw_plot(li)  # 曲线。好像在340的时候就斜率就下降了

    # curve_ratio_li = []
    # last_one = 1
    # for i in range(1, 1000):
    #     this_one = 1 + 5.0 * i / (i + 1200)
    #     curve_ratio_li.append(this_one*1.0/last_one)
    #     last_one = this_one
    # for j in curve_ratio_li:
    #     print(j)




if __name__ == '__main__':
    # main()
    test()