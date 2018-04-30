import cv2
import matplotlib.pyplot as plt
import numpy as np


def reverse_gray(image):
    """反转整幅图的灰度级"""
    empty = np.zeros(image.shape, np.uint8)
    height = image.shape[0]
    width = image.shape[1]
    for i in range(height):
        for j in range(width):
            empty[i, j] = 255 - image[i, j]
    return empty


def erode_dilate(image, flag, ct=1, ks=5, blur=0):
    """开运算，ct是循环次数，ks是腐蚀膨胀的窗口大小"""
    k_size = (ks, ks)
    tmp = image

    if flag != 'open' and flag != 'close':
        return False
    for i in range(ct):
        if flag == 'open':
            er = cv2.erode(image, k_size)
            tmp = cv2.dilate(er, k_size)
        else:
            di = cv2.dilate(image, k_size)
            tmp = cv2.erode(di, k_size)
        if blur == 1:
            tmp = cv2.GaussianBlur(tmp, (5, 5), 0.6)
    return tmp


def repeat(image, flag, ct=1, ks=5, blur=0):
    if ct < 1:
        return False
    if flag != 'dilate' and flag != 'erode':
        return False

    k_size = (ks, ks)
    result = image
    for i in range(ct):
        if flag == 'dilate':
            result = cv2.dilate(result, k_size)
        else:
            result = cv2.erode(result, k_size)
        if blur == 1:
            result = cv2.GaussianBlur(result, (5, 5), 0.6)
    return result


def process(image, th=80):
    # image = cv2.GaussianBlur(image, (5, 5), 0.8)

    thr_4 = cv2.threshold(image, th, 255, cv2.THRESH_BINARY)[1]
    thr_ga = cv2.GaussianBlur(thr_4, (5, 5), 0.6)
    thr_ga_la = reverse_gray(cv2.convertScaleAbs(cv2.Laplacian(thr_ga, cv2.CV_16S, ksize=3)))
    thr_ga_la_r = repeat(thr_ga_la, 'erode', 1)
    # thr_ga_la_rr = repeat(thr_ga_la_r,'dilate',5)
    # thr_ga_la_cl = erode_dilate(thr_ga_la, 'close', 10, 11)
    # thr_ga_la_ga = cv2.GaussianBlur(thr_ga_la, (11,11), 0.4)
    result = thr_ga_la
    plt.imshow(result)
    plt.show()
    return result


def process2(image, th=80):
    thr_4 = cv2.threshold(image, th, 255, cv2.THRESH_BINARY)[1]
    # thr_ga = cv2.GaussianBlur(thr_4, (5, 5), 0.2)
    thr_ga_la_r = repeat(thr_4, 'erode', 2)
    thr_ga_la_cl = erode_dilate(thr_ga_la_r, 'open', 5, 11)
    # thr_ga_la_ga = cv2.GaussianBlur(thr_ga_la, (11,11), 0.4)
    result = thr_ga_la_cl
    plt.imshow(result)
    plt.show()
    return result


def process3(image):
    ga = cv2.GaussianBlur(image, (5, 5), 0.6)
    ga_la = reverse_gray(cv2.convertScaleAbs(cv2.Laplacian(ga, cv2.CV_16S, ksize=3)))
    ga_la_cl_th = cv2.threshold(ga_la, 80, 255, cv2.THRESH_BINARY)[1]

    ga_la_cl = erode_dilate(ga_la_cl_th, 'open', ct=5,blur=1)
    # ga_la_cl_ga = cv2.GaussianBlur(ga_la_cl, (5, 5), 0.6)
    result = ga_la_cl
    plt.imshow(result)
    plt.show()


def ots(img_gray, th_begin=0, th_end=256, th_step=1):
    assert img_gray.ndim == 2, "must input a gary_img"

    max_g = 0
    suitable_th = 0
    for threshold in range(th_begin, th_end, th_step):
        bin_img = img_gray > threshold
        bin_img_inv = img_gray <= threshold
        fore_pix = np.sum(bin_img)
        back_pix = np.sum(bin_img_inv)
        if 0 == fore_pix:
            break
        if 0 == back_pix:
            continue

        w0 = float(fore_pix) / img_gray.size
        u0 = float(np.sum(img_gray * bin_img)) / fore_pix
        w1 = float(back_pix) / img_gray.size
        u1 = float(np.sum(img_gray * bin_img_inv)) / back_pix
        g = w0 * w1 * (u0 - u1) * (u0 - u1)
        if g > max_g:
            max_g = g
            suitable_th = threshold
    return suitable_th


