# -*- coding: utf-8 -*-
# author: github.com/dongyang2
# 给俩日期，得出天数差异

import os
from datetime import datetime


def main():
    date_format = "%Y%m%d"

    try:
        date1_str = input(f"请输入第一个日期 (格式：{date_format})：")
        date1 = datetime.strptime(date1_str, date_format)

        date2_str = input(f"请输入第二个日期 (格式：{date_format})：")
        date2 = datetime.strptime(date2_str, date_format)

        delta = abs((date2 - date1).days)

        print(f"\n两个日期相差：{delta} 天")

    except ValueError:
        print(f"\n输入格式错误！请按照 {date_format} 格式输入，例如 2025-10-01")


if __name__ == '__main__':
    main()


