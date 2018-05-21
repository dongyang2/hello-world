import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology, filters
import cv2

img_fil3 = 'picture/1/2.jpg'
img4 = cv2.imread(img_fil3)

gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)
denoised = filters.rank.median(gray4, morphology.disk(2))  # 过滤噪声

# 将梯度值低于10的作为开始标记点
markers = filters.rank.gradient(denoised, morphology.disk(5)) < 10
markers = ndi.label(markers)[0]

gradient = filters.rank.gradient(denoised, morphology.disk(2))  # 计算梯度
labels = morphology.watershed(gradient, markers, mask=gray4)  # 基于梯度的分水岭算法

plt.subplot(2, 2, 1)
plt.imshow(gray4)
plt.subplot(2, 2, 2)
plt.imshow(gradient)
plt.subplot(2, 2, 3)
plt.imshow(markers)
plt.subplot(2, 2, 4)
plt.imshow(labels)

plt.show()
