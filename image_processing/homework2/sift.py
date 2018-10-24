# Scale-invariant feature transform

import cv2
import numpy as np
import matplotlib.image as img
from matplotlib import pyplot as plt


# def getSift(fil):
#     """    得到并查看sift特征    """
#     # 读取图像
#     img1 = cv2.imread(fil)
#     # 转换为灰度图
#     gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
#     # 创建sift的类
#     sift = cv2.SIFT()
#     # 在图像中找到关键点 也可以一步计算#kp, des = sift.detectAndCompute
#     kp = sift.detect(gray, None)
#     print(type(kp), type(kp[0]))
#     # Keypoint数据类型分析 http://www.cnblogs.com/cj695/p/4041399.html
#     print(kp[0].pt)
#     # 计算每个点的sift
#     des = sift.compute(gray, kp)
#     print(type(kp), type(des))
#     # des[0]为关键点的list，des[1]为特征向量的矩阵
#     print(type(des[0]), type(des[1]))
#     print(des[0], des[1])
#     # 可以看出共有885个sift特征，每个特征为128维
#     print(des[1].shape)
#     # 在灰度图中画出这些点
#     img2 = cv2.drawKeypoints(gray, kp)
#     # cv2.imwrite('sift_keypoints.jpg',img2)
#     plt.imshow(img2), plt.show()


def matchSift3():
    '''
    匹配sift特征
    '''
    img1 = cv2.imread('../../data/box.png', 0)  # queryImage
    img2 = cv2.imread('../../data/box_in_scene.png', 0)  # trainImage
    sift = cv2.SIFT()
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)
    # 蛮力匹配算法,有两个参数，距离度量(L2(default),L1)，是否交叉匹配(默认false)
    bf = cv2.BFMatcher()
    # 返回k个最佳匹配
    matches = bf.knnMatch(des1, des2, k=2)
    # cv2.drawMatchesKnn expects list of lists as matches.
    # opencv3.0有drawMatchesKnn函数
    # Apply ratio test
    # 比值测试，首先获取与A 距离最近的点B（最近）和C（次近），只有当B/C
    # 小于阈值时（0.75）才被认为是匹配，因为假设匹配是一一对应的，真正的匹配的理想距离为0
    good = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good.append([m])
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, good[:10], None, flags=2)
    cv2.drawm
    plt.imshow(img3)
    plt.show()


if __name__ == '__main__':
    img_fil1 = 'picture/1/3.jpg'
    img_fil2 = 'H:/lesson/image_process/cut/澳洲蜜柑/20170412170047.jpg'

    img4 = img.imread(img_fil2)
    # SIFT
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints = sift.detect(img4, None)

    # kp, des = sift.detectAndCompute(gray,None)  #des是描述子，for match， should use des, bf = cv2.BFMatcher();smatches = bf.knnMatch(des1,des2, elem=2
    cv2.drawKeypoints(img4, keypoints, img4)
    cv2.imshow('testSift', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
