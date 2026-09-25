#!python3
# -*- coding: utf-8 -*-
# author: github.com/dongyang2
# update log:
#   2026.9.25
#       1. 制作父类和子类，方便维护，更灵活，省代码量，更简洁。若是需要子类单文件运行，到时候把母类代码复制到子类文件即可。

import os


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


class Rename:
    # def __init__(self,dic):
    #     self.dic = dic

    def ergodic_and_regular(self, path:str):
        print(f"遍历路径 {path} 且改名。")

    @staticmethod
    def get_final_part(s: str, sep):
        """经常有按sep分割后，保留最后一段和前面所有段的需求"""
        tmp = s.split(sep)
        front = sep.join(tmp[:-1])
        final = tmp[-1]
        return front, final

    def entry(self):  # 透传法
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
                self.ergodic_and_regular(user_inp2)
                # ergodic_and_regular(user_inp2, dic)
            else:
                print("❌ 输入的路径无效或不是目录，请重试。")
        elif user_inp1.isdigit():
            if int(user_inp1) < len(dirs):
                print(f"\n你的选择是 - [{user_inp1}], {dirs[int(user_inp1)]}\n")
                self.ergodic_and_regular(dirs[int(user_inp1)])
                # ergodic_and_regular(dirs[int(user_inp1)], dic)
            else:
                print("❌ 无效选项，请输入上述数字或 a，或直接粘贴有效的完整路径。")
        elif os.path.isabs(user_inp1) and os.path.isdir(user_inp1):  # 用户直接粘贴了完整路径
            print(f"\n你的选择是 - [手动输入了完整有效的路径], {user_inp1}\n")
            self.ergodic_and_regular(user_inp1)
            # ergodic_and_regular(user_inp1, dic)
        else:
            print("❌ 无效选项，请输入上述数字或 a，或直接粘贴有效的完整路径。")
