# https://blog.csdn.net/weixin_36541072/article/details/53786020

# coding:utf-8

import jieba  # 导入结巴分词
import numpy as np  # 导入Numpy
import pandas as pd  # 导入Pandas
from keras.layers.core import Dense, Dropout, Activation
from keras.layers.embeddings import Embedding
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from keras.preprocessing import sequence
from keras.utils import np_utils

# 读取训练语料完毕
neg = pd.read_excel(r'D:\tomcat\Theano\neg.xls', header=None, index=None)  # dataframe类型
pos = pd.read_excel(r'D:\tomcat\Theano\pos.xls', header=None, index=None)
# 给训练语料贴上标签
pos['mark'] = 1
neg['mark'] = 0
pn = pd.concat([pos, neg], ignore_index=True)  # 合并语料
# 计算语料数目
neglen = len(neg)
poslen = len(pos)

cw = lambda x: list(jieba.cut(x))  # 定义分词函数
pn['words'] = pn[0].apply(cw)

comment = pd.read_excel(r'D:\tomcat\Theano\sum.xls')  # 读入评论内容
# comment = pd.read_csv('a.csv', encoding='utf-8')
comment = comment[comment['rateContent'].notnull()]  # 仅读取非空评论
comment['words'] = comment['rateContent'].apply(cw)  # 评论分词

d2v_train = pd.concat([pn['words'], comment['words']], ignore_index=True)

# 将所有词语整合在一起
w = []
for i in d2v_train:
    w.extend(i)

# 统计词的出现次数
dict = pd.DataFrame(pd.Series(w).value_counts())
del w, d2v_train
dict['id'] = list(range(1, len(dict) + 1))

get_sent = lambda x: list(dict['id'][x])
pn['sent'] = pn['words'].apply(get_sent)  # 速度太慢

maxlen = 50

print("Pad sequences (samples x time)")
pn['sent'] = list(sequence.pad_sequences(pn['sent'], maxlen=maxlen))

x = np.array(list(pn['sent']))[::2]  # 训练集
y = np.array(list(pn['mark']))[::2]
xt = np.array(list(pn['sent']))[1::2]  # 测试集
yt = np.array(list(pn['mark']))[1::2]
xa = np.array(list(pn['sent']))  # 全集
ya = np.array(list(pn['mark']))

print('Build model...')
model = Sequential()
model.add(Embedding(len(dict) + 1, 256, input_length=maxlen))
model.add(LSTM(output_dim=128, activation='sigmoid', inner_activation='hard_sigmoid'))
model.add(Dropout(0.5))
model.add(Dense(1))
model.add(Activation('sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])
# model.compile(loss='binary_crossentropy', optimizer='adam', class_mode="binary")

model.fit(xa, ya, batch_size=16, nb_epoch=5)  # 训练时间为若干个小时

classes = model.predict_classes(xa)
acc = np_utils.accuracy(classes, ya)
print('Test accuracy:', acc)