def together(image, ct):
    r1 = cv2.GaussianBlur(image, (11, 11), 0.4)
    r2 = repeat(r1, 'erode', 10, 5)
    for i in range(ct - 1):
        r1 = cv2.GaussianBlur(r2, (11, 11), 0.4)
        r2 = repeat(r1, 'erode', 10, 5)
    return r2


if __name__ == '__main__':
    img1 = cv2.imread("picture/4.bmp")
    img2 = cv2.imread('picture/4.bmp', 0)
    img3 = cv2.imread('picture/6.bmp')
    img4 = cv2.imread('picture/6.bmp', 0)
    img5 = cv2.imread('picture/15.bmp')
    img15 = cv2.imread('picture/15.bmp', 0)
    img7 = cv2.imread('picture/21.bmp')
    img21 = cv2.imread('picture/21.bmp', 0)

    process3(img7)
    # p1 = process2(img7,70)
    # p1 = cv2.threshold(img3, 60, 255, cv2.THRESH_BINARY)[1]
    # p3 = together(p1, 1)
    # p4 = erode_dilate(p3,'close',100)
    # p3 = cv2.GaussianBlur(p2, (11, 11), 0.4)
    # p4 = repeat(p3, 'erode', 10, 5)
    # p5 = repeat(p4,'erode',100,5)

    # xgrad = cv2.Sobel(p1, cv2.CV_16SC1, 1, 0)
    # ygrad = cv2.Sobel(p1, cv2.CV_16SC1, 0, 1)
    # edge_output = cv2.Canny(xgrad, ygrad, 50, 150)
    # plt.imshow(edge_output)
    # plt.show()

    # plt.subplot(1, 2, 1)
    # plt.imshow(p1)
    #
    # plt.subplot(1, 2, 2)
    # plt.imshow(p3)
    #
    # plt.show()

    # print(img1.shape)  # 图像的宽，高，通道
    # print(type(img1.shape[1]))
    # print(img2.shape)  # 图像的宽，高

    # numb = img
    # print(numb)

    # img[50, 100] = (0, 0, 255)
    # cv2.imshow("img", img)    # 使用cv2进行图像输出
    # cv2.waitKey()

    # 使用plt进行图像输出
    # plt.imshow(img2)
    # plt.show()
    # 拉普拉斯算子
    # img6 = cv2.Laplacian(img5, cv2.CV_16S, ksize=3)
    # lap_img6 = cv2.convertScaleAbs(img6)
    #
    # thr_6 = cv2.threshold(img4, 100, 255, cv2.THRESH_BINARY)[1]  # 阈值分割
    # thr_gauss_4 = cv2.GaussianBlur(thr_6, (5, 5), 0.6) # 高斯滤波
    # thr_gauss_lap_4 = cv2.convertScaleAbs(cv2.Laplacian(thr_gauss_4, cv2.CV_16S, ksize=3))
    # thr_gauss_lap_rev_4 = reverse_gray(thr_gauss_lap_4)
    #
    # thr_gauss_lap_rev_er_4 = cv2.erode(thr_gauss_lap_rev_4, (5, 5))  # 腐蚀
    # thr_gauss_lap_rev_er_di_4 = cv2.dilate(thr_gauss_lap_rev_er_4, (5, 5))  # 膨胀

    # thr_gauss_lap_rev_4 = cv2.threshold(thr_gauss_lap_rev_4, 100, 255, cv2.THRESH_BINARY)[1]
    # thr_gauss_lap_rev_4 = cv2.dilate(thr_gauss_lap_rev_4, (5, 5))

    # thr_gauss_lap_rev_ed_4 = erode_dilate(thr_gauss_lap_rev_4, 'open', 10,3)
    # thr_gauss_lap_rev_de_4 = erode_dilate(thr_gauss_lap_rev_4, 'close', 10,3)

    # thr_gauss_lap_rev_cl_4 = cv2.morphologyEx(thr_gauss_lap_rev_4, cv2.MORPH_CLOSE, (7, 7))  # 闭运算

    # ga_4 = cv2.GaussianBlur(img4, (5,5), 0.8)
    # ga_la = reverse_gray(cv2.convertScaleAbs(cv2.Laplacian(ga_4, cv2.CV_16S, ksize=3)))
    # # ga_la_cl = erode_dilate(ga_la,'close',10)
    # ga_la_thr = cv2.threshold(ga_la, 150, 255, cv2.THRESH_BINARY)[1]

    # plt.subplot(1, 2, 1)
    # plt.imshow(img4)
    #
    # plt.subplot(1, 2, 2)
    # plt.imshow(reverse_gray(img4))
    #
    # plt.show()

    # print(cv2.CV_16S)
