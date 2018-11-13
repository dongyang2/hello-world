import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage as ndi
from skimage import morphology,feature
import cv2


img_fil3 = 'picture/1/2.jpg'
img4 = cv2.imread(img_fil3)
gray4 = cv2.cvtColor(img4, cv2.COLOR_BGR2GRAY)

#现在我们用分水岭算法分离两个圆
distance = ndi.distance_transform_edt(gray4) #距离变换
local_maxi =feature.peak_local_max(distance, indices=False, footprint=np.ones((3, 3)),
                                   labels=gray4)   #寻找峰值
markers = ndi.label(local_maxi)[0] #初始标记点
labels =morphology.watershed(-distance, markers, mask=gray4) #基于距离变换的分水岭算法

plt.subplot(2, 2, 1)
plt.imshow(gray4)
plt.subplot(2, 2, 2)
plt.imshow(-distance)
plt.subplot(2, 2, 3)
plt.imshow(markers)
plt.subplot(2, 2, 4)
plt.imshow(labels)
plt.show()
