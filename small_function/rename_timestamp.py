#!python3
# -*- coding: utf-8 -*-
# author: github.com/dongyang2
import os
from datetime import datetime


def has_timestamp(s: str):
    """判定字符串中有时间戳"""
    t = ""
    for c in s:
        if c.isdigit():
            t += c
    if len(t) == 10 or len(t) == 13:
        return t
    else:
        return False


def trans_timestamp(file_name, t, suffix):
    """把字符串类型的时间戳转换为字符串类型的日期"""
    ind1 = file_name.find(t)
    lt = len(t)
    t = int(t) / 1000 if lt == 13 else int(t)
    date = datetime.fromtimestamp(int(t)).strftime("%Y%m%d_%H_%M_%S")  # str
    return file_name[:ind1] + date + file_name[ind1 + lt:] + "." + suffix


def ergodic_and_rename(path):
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    for di_or_fi in path_dir:
        tmp_li = di_or_fi.split('.')
        name = ".".join(tmp_li[:-1])
        suffix = tmp_li[-1]
        t = has_timestamp(name)
        if t:
            print("原文件名 - " + di_or_fi)
            new_name = trans_timestamp(name, t, suffix)
            os.rename('%s/%s' % (path, di_or_fi), '%s/%s' % (path, new_name))


def test():
    di_or_fi = "abc1723876628746def.jpg"
    tmp_li = di_or_fi.split('.')
    name = ".".join(tmp_li[:-1])
    suffix = tmp_li[-1]
    t = has_timestamp(name)
    print(trans_timestamp(name, t, suffix))


def main():
    ergodic_and_rename(os.getcwd())


if __name__ == '__main__':
    # test()
    main()
