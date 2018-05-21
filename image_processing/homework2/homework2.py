#! python3
# coding: utf-8

import pickle
import xgboost as xgb
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from image_processing.homework2 import cut, feature, text_op, file_op
import datetime


def get_elem_from_li(li):
    """把二维数组中每个一维数组中的内容取出来，返回一个一维数组"""
    tmp_li = []
    for i in li:
        for j in i:
            tmp_li.append(j)
    return tmp_li


def change_dir(dr, st):
    tmp_s = dr.split('/')
    s = ''
    for ii, i in enumerate(tmp_s):
        if ii == len(tmp_s)-1:
            s += st
        else:
            s += i+'/'
    return s


def acc(pre, tst):
    ll = len(pre)
    i = 0
    c = 0
    while i < ll:
        if pre[i] == tst[i]:
            c += 1
        i += 1
    return c/ll*1.0


def run(fil, cla_num=26):
    """fil是特征文件位置"""
    fea3 = np.loadtxt(fil, delimiter=",")
    div = len(fea3[0])-1
    # print(div)
    x, tmp_y = np.split(fea3, (div,), axis=1)
    y = get_elem_from_li(tmp_y)
    # print(x, '\n', y)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2018)
    # print(x_train, '\n', y_train)
    data_train = xgb.DMatrix(x_train, label=y_train)
    data_test = xgb.DMatrix(x_test, label=y_test)

    # param = {'max_depth': 2, 'eta': 1, 'silent': 1, 'objective': 'multi:softmax', 'num_class': 26}
    param = {'max_depth': 7, 'eta': 0.10, 'silent': 1, 'objective': 'multi:softmax', 'num_class': cla_num}

    watch_list = [(data_test, 'eval'), (data_train, 'train')]
    model = xgb.train(param, data_train, num_boost_round=100, evals=watch_list)
    model.save_model('rgb_xgb.model')
    pre = model.predict(data_test)
    # result = y_test.reshape(1, -1) == pre
    print(acc(pre, y_test))


def use(fil, dr, nl):
    """fil是模型文件,dr是测试文件的目录"""
    mod = xgb.Booster(model_file=fil)
    lf = file_op.each_file_or_dir_name(dr)
    label = []
    for i in lf:
        tmp = file_op.each_file_or_dir_name(i)
        for j in tmp:
            label.append(j.split('/')[-2])

    ff = change_dir(test_dr, 'result') + '/feature.txt'
    feature.write_rgb_f(dr, ff)  # 写入特征
    fea = np.loadtxt(ff, delimiter=",")
    test = xgb.DMatrix(fea)
    pre = mod.predict(test)
    rlt = []
    for i in pre:
        nam = text_op.get_sub_or_elem(int(i), nl)
        rlt.append(nam)
    print(rlt)
    print(acc(rlt, label))


if __name__ == '__main__':
    fil_nam2 = 'H:/lesson/image_process/result/features1.csv'
    fil_nam1 = 'H:/lesson/image_process/result/features.txt'  # 存放特征结果的文件夹
    fil_nam3 = 'H:/lesson/image_process/result/features3.txt'  # 100cut图像像素点
    fil_nam4 = 'H:/lesson/image_process/result/features5.txt'  # rgb出现频率
    fil_nam5 = 'H:/lesson/image_process/result/features1.txt'  # 250个原始图像像素点
    fil_nam6 = 'H:/lesson/image_process/result/features6.txt'  # 250cut图像像素点
    dir_name1 = 'H:/lesson/image_process/dataset'  # 放各种原图片的文件夹
    test_dr = 'picture'
    mod_name1 = 'rgb_xgb.model'
    names = ['丰水梨', '冰糖心苹果', '冰糖橙', '台湾青枣', '国产青苹果', '大台农芒', '富士王', '小台农芒', '泰国香蕉', '海南香蕉', '澳洲大芒', '澳洲蜜柑', '特级红富士',
             '番石榴', '百香果', '砀山梨', '米蕉', '纽荷脐橙', '脆肉瓜', '花牛红苹果', '蜜梨', '贡梨', '陕西香酥梨', '雪梨', '鸭梨', '黄金梨']

    # cut.cut_pic(dir_name1)  # 裁剪图片
    # num_top = 100
    # 17:32~18:26 100个像素点 18：54~19：53 100个像素点
    # feature.write_feature(change_dir(dir_name1, 'cutout'), fil_nam3, nt=num_top)  # 存特征
    # 20：33~23:33
    # feature.write_rgb_f(change_dir(dir_name1, 'cutout'), fil_nam4, names)  # 存RGB特征
    # run(fil_nam4)  # 训练模型

    cut.cut_pic(test_dr)  # 裁剪图片
    use(mod_name1, change_dir(test_dr, 'cutout'), names)  # 使用保存的模型进行预测
