#!python3
# -*- coding: utf-8 -*-
# 去除音乐文件的“指纹”和“抽取后缀”

import os


def get_final_part(s:str, sep):
    """经常有按sep分割后，保留最后一段和前面所有段的需求"""
    tmp = s.split(sep)
    front = sep.join(tmp[:-1])
    final = tmp[-1]
    return front, final


def ergodic_dir(path):
    """遍历指定目录，显示目录下的所有文件或目录名    """
    s = path[-1]
    if s == '/':
        path = path[:-1]
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        di_fi.append(each_path)
    return di_fi


def is_music(s: str):
    # 根据后缀判断是否是音乐文件
    music_suffix = ['mp3', 'aac', 'm4a', 'ogg', 'oga', 'opus', 'wma', 'flac', 'alac', 'ape', 'wav', 'aiff', 'amr',
                    'mid', 'midi']
    if s.lower() in music_suffix:
        return True
    else:
        return False


def regular_fil_nam(fil_nam:str, suffix, ds):
    for elem in ds:
        fil_nam = fil_nam.replace(elem,"")

    tmp = fil_nam.split("-")
    front_li = tmp[:-1]
    stamp = tmp[-1]
    if len(stamp) in stamp_ll and len(front_li) > 2:  # 至少要有歌名和作者，其余的误杀了就误杀了
        fil_nam = "-".join(front_li)

    return f"{fil_nam}.{suffix}"


def ergodic_and_regular(path, ds):
    s = path[-1]
    if s == xiegang:
        path = path[:-1]
    path_dir = os.listdir(path)
    for di_or_fi in path_dir:
        nam, suffix = get_final_part(di_or_fi, ".")
        # print(f"name=\n{nam}\n\nsuf=\n{suffix}")
        if is_music(suffix):
            new_name = regular_fil_nam(nam, suffix, ds)
            if new_name != di_or_fi:
                print(f"旧文件名 {di_or_fi}\t->\t新文件名 {new_name}")
                os.rename('%s/%s' % (path, di_or_fi), '%s/%s' % (path, new_name))


def main():
    cur_path = os.getcwd()
    dirs = [cur_path]
    print(f"当前目录下可选路径（可输入行首数字）\n\n0. {dirs[0]}/")
    cnt = 1
    for p in ergodic_dir(cur_path):
        if os.path.isdir(p):
            dirs.append(p)
            print(f"{cnt}. {p}/")
            cnt += 1
    print("a. 手动输入完整路径(支持直接粘贴完整路径)\n\n请输入要进行命名清理的目录：")
    user_inp1 = input().strip()
    if user_inp1 == 'a':
        print(f"\n你的选择是 - [{user_inp1}], 请输入完整路径（例如 E:/视频/电影/）：", end="")
        user_inp2 = input().strip()
        if os.path.isdir(user_inp2):
            ergodic_and_regular(user_inp2, dic)
        else:
            print("❌ 输入的路径无效或不是目录，请重试。")
    elif user_inp1.isdigit():
        if int(user_inp1) < len(dirs):
            print(f"\n你的选择是 - [{user_inp1}], {dirs[int(user_inp1)]}\n")
            ergodic_and_regular(dirs[int(user_inp1)], dic)
        else:
            print("❌ 无效选项，请输入上述数字或 a，或直接粘贴有效的完整路径。")
    elif os.path.isabs(user_inp1) and os.path.isdir(user_inp1):        # 用户直接粘贴了完整路径
        print(f"\n你的选择是 - [手动输入了完整有效的路径], {user_inp1}\n")
        ergodic_and_regular(user_inp1, dic)
    else:
        print("❌ 无效选项，请输入上述数字或 a，或直接粘贴有效的完整路径。")


if __name__ == '__main__':
    import platform
    os_type = platform.system()
    xiegang = "\\" if os_type == "Windows" else "/"

    dic = {"-stream-1-audio-aac"}  # 要固定删除的字符串
    stamp_ll = [8,64]  # 下载站点的资源 ID / 文件指纹，长度一般是 8 或者 64 等。
    main()
    # test()
