import numpy as np


def write_predict(train_path, test_path):
    """
    :param train_path:      处理好的可以用来训练的数据
    :param test_path:       处理好的用来预测的无类标数据
    """
    import fastText
    classifier = fastText.train_supervised(train_path, loss='hs', label="__label__")

    # with open(test_path, 'r', encoding='utf-8') as f:
    #     for num in f:
    #         pre = classifier.predict(num[:-1])
    #         print(pre)
    #         break

    # use numpy
    test_data = np.load(test_path)
    # di_pre = rename(test_path, '/predict.csv')  # 存类标的文件名
    # di_pre = rename(test_path, '/predict1.csv')  # 存主题的文件名
    di_pre = rename(test_path, '/predict_fastT_multiLabel.csv')

    with open(di_pre, 'w', encoding='utf-8') as f:

        # li = []
        j = 0
        for i in test_data:
            j += 1
            pre = classifier.predict(i[:-1], k=10)
            # print(pre)
            # result = pre[0][0].split('_')[-1]
            # f.write(result)
            # f.write('\n')
            # li.append(result)
            if j == 10:
                break
        # arr = np.array(li)

    # np.save(di_pre, arr)


def read(test_path):
    with open(test_path, 'r', encoding='utf-8') as f:
        li = []
        for i in f:
            li.append(i[:-1])
        arr = np.array(li)
        # print(arr)
        return arr


def rename(di, add):
    """返回一个和di在一个目录中的路径"""
    s_li = di.split('/')[:-1]
    return '/'.join(s_li)+add


def merge(label_path, sub_path, test_path):  # 把两列合在一起
    subject = np.loadtxt(sub_path, dtype=str, delimiter=',', encoding='utf-8')
    test_content_id = np.loadtxt(test_path, dtype=str, delimiter=',', usecols=0, encoding='utf-8')
    test_content_id[0] = 'content_id'
    label = np.loadtxt(label_path, dtype=str, delimiter=',', encoding='utf-8')
    label = np.array(label)

    label_title = ['sentiment_value']
    label = np.concatenate((label_title, label))
    # print(test_content_id.shape, label.shape)
    li_label = np.concatenate([test_content_id.reshape(-1, 1), label.reshape(-1, 1)], axis=1)
    result = merge_core(subject, li_label)  # shape 2631*4
    w_path = rename(test_path, '/result/fastTextLabel_svmSub.csv')
    import pandas as pd
    result_pd = pd.DataFrame(result[1:], columns=['content_id', 'subject', 'sentiment_value', 'sentiment_word'])
    # print(result.shape)
    result_pd.to_csv(w_path, index=False)


def merge_core(li_subject, li_label):
    """
    :param li_subject: 必须是完整的二维数组，有id，subject，label
    :param li_label:   两列，第一列是id，第二列是类标
    :return: 合并的数组
    """
    # print(li_subject[:, 0])
    for k1, i in enumerate(li_subject[:, 0][1:]):  # num subject_content_id
        for k2, j in enumerate(li_label[:, 0][1:]):  # each_c label_content_id
            if j == i:
                li_subject[k1+1][2] = li_label[k2+1][1]
                break
    return li_subject


def get_predict(train_path, test_path):
    """
    :param train_path:      处理好的可以用来训练的数据
    :param test_path:       处理好的用来预测的无类标数据
    """
    import fastText
    classifier = fastText.train_supervised(train_path,
                                           lr=0.3,
                                           dim=10,
                                           epoch=10,
                                           minn=1,
                                           maxn=4,
                                           wordNgrams=1,
                                           loss='hs',
                                           )
    test_data = np.load(test_path)
    li = []
    j = 0
    for i in test_data:
        j += 1
        pre = classifier.predict(i[:-1], k=10)
        # print(pre)
        result = handle_ft_predict_result(pre)  # 每一个句子对应一个二维数组，形如[['价格,' '0' '0.65184933']...]
        # if each_c == 10:
        #     break
        li.append(result)
    # print(li)
    # li_np = np.array(li)
    loc_predict_probability = rename(test_path, '/probability_fastT_multiLabel.npy')
    np.save(loc_predict_probability, li)
    # return li


