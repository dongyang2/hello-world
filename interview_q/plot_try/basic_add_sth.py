# 加了一条虚线，一个标题，加了中文的横纵轴名称

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from matplotlib.ticker import MultipleLocator

x = np.arange(0, 50, 0.1)
y = np.sin(x)
# plt.plot(x, y)

plt.title('sin function')  # 加了标题
ax = plt.axes()

ax.xaxis.set_major_locator(MultipleLocator(5))  # 设置刻度粒度，要导MultipleLocator函数

plt.plot(x, y)
# 加字体了plt才能正确显示中文，title那里也可以加fontproperties
font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)

# 加横纵轴名称
plt.ylabel(u'纵轴', fontproperties=font)
plt.xlabel(u'横轴', fontproperties=font)
# 给图中加一条红色的横线 lw线宽 ls线风格（实线solid、虚线dashed、点线dotted、dashdot虚点混合）
ax.axhline(y=0, color='red', lw=2, ls='dashdot')
# plt.plot(x, y)
plt.show()
