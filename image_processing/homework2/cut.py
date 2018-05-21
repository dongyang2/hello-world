import cv2
import numpy as np
import os
import matplotlib.image as img
from matplotlib import pyplot as plt
from small_gram import file_op as fo
from PIL import Image as im
from image_processing.homework2 import histogram, text_op as to


def cut_by_thr(pic, thr=80):
    li_pic = pic.tolist()
    gray = cv2.cvtColor(pic, cv2.COLOR_BGR2GRAY)
    th_pic = cv2.threshold(gray, thr, 255, cv2.THRESH_BINARY)[1]

    rlt = []
    for ii, i in enumerate(th_pic):
        tmp = []
        for jj, j in enumerate(i):
            if j == 0 and bool_black(li_pic[ii][jj]) is False:
                tmp.append(li_pic[ii][jj])
            else:
                tmp.append([255, 255, 255])
        rlt.append(tmp)
    return np.uint8(rlt)


def bool_black(li):
    bool_b = 0
    for i in li:
        if i < 30:
            bool_b += 1
    if bool_b == 3:
        return True
    else:
        return False


def cut_pic(fil, th=80):
    """把原始图像进行裁剪，然后保存到另一个目录下"""
    dirs = fo.each_file_or_dir_name(fil)
    # m = 0
    for i in dirs:
        j = fo.each_file_or_dir_name(i)
        for k in j:
            # if m == 2:
            #     break
            pic = img.imread(k)
            cut_rlt = cut_by_thr(pic, thr=th)
            loc = write_dir(k)
            fo.save_pic(cut_rlt, loc)
            # m += 1


def write_dir(st):
    tmp_li = st.split('/')
    s = ''
    ll = len(tmp_li)
    for ii, i in enumerate(tmp_li):
        if ii == ll-3:
            s += 'cutout/'
        elif ii == ll-1:
            s += i
        else:
            s += i+'/'
        # print(ii, s)
    return s


if __name__ == '__main__':
    dir_name1 = 'H:/lesson/image_process/dataset'
    img_fil1 = 'picture/澳洲大芒/20170307144225.jpg'
    img_fil2 = '../homework1/picture/4.bmp'
    # img = cv2.imread(img_file, cv2.IMREAD_COLOR)
    # img1 = cv2.imread(img_file)  # opencv不支持中文
    img3 = img.imread(img_fil1)
    # img4 = cv2.imread(img_fil5)
    # img5 = img.imread(img_fil3)
    # img2 = cv2.imread(img_fil2)

    # ret, thresh = cv2.threshold(gray4, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)  # opencv分水岭算法

    # print(p1.shape)  # 灰度图像是二维矩阵
    # print(img4)  # 彩色图像是三维矩阵
    # li_p1 = p1.tolist()  # 将np的uint8数组改为list
    # np_p1 = np.array(li_p1, dtype=np.uint8)  # 将list改回np的uint8
    # print(np_p1)

    get_r = cut_by_thr(img3)
    # s_f1 = 'H:/lesson/image_process/cut/2.jpg'
    # fo.save_pic(get_r, s_f1)
    plt.subplot(1, 2, 1)
    plt.imshow(get_r)

    plt.subplot(1, 2, 2)
    plt.imshow(img3)
    plt.show()

    # cut_pic(dir_name1)
    # st1 = 'H:/lesson/image_process/dataset/丰水梨/20170308103252.jpg'
    # print(write_dir(st1))
