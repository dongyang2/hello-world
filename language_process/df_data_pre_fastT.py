import time

import numpy as np
import jieba

from sklearn.model_selection import train_test_split


def read_scv(path):
    import csv  # 这个包读文件好像会改文件内容，我了个暴脾气
    csv_reader = csv.reader(open(path, encoding='utf-8'))
    li = []
    i = 0
    for row in csv_reader:
        i += 1
        if i != 1:
            # print(row)
            li.append(row)
    arr = np.array(li)
    data = np.delete(arr, [0, 4], axis=1)  # 三列——内容，主题，类标
    # label = np.delete(arr, [0, 1, 2, 4], axis=1)  # 类标
    # label = np.delete(arr, [0, 1, 2, 4], axis=1).astype(np.int32)  # 类标
    # print(data)
    # print(label)
    return data


def read(path, fl='train', sep=True):
    if fl == 'train':
        with open(path, 'r', encoding='utf-8') as f:
            li = []
            j = 0
            for i in f:
                j += 1
                if j != 1:
                    # print(num)
                    li.append(i[:-1].split(','))  # 读scv文件标准切法
            # print(li)
            arr = np.array(li)
            if sep is True:
                data = np.delete(arr, [0, 3], axis=1)  # 三列:内容，主题，情感词
                label = np.delete(arr, [0, 1, 2, 4], axis=1).astype(np.int32)  # 类标
                # print(data)
                # print(label)
                return data, label
            else:
                return arr

    elif fl == 'test':
        with open(path, 'r', encoding='utf-8') as f:
            li = []
            j = 0
            for i in f:
                j += 1
                if j != 1:
                    # print(num)
                    li.append(i[:-1].split(',')[1])
            # print(li)
            arr = np.array(li)

            return arr

    else:
        print('Flag传错啦')
        return False


def word_seg(sen):
    import os
    ltp_data_dir = 'H:\ltp_data_v3.4.0'  # ltp模型目录的路径
    cws_model_path = os.path.join(ltp_data_dir, 'cws.model')  # 分词模型路径，模型名称为`cws.model`

    from pyltp import Segmentor
    segmentor = Segmentor()  # 初始化实例
    segmentor.load(cws_model_path)  # 加载模型
    words = segmentor.segment(sen)  # 分词
    # print('\t'.join(words))
    segmentor.release()  # 释放模型
    return ' '.join(words)


def write(path):  # 按照fastText的格式改写原数据,写预处理的训练数据到文件
    x, y = read(path)
    content = x[:, 0]  # 内容
    label = y[:, 0]

    # print(content)
    # print(label)
    x_train, x_test, y_train, y_test = train_test_split(
        content, label, test_size=0.2, random_state=666)

    import copy
    s_di = copy.deepcopy(path)
    di = s_di.split('/')[:-1][0]  # 获得绝对路径的当前目录
    di_train = di+'/train.txt'
    di_test = di + '/test.txt'
    # print(di)

    with open(di_train, 'w', encoding='utf-8') as f_t:
        for j, i in enumerate(x_train):
            # print(word_seg(num))
            # print(type(word_seg(num)))
            s = word_seg(i)+'\t__label__'+str(y_train[j])  # 注意这里__label__前面要加至少一个空格，否则fastText读不出标签
            # print(s)
            f_t.write(s)
            f_t.write('\n')
            # break

    with open(di_test, 'w', encoding='utf-8') as f_t:
        for j, i in enumerate(x_test):
            s = word_seg(i)+'\t__label__'+str(y_test[j])
            f_t.write(s)
            f_t.write('\n')
            # break


def write_test(path):  # 几十分钟
    data = read(path, 'test')

    di = path.split('/')[:-1][0]
    di_test = di + '/test_public.txt'

    # np写二进制文件
    # di_test = di + '/test_public0'
    # np.save(di_test, data)

    with open(di_test, 'w', encoding='utf-8') as f_t:
        for i in data:
            f_t.write(word_seg(i))
            f_t.write('\n')
            # break


def write_test_np(path, cut='jieba'):  # 十分钟
    test_data = np.loadtxt(path, delimiter=',', usecols=[1], encoding='utf-8', dtype=str)
    # print(test_data[1:])

    # di = path.split('/')[:-1][0]
    # di_test = di + '/test_public1'

    li = []
    if cut == 'pyltp':
        di_test = rename(path, '/test_public1')
        for i in test_data[1:]:
            li.append(word_seg(i))
    elif cut == 'jieba':
        di_test = rename(path, '/test_public_jb_delStop')
        for i in test_data[1:]:
            li.append(clean_str(i))

    np.save(di_test, li)


