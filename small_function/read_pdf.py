# Author: github.com/Dongyang2
# 用来把pdf转为txt的小程序，因特殊字符问题，未完待续······

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import os


def read_pdf(file):
    rsrc = PDFResourceManager()
    ret_str = StringIO()
    lparam = LAParams()
    device = TextConverter(rsrc, ret_str, laparams=lparam)

    process_pdf(rsrc, device, file)
    device.close()

    content = ret_str.getvalue()
    ret_str.close()
    return content


def write_txt(file, content):
    with open(file, 'w', encoding='utf-8') as f:
        str2 = content.split('\f')
        for i in str2:
            pre = ''
            for j in i:
                if j == '\n' and pre == '\n':
                    f.write(j)
                elif ord(j) != 8226 and j != '\n':  # 8226是一种前面有点的列表的那个黑点
                    f.write(j)
                pre = j


def each_file_or_dir_name(path):
    path_dir = os.listdir(path)
    di_fi = []
    for di_or_fi in path_dir:
        each_path = os.path.join('%s/%s' % (path, di_or_fi))
        di_fi.append(each_path)
    return di_fi


def del_question_mark(content):
    li = content.split()
    # print(li)
    s_new = ''
    j = 0
    bool_have_question_mark = 0
    while j < len(li):
        if li[j] == '[?]':
            j += 2
            bool_have_question_mark = 1
        else:
            s_new += ' ' + li[j]
            j += 1
    if bool_have_question_mark == 1:
        return s_new
    else:
        return content


def del_enter(content):
    """删除各种符号"""
    li = content.split('\n')
    c_new = ''
    for i in li:
        i = del_question_mark(i)
        # print('-'*18, i, len(i))
        if len(i) != 0:
            if i[-1] == '-':
                c_new += i[:-1]
            elif i[-1] == '.' or judge_title(i):
                c_new += i + '\n'
            else:
                c_new += i + ' '
    return c_new


def judge_title(s):
    ls = s.split(' ')
    if ls[0] is '':
        return False
    elif ls[0][0].isdigit() and ls[0][-1] is '.':
        return True
    else:
        return False


def rm_formula(content):
    import re
    return re.sub('(\n.{0,3}){3,}', ' ', content)


def read_pdf_real(path):
    with open(path, mode='rb') as f:
        txt = read_pdf(f)
        # print(txt)
        ab_ind = txt.find('Abstract')
        ref_ind = txt.rfind('References')
        need_txt = txt[ab_ind:ref_ind]

        txt_rf = rm_formula(need_txt)  # 移除数学公式导致的奇怪回车
        # print(txt3)
        # print(del_enter(txt_rf))
        return del_enter(txt_rf)


if __name__ == '__main__':
    str1 = u'D:/文档/info secu'

    # pdfFile = urlopen(path1)
    # pdfFile.close()
    # li = each_file_or_dir_name(str1)
    # for num in li:
    #     path2 = num[:-3] + 'txt'
    #     with open(num, 'rb') as pdf_file:
    #         # print(chardet.detect(pdf_file.read()))
    #         outputString = read_pdf(pdf_file)
    #         write_txt(path2)

    # str3 = ''''''
    # print(del_enter(str3))

    path1 = 'E:/下载/cvprw15.pdf'

    # print(judge_title('5. Conclusions'))
