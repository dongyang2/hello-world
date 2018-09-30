import numpy as np


def write_predict(train_path, test_path):
    """
    :param train_path:      处理好的可以用来训练的数据
    :param test_path:       处理好的用来预测的无类标数据
    """
    import fastText
    classifier = fastText.train_supervised(train_path, loss='hs', label="__label__")

    # with open(test_path, 'r', encoding='utf-8') as f:
    #     for i in f:
    #         pre = classifier.predict(i[:-1])
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
    w_path = 'H:/DF_emotion/result/fastTextLabel_svmSub.csv'
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
    classifier = fastText.train_supervised(train_path, loss='hs', label="__label__")
    test_data = np.load(test_path)
    # di_pre = rename(test_path, '/predict_fastT_multiLabel.csv')
    li = []
    j = 0
    for i in test_data:
        j += 1
        pre = classifier.predict(i[:-1], k=10)
        print(pre)
        result = handle_ft_predict_result(pre)  # 每一个句子对应一个二维数组，形如[['价格,' '0' '0.65184933']...]
        # f.write(result)
        # f.write('\n')
        if j == 10:
            break
        li.append(result)
    return li


def handle_ft_predict_result(li):
    new_li = []
    i = 0
    while i < len(li[0]):
        sub_lab = li[0][i].split('__label__')[1:]
        sub_lab.append(li[1][i])
        new_li.append(sub_lab)
        i += 1
    return np.array(new_li)


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
    train_labelAndSub_FastT_file = 'H:/DF_emotion/train_SubAndLab2.txt'

    # read(predict_path1)
    # write_predict(train_labelAndSub_FastT_file, test_seg_fil)

    # print(rename(path5, '/train5'))

    # merge(predict_path_label, sub_file, test_file)
    get_predict(train_labelAndSub_FastT_file, test_seg_fil)
    print('\nEND-----df_predict', time.ctime())
