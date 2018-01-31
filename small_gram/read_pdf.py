# 用来把pdf转为txt的小程序，因特殊字符问题，未完待续······

from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import os
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

    str3 = '''Malware binary, usually with a file name extension of “.exe”
or “.bin”, is a malicious program that could harm computer
operating systems. Sometimes, it may have many variations
with highly reused basic pattern. This implies malware binaries
could be categorized into multiple families (classes), and
each variation inherits the characteristics of its own family.
Therefore, it is important to effectively detect malware binary
and recognize possible variations [1], [2].
However, this is non-trivial but challenging. A malware
binary file can be visualized to a digital gray image [3].
After visualization, the malware binary detection turns into a
multi-class image classification problem, which has been well
studied in deep learning. One can manually extract features
from malware images and feed them into classifiers such as
SVM (support vector machine) or KNN (k-nearest neighbors
algorithm) to detect malware binaries through classification.
To be more discriminative, one can utilize CNN to automati-
cally extract features as Razavian et al. did in [4] and perform
classification in an end-to-end fashion. However, most deep
CNNs are trained by properly designed balanced data [5],
[6], while malware images dataset may be highly imbalanced:
some malware has many variations while some other only has
few variations. For instance, the dataset [3] used in our paper
contains 25 classes, and some class contains more than 2000
images while some other has only 80 images or so. As a result,
even reputed pre-trained CNN models [7], [8], [9], [10] may
perform poorly in our senario. Furthermore, pre-trained CNN
models are originally designed for specific vision tasks, and
they cannot be applied to malware binary detection directly.
One may argue that data augmentation could be a possible
approach to balance the data, such as oversampling the mi-
nority classes and/or down-sampling the majority classes. It
is, however, not suitable for our problem due to two reasons.
First, down-sampling may miss many representative malware
variations. Second, simply jittering the data cannot generate
images corresponding to real malware binaries. Therefore,
we aim to investigate how to train a CNN model with the
imbalanced data in hand.
To solve the above challenges, inspired by the work in [11],
[12] which designed new loss function for CNN to improve
training performance, we propose a weighted softmax loss for
deep CNN on malware images classification. Based on the
error rate given by softmax loss, we weight misclassifications
by different values corresponding to class size. Intuitively,
misclassification of minority class should be amplified, and
that of majority class needs to be suppressed. Our weighted
loss can achieve this goal and guide the CNN to update
filters in a proper direction. We adopt a pre-trained verydeep-
19 model [8] from VGG family (Visual Geometry Group at
Oxford), and retrain it to achieve a promising result on the
malware images classification. Once the proposed loss has
been proven feasible with VGG models, it can be extended
to other models, such as GoogleNet [9] and ResNet [10]. In
a word, the contributions of this work are two-fold. First, we
propose a weighted softmax loss to address the data imbalance
issue in CNN training. Second, we apply the proposed loss to
a pre-trained CNN model and fine tune it to solve the malware
images classification problem.
The rest of paper is organized as follows. Related work is
discussed in Section II. Section III introduces the proposed
weighted softmax loss. In Section IV, we describe how to
deploy the proposed loss and fine-tune a deep CNN for
malware images classification. We evaluate our method in
Section V, and conclude this paper in Section VI.'''
    print(del_enter(str3))
