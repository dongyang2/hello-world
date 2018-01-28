# 用来把pdf转为txt的小程序，因特殊字符问题，未完待续······

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import  os
import chardet


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
    # for i in li:
    #     path2 = i[:-3] + 'txt'
    #     with open(i, 'rb') as pdf_file:
    #         # print(chardet.detect(pdf_file.read()))
    #         outputString = read_pdf(pdf_file)
    #         write_txt(path2)

    str3 = '''To get intuitions on how piggybacked apps are built,
we consider samples from our ground truth and manu-
ally investigate how the piggybacked app di↵erentiates
from the original carrier app. Building on the character-
istics of piggybacking that emerge, we propose a feature
set for machine learning classification.
ComponentCapabilitydeclarations. In Android, In-
tents are the primary means for exchanging information
between components. These objects contain fields such
as the Component name to optionally indicate which app
component to whom to deliver the object, some data
(e.g., a phone number), or the action, which is a string
that specifies the generic action to perform (such as view
a contact, pick an image from the gallery, or send an
SMS). When the Android OS resolves an intent which
is not explicitly targeted to a specific component, it will
look for all registered components that have Intent fil-
ters with actions matching the intent action. Indeed, In-
tent filters are used by apps to declare their capabilities
(e.g., a Messaging app will indicate being able to pro-
cess intents with the ACTION_SEND action). Our manual
investigation into piggybacked apps has revealed that
they usually declare additional capabilities to the orig-
inal apps to support the needs of the added malicious
code. Usually, such new capabilities are used for the ac-
tivation of the malicious behaviour. For example, pig-
gybacked apps may add a new broadcast receiver with
an intent-filter that declares its intention for listening to
a specific event. Listing 1 illustrates an example of pig-
gybacked app from our ground truth. In this Manifest
file, components CAdR (line 12) is inserted and accom-
panied with the capability declaration for handling the
PACKAGE_ADDED system event (line 13).'''
    print(del_enter(str3))
