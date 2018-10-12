# Latent Dirichlet Allocation
from gensim.test.utils import common_texts
from gensim.corpora.dictionary import Dictionary
from gensim.models import LdaModel
import numpy as np


def train_exp():
    print(common_texts)
    common_dictionary = Dictionary(common_texts)
    print(common_dictionary)
    common_corpus = [common_dictionary.doc2bow(text) for text in common_texts]
    # print(common_corpus)
    lda = LdaModel(common_corpus, num_topics=10)
    return lda


def use_model_exp(model):
    common_dictionary = Dictionary(common_texts)
    other_texts = [
        ['computer', 'time', 'graph'],
        ['survey', 'response', 'eps'],
        ['human', 'system', 'computer']
    ]
    other_corpus = [common_dictionary.doc2bow(text) for text in other_texts]
    unseen_doc = other_corpus[0]
    vector = model[unseen_doc]  # get topic probability distribution for a document
    return vector


def incrementally_train_exp(model, add_corpus, elem):
    model.update(add_corpus)
    vector = model[elem]
    return vector


def sav_lda_vec(path, sav_place):  # train 16s, test 4s
    content = np.load(path)
    con_dictionary = Dictionary(content)
    common_corpus = [con_dictionary.doc2bow(text) for text in content]
    lda = LdaModel(common_corpus, num_topics=120)
    li_vec = [lda[i] for i in common_corpus]  # 这里得到一个向量，格式是 [主题名：是该主题的概率]
    np.save(sav_place, li_vec)


def val(train_path, test_path):
    # content = np.loadtxt(path, delimiter=',', usecols=[1], encoding='utf-8', dtype=str)[1:]
    train_vec = np.load(train_path)
    test_vec = np.load(test_path)  # 测试集的向量
    print(train_vec)


def seg_word(sentence):
    """使用jieba对文档分词"""
    stop_word_path = 'H:/dictionary/stopWord.txt'
    import jieba

    seg_list = jieba.cut(sentence)
    seg_result = []
    for w in seg_list:
        seg_result.append(w)
    stopwords = set()
    import codecs
    fr = codecs.open(stop_word_path, 'r', 'utf-8')
    for word in fr:
        stopwords.add(word.strip())
    fr.close()
    return list(filter(lambda x: x not in stopwords, seg_result))


def bool_int(item):
    if type(item) is int:
        print('wa')


def write_seg(path, w_path):  # write train 31s, test 9s
    content = np.loadtxt(path, delimiter=',', usecols=[1], encoding='utf-8', dtype=str)[1:]
    seg_content = [seg_word(sentence) for sentence in content]
    np.save(w_path, seg_content)


def rename(di, add):
    tmp = di.split('/')[:-1]
    tmp.append(add)
    return '/'.join(tmp)


def del_int(li):
    i = 0
    while i < len(li):
        j = 0
        while j < len(li[i]):
            if type(li[i][j]) is int:
                li[i][j] = ''
                print('wa')
            j += 1
        i += 1


def xgboost(train_x, train_y, test_x, test_y):
    # print('dep= ', dep, ' eta = ', eta)
    import pandas as pd
    import xgboost as xgb
    train_y = pd.Series(train_y).replace(-1, 2)  # 因为XGB的无理要求，-1类标必须转为2
    data_train = xgb.DMatrix(train_x, label=train_y)
    # depth 3 eta 0.08 或者 dep=5,eta=0.16
    param = {'max_depth': 5, 'eta': 0.16, 'silent': 1, 'objective': 'multi:softmax', 'nthread': 2, 'num_class': 3}
    model = xgb.train(param, data_train, 100)
    pre = model.predict(xgb.DMatrix(test_x))
    pre = pd.Series(pre).replace(2, -1)  # 然后把类标2换回-1
    if test_y != 0:
        from sklearn.metrics import precision_score
        return precision_score(test_y, pre, average='micro')
    else:
        return pre


def train(score_train_path, train_path):
    from sklearn.model_selection import train_test_split

    score_train = np.load(score_train_path)
    label = read_scv_label(train_path).T[0]
    # print(score_train, '\n', label)

    score_train_th = get_element_by_thr(score_train, 3)
    # eta = [0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08, 0.09, 0.1, 0.11, 0.12, 0.13, 0.14, 0.15, 0.16, 0.17, 0.18, 0.2]
    average = 0
    for i in range(2, 32):
        import random
        random_stat = random.randint(1, 1000)
        train_x, test_x, train_y, test_y = train_test_split(score_train_th, label, test_size=0.2,
                                                            random_state=random_stat)

    #     train
    #     svm_cross_validation(train_x, train_y)
    #
        average += xgboost(train_x, train_y, test_x, test_y)
    print(average*1.0/30)


def read_scv_label(path):
    import csv
    csv_reader = csv.reader(open(path, encoding='utf-8'))
    li = []
    i = 0
    for row in csv_reader:
        i += 1
        if i != 1:
            # print(row)
            li.append(row)
    arr = np.array(li)
    label = arr[:, 3].astype(np.int32).reshape(-1, 1)  # 类标
    return label


def get_element_by_thr(li, th):
    """保留li中tuple第二个值高于阈值的对应id，不会保留用于进行阈值分割的那个值
    :param li: 三维数组，其中每一个二维数组中具有很多元组（此处把元组看为一维数组），元组的格式是(id, 与id相关的数字)
    :param th: 阈值，th仅针对每个元组中第二个值，即上面说的“与id相关的数字”
    :return    一个二维数组，之前的每个元组仅留下id
    """
    new_li = []
    for i in li:
        tmp = []
        for j in i:
            if j[1] > th:
                tmp.append(j[0])
        new_li.append(tmp)
    return new_li


def get_elem_top_k(li, k=2):
    """保留li中tuple第二个值排名前三的对应id
    :param li: 三维数组，其中每一个二维数组中具有很多元组（此处把元组看为一维数组），元组的格式是(id, 与id相关的数字)
    :param k : 选几个
    :return    一个二维数组，之前的每个元组仅留下id
    """
    new_li = []
    for i in li:
        tmp_i = sorted(i, key=lambda prob: prob[1])  # 按元组第二个值排序
        new_li.append(tmp_i[-k:])
    return new_li


if __name__ == '__main__':
    import time
    print('--------LDA-------START', time.ctime(), '\n')

    # common_dictionary = Dictionary(common_texts)
    # for i in common_texts:
    #     print(i)

    # print(type(common_dictionary))

    path1 = 'H:/DF_emotion/train.csv'
    test_path = 'H:/DF_emotion/test_public.csv'
    mod_loc = 'H:/DF_emotion/LDA_model'
    train_vec_loc = 'H:/DF_emotion/train_vector.npy'
    test_vec_loc = 'H:/DF_emotion/test_vector.npy'
    seg_train_loc = 'H:/DF_emotion/seg_sentence.npy'
    seg_test_loc = 'H:/DF_emotion/seg_test.npy'
    # write_seg(test_path, seg_test_loc)
    # print(rename(path1, 'seg_con'))
    # sav_lda_vec(seg_test_loc, test_vec_loc)
    # train_exp()
    # print(np.load(train_vec_loc))
    # print(read_scv_label(path1))
    train(train_vec_loc, path1)
    print('\n--------LDA-------END', time.ctime())
