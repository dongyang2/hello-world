# coding: utf-8
# 生成英文名，包含姓氏和中间名缩写
from small_gram.file_op import read_file, write_file


def make_str_like_name(s: str):
    """首字母大写，其余小写"""
    return s[0].upper()+s[1:].lower()


def main():
    name_file = "E:/Download/tmp/英文名字.txt"
    family_name_file = "E:/Download/tmp/英文姓氏.txt"

    name_li = read_file(name_file)
    fname_li = read_file(family_name_file)

    mid_name_li = ['', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    li = []
    for i in name_li:
        for j in mid_name_li:
            for k in fname_li:
                if j == "":
                    li.append(make_str_like_name(i) + " " + make_str_like_name(k))
                else:
                    li.append(make_str_like_name(i) + " " + make_str_like_name(j) + " " + make_str_like_name(k))
    write_file(li, "E:/Download/tmp/full_name.txt", "1D list")


if __name__ == "__main__":
    main()
