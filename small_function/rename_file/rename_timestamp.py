#!python3
# -*- coding: utf-8 -*-
# author: github.com/dongyang2
# update log:
#   2026.9.25
#       1. 制作父类和子类，方便维护，更灵活，省代码量，更简洁。若是需要单文件运行，到时候把母类代码复制进来即可。
#       2. 由于pixpin截屏、potplayer视频截屏、obs录屏等，可能带有前缀和后缀，此文件用于清理并用标准格式化含有时间戳的文件

import os
import re
from datetime import datetime

from small_function.rename_file.rename import Rename


def has_timestamp(s: str):
    """判定字符串中有时间戳。若有，则返回时间戳，否则返回 空串
    此处限制 时间戳 上限为 4102416000（2100-01-01 00:00:00）
    """
    t = ""
    for c in s:
        if c.isdigit():
            t += c
        else:
            if len(t) == 10 and int(t) < 4102416000:
                break
            elif len(t) == 13 and int(t) < 4102416000000:
                break
            t = ""
    if len(t) == 10 or len(t) == 13:
        return t
    else:
        return ""


def date_format(s, s3, in_fmt, out_fmt):
    rest_txt = s.split(s3)[-1]  # 备注文字在日期后面，可成立
    dt2 = datetime.strptime(s3, in_fmt)
    return dt2.strftime(out_fmt)+rest_txt


def find_pat(s, pat:str):
    s3 = ""
    match = re.search(pat, s)
    if match:
        s3 = match.group()  # 已匹配字符串
    return s3


def trans_potplayer_screenshot(f_name:str,sep,last_pp_s:str):
    """potplayer截图"""
    if "_edit" in f_name:  # 既然是potplayer的截图，那这个不保留，靠后面s2的截图时间戳，也能保证唯一性和时间顺序
        f_name = f_name.replace("_edit", "")
    s1,s2 = f_name.split(sep)

    pp_pat = r'\d{8}_\d{6}\.\d{3}'  # potplayer固定时间戳格式
    s2 = date_format(s2, find_pat(s2, pp_pat), "%Y%m%d_%H%M%S.%f", "%y%m%d%H%M%S")
    if s2 == last_pp_s:  # 这里假设我一秒内在potplayer最多只能截2张图，若超过2张，则此处需要写while循环，且外层需要用集合类的数据结构
        s2 += "_1"

    return f"{s1}_ss{s2}", s2  # ss: screenshot


def trans_timestamp(file_name, t):
    """把字符串类型的时间戳转换为字符串类型的日期"""
    ind1 = file_name.find(t)
    lt = len(t)
    t = int(t) / 1000 if lt == 13 else int(t)
    date = datetime.fromtimestamp(int(t)).strftime(output_fmt)  # str
    return file_name[:ind1] + date + file_name[ind1 + lt:]


def del_prefix(name:str, prefix:str):
    # print(f"{name} 将被删除前缀 => ",end="")
    ind1 = name.find(prefix)
    j = 0
    for i in range(ind1, len(name)):
        if name[i] in "1234567890":
            break
        j += 1
    name = name[ind1+j:]
    return name


def change_date_format(s1):
    tmp_li = [
        (r'\d{4}-\d{2}-\d{2} \d{2}-\d{2}-\d{2}', "%Y-%m-%d %H-%M-%S"),  # obs录屏
        (r"\d{8}_\d{2}-\d{2}-\d{2}", "%Y%m%d_%H-%M-%S"),  # obs录屏 另一种
        (r'\d{8}-\d{6}', "%Y%m%d-%H%M%S"),  # 平板录屏
        (r"\d{4}-\d{2}-\d{2}_\d{2}-\d{2}-\d{2}", "%Y-%m-%d_%H-%M-%S"),  # pixpin老格式
        (r"\d{8}_\d{2}_\d{2}_\d{2}", "%Y%m%d_%H_%M_%S"),  # pixpin现格式（26.9.25）
    ]
    for elem in tmp_li:
        m = find_pat(s1, elem[0])
        if m:
            s1 = date_format(s1, m, elem[1], output_fmt)
            break
    return s1


def test():
    li = ["2026-08-15 21-45-49.mkv_20260816_111846.370诅咒是提瓦特的根基之一.jpg",
          "2026-08-15 21-45-49.mkv_20260816_111846.371阿坝阿坝.jpg",
          "2026-08-15 21-45-49.mp4_20260816_111846.371阿789.jpg",
          "2026-09-23 19-37-43.mkv_20260923_204219.208.png",
          "screenrecorder-20250622-124334.mp4_20260923_210500.345.jpg",
          "PixPin_20260815_193807.png"]
    for di_or_fi in li:
        tmp_li = di_or_fi.split('.')
        name = ".".join(tmp_li[:-1])
        suffix = tmp_li[-1]
        t = has_timestamp(name)
        print(trans_timestamp(name, t) + "." + suffix)
        tmp_li = [".mkv_", ".mp4_"]  # potplayer截图
        sep = ""
        for e in tmp_li:
            if e in name:
                sep = e
                break
        if sep:
            new_name,_ = trans_potplayer_screenshot(name,sep,"")
            print(new_name)


class RenameTime(Rename):
    def ergodic_and_regular(self, path):
        s = path[-1]
        if s == '/':
            path = path[:-1]
        path_dir = os.listdir(path)
        last_pp_stamp = ""  # 记录上一个文件的potplayer截图时间戳，避免一秒内截图超过1张
        for di_or_fi in path_dir:
            name, suffix = self.get_final_part(di_or_fi, ".")

            new_name = name
            prefix_li = ["PixPin", "Screenshot", "screenrecorder"]
            for p in prefix_li:
                if p in name:
                    new_name = del_prefix(new_name, p)
                    break

            tmp_li = [".mkv_", ".mp4_"]  # potplayer截图
            sep = ""
            for e in tmp_li:
                if e in name:
                    sep = e
                    break
            if sep:
                new_name, last_pp_stamp = trans_potplayer_screenshot(new_name, sep, last_pp_stamp)

            t = has_timestamp(name)
            if t:
                print(f"原文件名 - {name} 被判定为时间戳，将转化。")
                new_name = trans_timestamp(new_name, t)

            new_name = change_date_format(new_name)
            if new_name != name:
                print(f"旧文件名 {name}\t->\t新文件名 {new_name}\n")
                os.rename(f"{path}/{di_or_fi}", f"{path}/{new_name}.{suffix}")


if __name__ == '__main__':
    output_fmt = "%Y%m%d_%H%M%S"  # 指定 录屏/截屏 的真实日期的格式

    r = RenameTime()
    r.entry()
    # test()

