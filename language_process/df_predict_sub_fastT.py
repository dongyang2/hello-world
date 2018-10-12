import numpy as np


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


def rename(di, add):
    """返回一个和di在一个目录中的路径"""
    s_li = di.split('/')[:-1]
    return '/'.join(s_li)+add


def merge_core(li_subject, li_label):
    """
    :param li_subject: 必须是完整的二维数组，有id，subject，label
    :param li_label:   两列，第一列是id，第二列是类标
    :return: 合并的数组
    """
    # print(li_subject[:, 0])
    for k1, i in enumerate(li_subject[:, 0][1:]):  # i subject_content_id
        for k2, j in enumerate(li_label[:, 0][1:]):  # j li_label_content_id
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
                                           lr=0.325,
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
        result = handle_ft_predict_result(pre)  # 每一个句子对应一个二维数组，形如[['价格,' '0' '0.65184933']...]
        li.append(result)
    loc_predict_probability = rename(test_path, 'probability_fastT_subOnly.npy')
    np.save(loc_predict_probability, li)


def get_good_probability(test_path, threshold=0.3):
    loc_predict_probability = rename(test_path, 'probability_fastT_subOnly.npy')
    prob = np.load(loc_predict_probability)
    # print(prob)
    li_threshold = []  # 用来存储满足阈值的结果，如果在阈值以下，则取最大
    i = 0
    while i < len(prob):
        j = 0
        tmp = []
        while j < len(prob[i]):
            if float(prob[i][j][1]) > threshold:
                tmp.append(prob[i][j][0])
            j += 1
        if len(tmp) == 0:
            tmp.append(prob[i][0][0])
        li_threshold.append(tmp)
        i += 1
    # print(li_threshold)
    content_id = np.loadtxt(test_path, dtype=str, delimiter=',', usecols=[0], encoding='utf-8')[1:]
    w_path = rename(test_path, '/result/fastT_sub_th'+str(threshold) +
                               '_lr0.325'
                               # '_hs'
                               '_dim10'
                               '_epoch10'
                               '_gram(1,4)'
                               '_ngram1'
                               '_cutjb'
                               '_delStop'
                               '.csv')
    with open(w_path, 'w', encoding='utf-8') as f:
        f.write('content_id,subject,sentiment_value,sentiment_word\n')
        i = 0
        while i < len(prob):
            for j in range(len(li_threshold[i])):
                tmp_s = ','.join([content_id[i], li_threshold[i][j], '0'])
                f.write(tmp_s+',\n')
            # if i == 50:
            #     break
            i += 1


def all_zero(path):
    wno = np.loadtxt(path, delimiter=',', encoding='utf-8', dtype=str)
    len_zero = len(wno[:, 2]) - 1
    zero = np.zeros(len_zero, np.int).astype(str)
    col = np.array([wno[:, 2][0]])
    col = np.append(col, zero)

    li_0 = wno[:, 0]
    li_3 = wno[:, 3]
    li_1 = wno[:, 1]
    result = [li_0, li_1, col, li_3]
    result = np.array(result).T

    w_path = rename(path, '_00.csv')
    with open(w_path, 'w', encoding='utf-8')as f:
        for i in result:
            s = ','.join(i)
            f.write(s + '\n')


if __name__ == '__main__':
    test_fil = 'H:/DF_emotion/test_public.csv'
    train_fil = 'H:/DF_emotion/train.csv'
    train_sunOnly_jb_delStop_fil = 'H:/DF_emotion/train_sub_jieba.txt'
    test_seg_jb_delStop_fil = 'H:/DF_emotion/test_public_jb_delStop.npy'
    # print(rename(test_fil, '/result/fastTextLabel_svmSub.csv'))
    # get_predict(train_sunOnly_jb_delStop_fil, test_seg_jb_delStop_fil)
    get_good_probability(test_fil, 0.1)

    # all_zero('H:/DF_emotion/result/fastT_multiLabel_th0.3_lr0.325_hs_dim200_epoch10_gram(1,4)_ngram1_cutjb_delStop.csv')