def handle_ft_predict_result(li):
    """把fastText的预测结果进行处理"""
    new_li = []
    i = 0
    while i < len(li[0]):
        sub_lab = li[0][i].split('__label__')[1:]
        sub_lab.append(li[1][i])
        new_li.append(sub_lab)
        i += 1
    return new_li


def get_good_probability(test_path):
    loc_predict_probability = rename(test_path, '/probability_fastT_multiLabel.npy')
    prob = np.load(loc_predict_probability)
    # print(prob)
    li_threshold = []  # 用来存储满足阈值的结果，如果在阈值以下，则取最大
    threshold = 0.3
    i = 0
    while i < len(prob):
        j = 0
        tmp = []
        while j < len(prob[i]):
            if float(prob[i][j][2]) > threshold:
                tmp.append(prob[i][j])
            j += 1
        if len(tmp) == 0:
            tmp.append(prob[i][0])
        li_threshold.append(tmp)
        i += 1
        # if num == 20:
        #     break
    # li_np = np.array(li_threshold)
    #
    # for num in li_threshold:
    #     print(num)
    content_id = np.loadtxt(test_path, dtype=str, delimiter=',', usecols=[0], encoding='utf-8')[1:]
    w_path = rename(test_path, '/result/fastT_multiLabel_th0.3'
                               '_lr0.325'
                               '_hs'
                               '_dim200'
                               '_epoch10'
                               '_gram(1,4)'
                               '_ngram2'
                               '_cutjb'
                               '_delStop'
                               # '_30l'
                               '.csv')
    # print(li_threshold)
    with open(w_path, 'w', encoding='utf-8') as f:
        f.write('content_id,subject,sentiment_value,sentiment_word\n')
        i = 0
        while i < len(prob):
            tmp = ''
            for j in range(len(li_threshold[i])):
                sub = li_threshold[i][j][0][:-1]
                if tmp != sub:
                    tmp_s = ','.join([content_id[i], sub, li_threshold[i][j][1]])  # 这里[:-1]是为了去掉逗号
                    f.write(tmp_s+',\n')
                    tmp = sub
            i += 1
            # if num == 5:
            #     break
    # print(len(prob), len(content_id))


def change_to_30_labels(path):
    train_data = np.loadtxt(path, dtype='str', delimiter='\t', encoding='utf-8')
    w_path = rename(path, '/train_SubAndLab_jb_delStop_30l.txt')

    with open(w_path, 'w', encoding='utf-8') as f:
        tmp = []
        for i, row in enumerate(train_data[:-1]):  # [:-1]是为了去掉最后一行的回车
            li_label = row[1].split('__label__')
            tmp_s = '__label__'+li_label[1][:-1]+li_label[2]  # 这里[:-1]是为了去掉逗号
            tmp.append(tmp_s)
            if row[0] == train_data[i+1][0]:
                # print(num)
                # next_label = train_data[num+1][1].split('__label__')
                # tmp_s = '__label__'+next_label[1][:-1]+next_label[2]
                # tmp.append(tmp_s)  # 加入下个类标
                continue
            else:
                s = row[0]+'\t'
                for j in tmp:
                    s = s+j+','
                # print(s[:-1])
                f.write(s[:-1]+'\n')  # 这里[:-1]也是为了去掉逗号
                tmp = []
            # if num == 50:
            #     break
    # print(train_data.shape)


