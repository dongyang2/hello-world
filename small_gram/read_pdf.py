# Author: Dongyang
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
    # for i in li:
    #     path2 = i[:-3] + 'txt'
    #     with open(i, 'rb') as pdf_file:
    #         # print(chardet.detect(pdf_file.read()))
    #         outputString = read_pdf(pdf_file)
    #         write_txt(path2)

    str3 = '''Linguistic sequence labeling, such as part-ofspeech
(POS) tagging and named entity recognition
(NER), is one of the first stages in deep language
understanding and its importance has been
well recognized in the natural language processing
community. Natural language processing (NLP)
systems, like syntactic parsing (Nivre and Scholz,
2004; McDonald et al., 2005; Koo and Collins,
2010; Ma and Zhao, 2012a; Ma and Zhao, 2012b;
Chen and Manning, 2014; Ma and Hovy, 2015)
and entity coreference resolution (Ng, 2010; Ma
et al., 2016), are becoming more sophisticated,
in part because of utilizing output information of
POS tagging or NER systems.
Most traditional high performance sequence labeling
models are linear statistical models, including
Hidden Markov Models (HMM) and Conditional
Random Fields (CRF) (Ratinov and Roth,
2009; Passos et al., 2014; Luo et al., 2015), which
rely heavily on hand-crafted features and taskspecific
resources. For example, English POS taggers
benefit from carefully designed word spelling
features; orthographic features and external resources
such as gazetteers are widely used in NER.
However, such task-specific knowledge is costly
to develop (Ma and Xia, 2014), making sequence
labeling models difficult to adapt to new tasks or
new domains.
In the past few years, non-linear neural networks
with as input distributed word representations,
also known as word embeddings, have been
broadly applied to NLP problems with great success.
Collobert et al. (2011) proposed a simple but
effective feed-forward neutral network that independently
classifies labels for each word by using
contexts within a window with fixed size. Recently,
recurrent neural networks (RNN) (Goller
and Kuchler, 1996), together with its variants such
as long-short term memory (LSTM) (Hochreiter
and Schmidhuber, 1997; Gers et al., 2000) and
gated recurrent unit (GRU) (Cho et al., 2014),
have shown great success in modeling sequential
data. Several RNN-based neural network models
have been proposed to solve sequence labeling
tasks like speech recognition (Graves et al., 2013),
POS tagging (Huang et al., 2015) and NER (Chiu
and Nichols, 2015; Hu et al., 2016), achieving
competitive performance against traditional models.
However, even systems that have utilized distributed
representations as inputs have used these
to augment, rather than replace, hand-crafted features
(e.g. word spelling and capitalization patterns).
Their performance drops rapidly when the
models solely depend on neural embeddings.
In this paper, we propose a neural network architecture
for sequence labeling. It is a truly endto-end
model requiring no task-specific resources,
feature engineering, or data pre-processing beyond
pre-trained word embeddings on unlabeled
corpora. Thus, our model can be easily applied
to a wide range of sequence labeling tasks on different
languages and domains. We first use convolutional
neural networks (CNNs) (LeCun et al.,
1989) to encode character-level information of a
word into its character-level representation. Then
we combine character- and word-level representations
and feed them into bi-directional LSTM
(BLSTM) to model context information of each
word. On top of BLSTM, we use a sequential
CRF to jointly decode labels for the whole sentence.
We evaluate our model on two linguistic
sequence labeling tasks — POS tagging on Penn
Treebank WSJ (Marcus et al., 1993), and NER
on English data from the CoNLL 2003 shared
task (Tjong Kim Sang and De Meulder, 2003).
Our end-to-end model outperforms previous stateof-the-art
systems, obtaining 97.55% accuracy for
POS tagging and 91.21% F1 for NER. The contributions
of this work are (i) proposing a novel
neural network architecture for linguistic sequence
labeling. (ii) giving empirical evaluations of this
model on benchmark data sets for two classic NLP
tasks. (iii) achieving state-of-the-art performance
with this truly end-to-end system'''
    print(del_enter(str3))
