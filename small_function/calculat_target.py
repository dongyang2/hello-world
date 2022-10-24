# coding: utf-8
# 计算小目标的达成时间
# Python 3


def main():
    print('-' * 15, ' 请输入你的预期（仅支持数字） ', '-' * 15, '\n')
    target = float(input())
    print('-' * 15, ' 请输入你的当前存款（仅支持数字） ', '-' * 15, '\n')
    save_num = float(input())
    print('-' * 15, ' 请输入你的月收入（仅支持数字） ', '-' * 15, '\n')
    month_earn = float(input())
    print('-' * 15, ' 请输入你的年收益（仅支持小数） ', '-' * 15, '\n')
    rate = float(input())
    print('-' * 15, ' 请问是否需要打印每月的最终累计收入 ', '-' * 15, '\n')
    do_month_print = input()
    month_rate = rate / 12
    final_earn = save_num
    i = 1
    while final_earn < target:
        month_final_save = final_earn * month_rate + month_earn
        final_earn += month_final_save
        if do_month_print == "是" or do_month_print.lower() == "yes" or do_month_print.lower() == "y":
            print(f"\n第 {i} 月 你的总收入为 {final_earn}")
        i += 1
    year = int(i / 12)
    month = i % 12
    print(f"\n第 {i} 个月 （共{year}年{month}月） 你达成了目标！ 当前总收入为 {final_earn} ！")


if __name__ == '__main__':
    main()
