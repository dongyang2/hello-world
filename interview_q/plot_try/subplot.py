# python3.5 matplotlib2.2.3 numpy1.14.5

import matplotlib.pyplot as plt
import numpy as np

# # 方法一 单独指定每个子图。使用的是subplots()
# np.random.seed(19990116)
# data = np.random.randn(2, 100)
#
# _, axs = plt.subplots(2, 2, figsize=(5, 5))
# axs[0, 0].hist(data[0])
# axs[1, 0].scatter(data[0], data[1])
# axs[0, 1].plot(data[0], data[1])
# axs[1, 1].hist2d(data[0], data[1])
#
# plt.show()

# 方法二 使用subplot()
plt.subplot(221)
ax1 = plt.subplot(2, 2, 1)  # equivalent but more general
# ax2 = plt.subplot(222, frameon=False)  # add a subplot with no frame
ax2 = plt.subplot(2, 2, 2)
plt.subplot(223, projection='polar')  # add a polar subplot
plt.subplot(224, sharex=ax1, facecolor='red')  # add a red subplot that shares the x-axis with ax1
plt.delaxes(ax2)  # delete ax2 from the figure
plt.subplot(ax2)  # add ax2 to the figure again
plt.show()
