from small_gram import file_op as fo
from lessons.image_processing.homework2 import text_op as to, histogram
import matplotlib.image as img
import os
import datetime


def write_file(li, filename):
    """写图片RGB像素点到文件中"""
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = to.get_dir(filename)
        os.makedirs(f)
        f = open(filename, 'w', encoding='utf-8')
    for i in li:
        for jj, j in enumerate(i):
            if jj != len(i)-1:
                for k in j:
                    f.write(str(k) + ' ')
                f.write(',')
            else:
                f.write(j)
        f.write('\n')
    f.close()


def write_file_new(li, filename):
    """写图片RGB前50个像素点到文件中,一个像素点只写一个数字"""
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = to.get_dir(filename)
        os.makedirs(f)
        f = open(filename, 'w', encoding='utf-8')
    for i in li:
        for jj, j in enumerate(i):
            if jj != len(i)-1:
                ss = ''
                for k in j:
                    sk = str(k)
                    if len(sk) == 1:
                        tmp_s = '00' + sk
                    elif len(sk) == 2:
                        tmp_s = '0' + sk
                    else:
                        tmp_s = sk
                    ss = ss + tmp_s
                f.write(ss+',')
            else:
                f.write(j)
        f.write('\n')
    f.close()


def write_feature(in_file, out_file, nl, nt=50):
    dirs = fo.each_file_or_dir_name(in_file)
    line = []
    # m = 0
    for i in dirs:
        j = fo.each_file_or_dir_name(i)
        for k in j:
            # if m == 300:
            #     break
            pic = img.imread(k)
            # cut_pic = cut.cut_by_thr(pic)
            color = histogram.cnt(pic.tolist(), top=nt)  # RGB特征像素点
            s = k.split('/')[-2]  # 获得水果种类
            ind = to.get_sub_or_elem(s, nl)  # 加入类标
            # print(ind)
            color.append(str(ind))
            line.append(color)
            # m += 1
    # for num in line:
    #     print(num)
    write_file_new(line, out_file)


def write_rgb_f(in_fil, out_fil, nl=0):
    """nl=0则不写入类标，直接写入特征，否则nl需是一个列表，存放了类标的中文名字"""
    dirs = fo.each_file_or_dir_name(in_fil)
    line = []
    # m = 0
    for i in dirs:
        j = fo.each_file_or_dir_name(i)
        for k in j:
            # if m == 30:
            #     break
            # pic = img.imread(elem)
            color = histogram.get_rgb(k)
            if nl != 0:
                s = k.split('/')[-2]  # 获得水果种类
                ind = to.get_sub_or_elem(s, nl)  # 加入类标
                # print(ind)
                color.append(str(ind))
            line.append(color)
            # m += 1
    # for num in line:
    #     print(num)
    write_file_li(line, out_fil)


def read_pix_old(file):
    """把每个RGB像素都读成一个9位的数字"""
    f = fo.read_file(file)
    fil_li = []
    for i in f:
        s = i.split(',')
        tmp_li = []
        for j in s:
            si = j.split(' ')
            ss = ''
            for k in si:
                if len(k) == 1:
                    tmp_s = '00' + k
                elif len(k) == 2:
                    tmp_s = '0' + k
                else:
                    tmp_s = k
                ss = ss + tmp_s
            tmp_li.append(ss)
            # print(each_c)
        fil_li.append(tmp_li)
    return fil_li


def write_file_li(li, filename):
    try:
        f = open(filename, 'w', encoding='utf-8')
    except FileNotFoundError:
        f = to.get_dir(filename)
        os.makedirs(f)
        f = open(filename, 'w', encoding='utf-8')
    if type(li[0]) is not list:
        for ii, i in enumerate(li):
            if ii == len(li)-1:
                f.write(str(i))
            else:
                f.write(str(i) + ',')
        f.write('\n')
    else:
        for i in li:
            for jj, j in enumerate(i):
                if jj == len(i)-1:
                    f.write(str(j))
                else:
                    f.write(str(j) + ',')
            f.write('\n')
    f.close()


if __name__ == '__main__':
    time_stamp = datetime.datetime.now()
    print(time_stamp.strftime('%Y.%m.%d %H:%M:%S'))

    dir_name1 = 'H:/lesson/image_process/dataset'
    dir_name2 = 'H:/lesson/image_process/cut'
    img_fil1 = 'picture/澳洲大芒/20170307144225.jpg'
    write_name1 = 'H:/lesson/image_process/result/features.txt'
    write_name2 = 'H:/lesson/image_process/result/features1.txt'
    write_name3 = 'H:/lesson/image_process/result/features4.txt'
    write_name4 = 'H:/lesson/image_process/result/features6.txt'

    # dirs1 = fo.each_file_or_dir_name(dir_name1)
    # names1 = []  # 二维列表
    # lines = []
    # # m = 0
    # from matplotlib import pyplot as plt
    # for i1 in dirs1:
    #     j1 = fo.each_file_or_dir_name(i1)
    #     for k1 in j1:
    #         # if m == 2:
    #         #     break
    #         pic = img.imread(k1)
    #         cut_pic = cut.cut_by_thr(pic)
    #         # plt.subplot(1, 2, 1)
    #         # plt.imshow(cut_pic)
    #         # plt.subplot(1, 2, 2)
    #         # plt.imshow(pic)
    #         # plt.show()
    #         color = histogram.cnt(cut_pic.tolist())  # RGB特征
    #         s = k1.split('/')[-2]  # 再加入类标
    #         color.append(s)
    #         lines.append(color)
    #         # m += 1
    #     # break
    #     # names1.append(j1)
    # write_file(lines, write_name)
    # print(names1)

    # 这个要跑3个小时,50个像素点
    # write_feature(dir_name1, write_name1)
    # write_feature(dir_name2, write_name4, 250)  # 250个像素点 cut图像 52分钟
    # time_stamp = datetime.datetime.now()
    # 测试write_rgb_f()函数, 30个1分2秒，三千个应该是1小时42分
    # write_rgb_f(dir_name1, write_name3)

    print(time_stamp.strftime('%Y.%m.%d %H:%M:%S'))

