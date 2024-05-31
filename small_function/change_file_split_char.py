# coding: utf-8
# Python 3

from small_gram.file_op import change_split_char


def main():
    inp = "E:/我的文档/广科大/storm考试卷子/class2/storm_class2_origin.txt"
    out = "E:/我的文档/广科大/storm考试卷子/class2/storm_class2.txt"
    new_s = "\001"

    change_split_char(inp, out, new_s)


if __name__ == '__main__':
    main()
