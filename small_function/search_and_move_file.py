# coding: utf-8
# 按名称搜索文件
import argparse
import os
import shutil

from small_gram import search_by_name, mkdir

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='按名称搜索并移动文件')

    parser.add_argument('from_dir', metavar='search dir', help='The input must be an exist directory.')
    parser.add_argument('key', metavar='search key', help='The input must be a string.')
    parser.add_argument('to_dir', metavar='output dir', help='Output directory.')
    args = parser.parse_args()

    search_dir = args.from_dir
    out_dir = args.to_dir
    key = args.key

    if os.path.isdir(search_dir) and os.path.isdir(out_dir) and type(key) is str:
        pass
    else:
        assert IOError('Input is not valid, please use -h to get more information.')

    s_li = search_by_name(search_dir, key)
    out_dir = out_dir + key + '/'
    mkdir(out_dir)
    for fil in s_li:
        shutil.copy(fil, out_dir)
