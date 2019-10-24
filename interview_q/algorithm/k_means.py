# coding: utf-8
# python 3
# WPS 笔试最后一题

# 大致思路：
# 1.指定k个初始中心；
# 2.将点分配到k个初始中心，形成k个簇；
# 3.重新计算k个中心；
# 4.重复2，3步直到触发终止条件。

import math


class Solution:

    def __init__(self, n, k, m):
        self.n_dim = n
        self.k = k
        self.m = m
        self.means = []

    def train(self, data):
        train_num = len(data)
        cent = data[::int(train_num / self.k)]  # 找k个初始点，也可以random()出来
        flag = [0 for _ in range(train_num)]
        for _ in range(self.m):  # m次迭代
            # 分配到中心
            for i in range(train_num):
                min_d = distance(data[i], cent[0])
                for j in cent:
                    if distance(data[i], cent[j]) <= min_d:
                        min_d = distance(data[i], cent[j])
                        flag[i] = j
            # 重新找k个中心
            for i in range(self.k):
                sum_li = [0 for _ in range(self.k)]
                for j in range(train_num):
                    if flag[j] == i:
                        for d_i in data[j]:
                            sum_li[d_i] += data[j][d_i]
                cent[i] = [x / self.n_dim for x in sum_li]  # 中心点
        # 结束m次迭代后，将中心点存到变量里
        self.means = cent

    def evaluate(self, data):
        label = 0
        d = distance(self.means[0], data)
        for i in range(self.k):
            if distance(self.means[i], data) <= d:
                d = distance(self.means[i], data)
                label = i
        return label


def distance(x1, x2):
    sum_ = 0
    for i in range(len(x1)):
        sum_ += pow(x1[i] - x2[i], 2)
    return math.sqrt(sum_)
