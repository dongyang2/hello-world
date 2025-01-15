# coding: utf-8
# Author: github.com/Dongyang2
# 用来把pdf转为txt的小程序
# pip install pdfminer3k

from io import StringIO
from io import open
import os
import re


def read_pdf_via_pdfminer(file):
    from pdfminer.pdfinterp import PDFResourceManager, process_pdf
    from pdfminer.converter import TextConverter
    from pdfminer.layout import LAParams

    rsrc = PDFResourceManager()
    ret_str = StringIO()
    lparam = LAParams()
    device = TextConverter(rsrc, ret_str, laparams=lparam)

    process_pdf(rsrc, device, file)
    device.close()

    content = ret_str.getvalue()
    ret_str.close()
    return content


def read_pdf_via_PyPDF2(file):
    import PyPDF2

    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page_num in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page_num].extract_text()
    return text


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
            if i[-1] == '-' or i[-1] == '\xad':
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
    return re.sub('(\n.{0,3}){3,}', ' ', content)


def read_pdf_real(path):
    li_xx = ['\xa0', '\xa1', '\xa2', '\xa3', '\xa4', '\xa5', '\xa6', '\xa7',
             '\xa8', '\xa9', '\xaa', '\xab', '\xac', '\xad', '\xae', '\xaf',
             '\ufffd', '\u2022']
    with open(path, mode='rb') as f:
        txt = read_pdf_via_pdfminer(f)
        txt = del_xax(txt, li_xx)
        # print(len(txt))
        abs_mode = re.compile('abstract', re.I)  # 忽略大小写
        ab_ind = abs_mode.search(txt).end()
        ref_mode = re.compile('reference', re.I)
        ref_ind = ref_mode.search(txt).start()

        need_txt = txt[ab_ind:ref_ind]
        # print(need_txt)

        txt_rf = rm_formula(need_txt)  # 移除数学公式导致的奇怪回车
        # print(txt3)
        # print(del_enter(txt_rf))
        return del_enter(txt_rf)


def del_xax(content, li):
    """删除content中所有出现在li中的元素，li若是单个字符，请以列表的形式指定。
    比如要删除content中所有的j，则li指定为['j']。"""
    lc = len(content)-1  # 指针从最后一个元素开始往前跑
    while lc != 0:
        if content[lc] in li:
            content = content[:lc]+content[lc+1:]
        lc -= 1
    return content


def references_statistic(s):
    """统计参考文献"""
    tmp_s = ""
    record = True
    dic = dict()
    for c in s:
        if c == "[":
            record = True
        elif c == "]":
            for x in tmp_s.split(","):
                if x.strip().isdigit():
                    add_elem_to_dict(dic, x.strip())

            record = False
            tmp_s = ""
        else:
            if record:
                tmp_s += c
            else:
                continue
    # print(dic)
    print(sorted(dic.items(), key=lambda a:a[1], reverse=True))


def add_elem_to_dict(d: dict, e: str):
    if e in d:
        d[e] += 1
    else:
        d[e] = 1


if __name__ == '__main__':
    import argparse
    import warnings
    # import sys
    # sys.getdefaultencoding()
    warnings.filterwarnings('ignore')

    tool_li = ["miner", "pypdf2"]

    parser = argparse.ArgumentParser(description='Read PDF')
    parser.add_argument('input', help='The input pdf file')
    parser.add_argument('--out', help=f'output file', default="E:\下载/00.txt")
    parser.add_argument('--tool', help=f'{tool_li}, which tool you choose.', default='pypdf2')
    parser.add_argument('--count_reference', help=f'Do reference count or not.', default=False)
    args = parser.parse_args()

    inp, tool, out_file, count_reference = args.input, args.tool, args.out, args.count_reference

    if os.path.exists(inp):  # 先判断是否为文件
        if tool == "miner":
            article = read_pdf_real(inp)
        elif tool == "pypdf2":
            article = read_pdf_via_PyPDF2(inp)
        else:
            article = None
            print(f"tool must in {tool_li}")

        if article:
            if count_reference:
                references_statistic(article)

            with open(out_file, "w", encoding="utf-8") as f:
                f.write(article)

    elif isinstance(inp, str):  # 不是文件就按照一段PDF样式的字符串处理输入
        out = del_enter(inp)
        print(out)
    else:
        raise IOError('Input must be a string or file path')
    # for i5 in article:
    #     print(sys.getdefaultencoding())
    #     print(i5)

    # a = 'bbbbb\xe5\x90\xb4\xe5\x85\xb6\xe6\x98\xa5aaaaa'
    # print(a.encode('latin1').decode('utf8'))

    # print('\xa9')

