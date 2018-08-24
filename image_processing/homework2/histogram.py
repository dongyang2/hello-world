import numpy as np
from skimage import exposure, data
import cv2
import matplotlib.image as img
from matplotlib import pyplot as plt
from collections import Counter
from image_processing.homework2 import con_RGB as cr
import operator
from image_processing.homework2 import cut


def cnt(li, top=50, del_white=True, turn_li=True):
    """统计最多出现的像素点"""
    hist = {}
    for i in li:
        for j in i:
            t_j = tuple(j)
            if t_j in hist.keys():
                hist[t_j] += 1
            else:
                hist[t_j] = 1
    # print(hist)
    zip_h = zip(hist.values(), hist.keys())
    s_h = sorted(zip_h)  # 升序排好的所有颜色
    # print(s_h)
    if del_white is True:
        d_sh = del_wh(s_h)
        top_50 = d_sh[-top - 1:-1]
    else:
        top_50 = s_h[-top:]
    # print(len(top_50))
    if turn_li is True:
        return get_pix(top_50)
    else:
        return top_50


def get_pix(li):
    rlt = []
    for i in li:
        pix = []
        for j in i[1]:
            pix.append(j)
        rlt.append(pix)
    return rlt


def del_wh(li):
    tmp_li = []
    for ii, i in enumerate(li):
        b_w = 0
        for j in i[1]:
            if j > 235:
                b_w += 1
        if b_w < 2:
            tmp_li.append(i)
            # li.pop(ii)
    return tmp_li


def get_shi(num, shi=1):
    """算num所在的十位段，比如255在250段，136在130段
    shi=1 返回十位段
    shi=0 返回没有0的十位段，比如255是25段，3是0段，136是13段，压缩数据"""
    st = str(num)
    ls = len(st)
    if shi ==1:
        if ls == 1:
            return 0
        else:
            du = int(st[:-1])*10
            return du
    else:
        if ls == 1:
            return 0
        else:
            du = int(st[:-1])
            return du


def get_rgb(fil):
    from PIL import Image
    im = Image.open(fil)
    pix = im.load()
    width = im.size[0]
    height = im.size[1]
    hist_r = [0 for i in range(26)]
    # print(len(hist_r))
    hist_g = [0 for i in range(26)]
    hist_b = [0 for i in range(26)]
    for x in range(width):
        for y in range(height):
            r, g, b = pix[x, y]
            rs = get_shi(r, 0)
            gs = get_shi(g, 0)
            bs = get_shi(b, 0)
            hist_r[rs] += 1
            hist_g[gs] += 1
            hist_b[bs] += 1
    tmp_li = []
    for i in hist_r:
        tmp_li.append(i)
    for i in hist_g:
        tmp_li.append(i)
    for i in hist_b:
        tmp_li.append(i)
    return tmp_li


if __name__ == '__main__':
    img_fil1 = 'picture/澳洲大芒/20170307144225.jpg'
    img_fil2 = 'H:/lesson/image_process/dataset/丰水梨/20170308103252.jpg'
    img3 = img.imread(img_fil2)

    # hist1 = np.histogram(img3, bins=2)  # 用numpy包计算直方图
    # hist2 = exposure.histogram(img3, nbins=2)  # 用skimage计算直方图
    # print(hist1)
    # print(len(hist2))
    # print(Counter(img3.tolist()))
    # img3 = cut.cut_by_thr(img3)
    # con1 = cnt(img3.tolist(), turn_li=False)
    # print(get_pix(con1))
    # print(cnt(img3.tolist()))
    # d1 = {(1, 2): 3, (2, 3): 2, (3, 4): 5, (4, 5): 1}
    # li1 = [1, 2]
    # d11 = sorted(d1.items(), key=operator.itemgetter(1))
    # print(d11)

    # 测试 del_wh()函数
    # li2 = [(1, (0, 2, 7)), (1, (0, 4, 6)), (1, (0, 5, 0)), (1, (0, 6, 0)), (1, (0, 8, 0)),(1, (1, 5, 6)),
    #        (1, (250, 231, 245)), (1, (2, 1, 7)), (1, (2, 3, 5)), (2, (250, 251, 153)), (1, (255, 255, 255))]
    # print(del_wh(li2))
    # 测试get_rgb()函数
    print(get_rgb(img_fil1))

    # print(get_shi(255, 0))
