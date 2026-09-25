#!python3
# -*- coding: utf-8 -*-
# 去除音乐文件的“指纹”和“抽取后缀”

import os

from small_function.rename_file.rename import Rename


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


class RenameMusic(Rename):
    def ergodic_and_regular(self, path):
        s = path[-1]
        if s == xiegang:
            path = path[:-1]
        path_dir = os.listdir(path)
        for di_or_fi in path_dir:
            nam, suffix = self.get_final_part(di_or_fi, ".")
            # print(f"name=\n{nam}\n\nsuf=\n{suffix}")
            if is_music(suffix):
                new_name = regular_fil_nam(nam, suffix, dic)
                if new_name != di_or_fi:
                    print(f"旧文件名 {di_or_fi}\t->\t新文件名 {new_name}")
                    os.rename('%s/%s' % (path, di_or_fi), '%s/%s' % (path, new_name))


if __name__ == '__main__':
    import platform
    os_type = platform.system()
    xiegang = "\\" if os_type == "Windows" else "/"

    dic = {"-stream-1-audio-aac"}  # 要固定删除的字符串
    stamp_ll = [8,64]  # 下载站点的资源 ID / 文件指纹，长度一般是 8 或者 64 等。
    r1 = RenameMusic()
    r1.entry()
    # test()