def get_good_probability_30l(test_path):
    loc_predict_probability = rename(test_path, '/probability_fastT_multiLabel.npy')
    prob = np.load(loc_predict_probability)
    # print(prob)
    li_threshold = []  # 用来存储满足阈值的结果，如果在阈值以下，则取最大
    threshold = 0.3
    i = 0
    while i < len(prob):
        j = 0
        tmp = []
        while j < len(prob[i]):
            # print(prob[num][each_c])
            if float(prob[i][j][-1]) > threshold:
                tmp.append(prob[i][j][0])
            j += 1
        if len(tmp) == 0:
            tmp.append(prob[i][0][0])
        li_threshold.append(tmp)
        i += 1

    content_id = np.loadtxt(test_path, dtype=str, delimiter=',', usecols=[0], encoding='utf-8')[1:]
    w_path = rename(test_path, '/result/fastT_multiLabel_th0.3'
                               '_lr0.3'
                               '_hs'
                               '_dim10'
                               '_epoch10'
                               '_gram(1,4)'
                               '_ngram1'
                               '_cutjb'
                               '_delStop'
                               '_30l'
                               '.csv')
    # print(li_threshold)
    with open(w_path, 'w', encoding='utf-8') as f:
        f.write('content_id,subject,sentiment_value,sentiment_word\n')
        i = 0
        while i < len(prob):
            tmp = ''
            for j in range(len(li_threshold[i])):
                # print(li_threshold[num][each_c])
                lab = split_num_from_str(li_threshold[i][j])[0][0]
                sub = li_threshold[i][j].split(lab)
                if tmp == sub:
                    continue
                else:
                    tmp_s = ','.join([content_id[i], sub[0], lab])
                    f.write(tmp_s+',\n')
                    tmp = sub
                # print(tmp_s)
            i += 1
            # if num == 100:
            #     break


def split_num_from_str(s):
    import re
    int_num = r'(\-\d+|\+\d+|\d+)'
    word = r'[a-zA-Z]+'
    return re.findall(int_num, s), re.findall(word, s)


def after_processing(path):
    return 0


if __name__ == '__main__':
    import time
    print('START------df_predict', time.ctime(), '\n')
    path1 = 'H:\DF_emotion/test_public.txt'
    train_labelFastText_file = 'H:\DF_emotion/train.txt'
    test_seg_fil = 'H:\DF_emotion/test_public1.npy'
    path4 = 'H:\DF_emotion/train2.npy'
    path5 = 'H:\DF_emotion/train2.txt'
    predict_path1 = 'H:\DF_emotion/predict1.csv'
    predict_path_label = 'H:\DF_emotion/predict.csv'
    test_file = 'H:\DF_emotion/test_public.csv'
    sub_file = 'H:/DF_emotion/subject_only_over.csv'
    train_labelAndSub_FastT_file = 'H:/DF_emotion/train_SubAndLab2.txt'  # pyltp切词
    train_lAS_fastT_jb_file = 'H:/DF_emotion/train_SubAndLab_jb.txt'  # jieba分词
    train_lAS_fastT_jb_delStop_file = 'H:/DF_emotion/train_SubAndLab_jb_delStop.txt'  # jieba分词且去除停用词
    test_seg_jieba_fil = 'H:/DF_emotion/test_public_jb.npy'
    test_seg_jieba_delStop_fil = 'H:/DF_emotion/test_public_jb_delStop.npy'
    train_lAS_fT_jb_delStop_30l_fil = 'H:/DF_emotion/train_SubAndLab_jb_delStop_30l.txt'  # 这里这个train文件是把类标作30个处理

    # read(predict_path1)
    # write_predict(train_labelAndSub_FastT_file, test_seg_fil)

    # print(rename(path5, '/train5'))

    # merge(predict_path_label, sub_file, test_file)
    # get_predict(train_lAS_fastT_jb_delStop_file, test_seg_jieba_delStop_fil)  # 使用jieba去除停用词的
    # get_predict(train_lAS_fastT_jb_file, test_seg_jieba_fil)  # 使用jieba没去除停用词的
    # get_good_probability(test_file)  # 最后调阈值时就用这个函数即可，get_predict函数保存了预测结果

    # change_to_30_labels(train_lAS_fastT_jb_delStop_file)
    get_predict(train_lAS_fT_jb_delStop_30l_fil, test_seg_jieba_delStop_fil)  # 使用当30个类标处理的train文件
    get_good_probability_30l(test_file)  # 最后调阈值时就用这个函数即可，get_predict函数保存了预测结果
    print('\nEND-----df_predict', time.ctime())
