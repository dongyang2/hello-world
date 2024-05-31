# 展示一张图片
# Python 3
# coding: UTF-8

import matplotlib.pyplot as plt
import matplotlib.image as pim

path = '01400.jpg'
pic = pim.imread(path)
plt.imshow(pic)
plt.axis('off')  # 不显示坐标轴
plt.show()
