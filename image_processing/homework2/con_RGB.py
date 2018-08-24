#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 14:39:45 2018

@author: mingsun
"""
import cv2
import numpy as np
# from imutils import paths
import os
import pandas as pd




def create_rgb_hist(image):
    """创建rgb 三通道直方图"""
    h, w, c = image.shape
    rHist = np.zeros([16], np.float32)
    gHist = np.zeros([16], np.float32)
    bHist = np.zeros([16], np.float32)
    allHist = np.zeros([48], np.float32)
    bsize = 256 / 16
    for row in range(h):
        for col in range(w):
            b = image[row, col, 0]
            g = image[row, col, 1]
            r = image[row, col, 2]
            index_r = np.int(r / bsize)
            index_g = np.int(g / bsize)
            index_b = np.int(b / bsize)
            rHist[index_r] = rHist[index_r] + 1
            gHist[index_g] = gHist[index_g] + 1
            bHist[index_b] = bHist[index_b] + 1

    allHist = np.append(rHist, gHist)
    allHist = np.append(allHist, bHist)

    return allHist


if __name__ == '__main__':
    # train_path = '/home/mingsun/DIP2/dataset'
    train_path = 'picture'
    labels = []
    fea_rgb = []
    featVecs = []

    for train_file_name in os.listdir(train_path):
        train_file_path = train_path + '/' + train_file_name
        for img_name in os.listdir(train_file_path):
            img_path = train_file_path + '/' + img_name
            img = cv2.imread(img_path)
            fea_rgb = create_rgb_hist(img)
            featVec_uni = np.array([x / fea_rgb.sum() for x in fea_rgb])
            featVecs.append(featVec_uni)
            labels.append(train_file_name)
            # %%
    results = pd.DataFrame(featVecs)
    # %%
    results['label'] = labels

    results.to_csv('fea_RGB.txt', index=False, sep=',')
