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
        if i[-1] == '-':
            c_new += i[:-1]
        elif i[-1] == '.':
            c_new += i + '\n'
        else:
            c_new += i + ' '
    return c_new


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

    str3 = '''Over-fitting and generalization. In all experiments, all
clusters including any image (not only query landmarks)
from Oxford5k or Paris6k datasets are removed. We now
repeat the training using all 3D models, including those
of Oxford and Paris landmarks. In this way, we evaluate
whether the network tends to over-fit to the training data
or to generalize. The same amount of training queries is
used for a fair comparison. We observe negligible difference
in the performance of the network on Oxford and Paris
evaluation results, i.e. the difference in mAP was on average
+0.3 over all testing datasets. We conclude that the network
generalizes well and is relatively insensitive to over-fitting.
Comparison with the state of the art. We extensively
compare our results with the state-of-the-art performance
on compact image representations and on approaches that
do query expansion. The results for the fine-tuned GeM
based networks are summarized together with previously
published results in Table 5. The proposed methods outper-
form the state of the art on all datasets when the VGG net-
work architecture and initialization are used. Our method is
outperformed by the work of Gordo et al. on Paris with the
ResNet architecture, while we have the state-of-the-art score
on Oxford and we are on par on Holidays. Note, however,
that we did not perform any manual labeling or cleaning
of our training data, while in their work landmark labels
are involved. We additionally combine GeM with query
expansion and further boost the performance.'''
    print(del_enter(str3))