def write_train_np(path):  # 40分钟
    """对原始训练数据不分训练和验证，直接切词存入"""
    d = read(path, sep=False)
    # print(d)

    # di = path.split('/')[:-1][0]
    # di_tr = di + '/train2.txt'  # 主题保存名称
    # di_tr = di + '/train3.txt'  # 类标保存名称
    di_tr = rename(path, '/train3.txt')

    with open(di_tr, 'w', encoding='utf-8') as f_t:
        k = 0
        while k < len(d):
            # 留类标
            # s = word_seg(d[elem][1])+'\t__label__'+str(d[elem][3])

            # 留主题
            s = word_seg(d[k][1])+'\t__label__'+str(d[k][2])
            # print(s)
            f_t.write(s)
            f_t.write('\n')
            k += 1


def rename(di, add):
    """返回一个和di在一个目录中的路径"""
    s_li = di.split('/')[:-1]
    return '/'.join(s_li)+add


def clean_str(stri, stop=True):
    import re
    stri = re.sub(u'[\s]+|[^\u4e00-\u9fa5A-Za-z0-9]+|<br />', '', stri)
    cut_str = jieba.cut(stri.strip())
    if stop is True:
        list_str = [word for word in cut_str if word not in stop_word]
        stri = ' '.join(list_str)
    else:
        stri = ' '.join(cut_str)
    return stri


def write_train_sub_and_label(train_path, cut='pyltp'):  # 笔记本ltp 38min,服务器ltp 12min
    """把数据处理成可放入fastText的格式，既写入主题也写入情感分类

    :param train_path: 训练文件的路径
    :param cut:        切词方法。jieba或者pyltp二选一
    """
    data_train = read_scv(train_path)
    # print(data_train)

    if cut == 'jieba':
        file_name = '/train_SubAndLab_jb_delStop.txt'
    elif cut == 'pyltp':
        file_name = '/train_SubAndLab_ltp.txt'
    di_tr = rename(train_path, file_name)  # 写到和train文件一个目录下
    with open(di_tr, 'w', encoding='utf-8') as f_t:
        k = 0
        while k < len(data_train):
            s = ''
            if cut == 'pyltp':
                s = word_seg(data_train[k][0])+'\t__label__'+str(data_train[k][1])+',__label__'+str(data_train[k][2])
            elif cut == 'jieba':
                s = clean_str(data_train[k][0])+'\t__label__'+str(data_train[k][1])+',__label__'+str(data_train[k][2])
            else:
                print('No such cut function')
                break
            f_t.write(s)
            f_t.write('\n')
            k += 1


def write_train_sub_or_label(train_path, cut='jieba', c='sub'):
    """将数据处理成可放入fastText的格式，只写入主题（或情感分类）

    :param train_path:  训练文件的路径
    :param cut:         切词方法。jieba或者pyltp二选一
    :param c:           只进行主题或者类标的多分类。sub或者lab二选一。
    """
    data_train = read_scv(train_path)
    # print(data_train)

    file_name = '/train_'+c+'_'+cut+'.txt'
    di_tr = rename(train_path, file_name)  # 写到和train文件一个目录下
    with open(di_tr, 'w', encoding='utf-8') as f_t:
        k = 0
        while k < len(data_train):
            s = ''
            if cut == 'pyltp':
                if c == 'sub':
                    s = word_seg(data_train[k][0])+'\t__label__'+str(data_train[k][1])
                else:
                    s = word_seg(data_train[k][0])+'\t__label__'+str(data_train[k][2])
            elif cut == 'jieba':  # 默认去除停用词，具体可以看clean_str函数。去除停用词在fastText中表现更好
                if c == 'sub':
                    s = clean_str(data_train[k][0])+'\t__label__'+str(data_train[k][1])
                else:
                    s = clean_str(data_train[k][0])+'\t__label__'+str(data_train[k][2])
            else:
                print('No such cut function')
                break
            f_t.write(s)
            f_t.write('\n')
            k += 1


if __name__ == '__main__':
    print('START-----df_data_pre ', time.ctime())
    train_fil = 'H:\DF_emotion/train.csv'
    test_fil = 'H:\DF_emotion/test_public.csv'
    li_test = ['四驱价格貌似挺高的，高的可以看齐XC60了，看实车前脸有点违和感。不过大众的车应该不会差。',
               '优惠可以了！购进吧！买了不会后悔的！时间可鉴！',
               '山东威海全系这才优惠3000，MD']
    # read(path1)

    # write(path1)
    # write_test(path2)
    # write_test_np(path2)
    # write_train_np(path1)
    stop_word = []
    stop_words_path = './stop.txt'

    with open(stop_words_path, encoding='utf8') as f:
        for line in f.readlines():
            stop_word.append(line.strip())
    stop_word.append(' ')
    # write_train_sub_and_label(train_fil, cut='jieba')
    # write_test_np(test_fil)
    # print(np.load('H:\DF_emotion/test_public_jb.npy'))
    # for sentence in li_test:
    #     print(clean_str(sentence))

    write_train_sub_or_label(train_fil)
    print('END-----df_data_pre ', time.ctime())
