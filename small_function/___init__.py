# coding=utf-8
# 本文件夹写了一些小功能


# Windows把项目目录加入环境变量
# import os
# import sys
# now_path = os.getcwd()
# dir_path = '/'.join(now_path.split('\\')[:-1])
# sys.path.append(dir_path)


# Linux把本项目目录加入环境变量
# now_path = os.getcwd()
# dir_path = '/'.join(now_path.split('/')[:-1])
# sys.path.append(dir_path)

__all__ = [
    'all_zero',                             #
    'change_url_for_other_explorer',
    'create_pure_color_pic',
    'get_win10_lock_background_picture',
    'MD5_check',
    'py2_to_py3',                           # 把Python 2脚本转为Python 3
    'random_sort',
    'read_officeWord',
    'read_pdf',
    'rename_movie_file',
    'search_and_move_file',
    'sz_metro',
    'translate_paper'
]
