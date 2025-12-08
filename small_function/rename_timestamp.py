#!python3
# -*- coding: utf-8 -*-
# author: github.com/dongyang2
import os
from datetime import datetime


def ergodic_dir(path):
    """遍历指定目录，显示目录下的所有文件或目录名
    相对于each_file_or_dir_name，一名字短了，二处理了path
    """
    s = path[-1]
    if s == '/':
        path = path[:-1]
    # print(path)
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        # print(di_or_fi)
        di_fi.append(each_path)
    return di_fi


def has_timestamp(s: str):
    """判定字符串中有时间戳。
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
        return False


def trans_timestamp(file_name, t):
    """把字符串类型的时间戳转换为字符串类型的日期"""
    ind1 = file_name.find(t)
    lt = len(t)
    t = int(t) / 1000 if lt == 13 else int(t)
    date = datetime.fromtimestamp(int(t)).strftime("%Y%m%d_%H_%M_%S")  # str
    return file_name[:ind1] + date + file_name[ind1 + lt:]


def del_prefix(name:str, prefix:str):
    print(f"{name} 将被删除前缀 => ",end="")
    ind1 = name.find(prefix)
    j = 0
    for i in range(ind1, len(name)):
        if name[i] in "1234567890":
            break
        j += 1
    name = name[ind1+j:]
    print("\t"+name)
    return name


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
            new_name = trans_timestamp(name, t)
            os.rename('%s/%s' % (path, di_or_fi), f"{path}/{new_name}.{suffix}")


def ergodic_and_rename_new(path):
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    for di_or_fi in path_dir:
        tmp_li = di_or_fi.split('.')
        name = ".".join(tmp_li[:-1])
        suffix = tmp_li[-1]
        t = has_timestamp(name)
        new_name = 0
        if "PixPin" in name:
            new_name = del_prefix(name, "PixPin")
        if "Screenshot" in name:
            new_name = del_prefix(name, "Screenshot")
        if t:
            print(f"原文件名 - {new_name} 被判定为时间戳，将转化。")
            new_name = trans_timestamp(name, t)
        if new_name != 0:
            print(f"""新文件名\t{new_name+ "." + suffix}""")
            os.rename(f"{path}/{di_or_fi}", f"{path}/{new_name}.{suffix}")


def test():
    di_or_fi = "abc1765205566008_首次36星3.jpg"
    tmp_li = di_or_fi.split('.')
    name = ".".join(tmp_li[:-1])
    suffix = tmp_li[-1]
    t = has_timestamp(name)
    print(trans_timestamp(name, t)+ "." + suffix)


def main():
    # ergodic_and_rename(os.getcwd())
    cur_path = os.getcwd()
    dirs = [cur_path]
    print(f"当前可选路径\n0. {dirs[0]}/")
    cnt = 1
    for p in ergodic_dir(cur_path):
        if os.path.isdir(p):
            dirs.append(p)
            print(f"{cnt}. {p}/")
            cnt += 1
    print("a. 手动输入完整路径(支持直接粘贴完整路径)\n请输入要进行命名清理的目录：", end="")
    user_inp1 = input().strip()
    if user_inp1 == 'a':
        print(f"你的选择是 - {user_inp1}, 请输入完整路径（例如 E:/视频/电影/）：", end="")
        user_inp2 = input().strip()
        if os.path.isdir(user_inp2):
            ergodic_and_rename_new(user_inp2 )
        else:
            print("❌ 输入的路径无效或不是目录，请重试。")
    elif user_inp1.isdigit():
        if int(user_inp1) < len(dirs):
            print(f"你的选择是 - {user_inp1}, {dirs[int(user_inp1)]}\n")
            ergodic_and_rename_new(dirs[int(user_inp1)] )
        else:
            print("❌ 无效选项，请输入上述数字或 a，或直接粘贴有效的完整路径。")
    elif os.path.isabs(user_inp1) and os.path.isdir(user_inp1):        # 用户直接粘贴了完整路径
        print(f"你的选择是 - 直接输入了完整有效的路径, {user_inp1}\n")
        ergodic_and_rename_new(user_inp1 )
    else:
        print("❌ 无效选项，请输入上述数字或 a，或直接粘贴有效的完整路径。")


if __name__ == '__main__':
    # test()
    main()
