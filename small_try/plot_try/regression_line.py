# 输入一串二元组或者横纵坐标，得到一条“平滑的”曲线。

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

import numpy as np
from sklearn.linear_model import LinearRegression

# 下面是横纵坐标的例子
x = [25, 26, 27, 38, 40, 45, 46, 52, 54, 62, 66, 67, 69, 74, 81, 83, 88, 96, 102]
y = [136.3, 135.2, 135.0, 133.0, 134.4, 133.1, 133.7, 133.2, 132.5, 130.7, 132.0, 130.8, 129.8, 130.2, 129.5, 129.8,
     129.6, 129.1, 128.1]
x = np.array(x)
y = np.array(y)
# print(x.shape, y.shape)

lr = LinearRegression()
lr.fit(x.reshape(-1, 1), y)  # reshape(-1, 1)把一行n列转化为n行一列


# fig = plt.figure()
# plt.plot(x, y, 'r.', markersize=12)
# plt.plot(x, lr.predict(x[:, np.newaxis]), 'b-')
# axes = plt.gca()
# # axes.set_xlim([xmin,xmax])
# axes.set_ylim([100, 150])  # 加入对横纵轴坐标区间的限制
# plt.legend(('Data', 'Linear Fit'), loc='lower right')
# plt.title('Isotonic regression')
# plt.show()


def transform(date=0, num=0):
    # 9月1日等于1,10月1日等于31,12月11日等于102
    li = [30, 31, 30, 31, 31, 28, 31, 30, 31, 30, 31, 31]
    month = 9
    if date == 0:
        i = 0
        while num - li[i] > 0:
            num = num - li[i]
            month += 1
            if month == 13:
                month = 1
            i += 1
            if i == 11:
                i = 0

        return month * 100 + num

    if num == 0:
        h = int(date / 100)
        if h < 9:
            h += 12
        day = date % 100
        result = 0
        for i in range(h-month):
            result += li[i]
        return result + day


y_target = 110

future_data_num = np.arange(103, 303)
f_y = lr.predict(future_data_num.reshape(-1, 1))
target = future_data_num[f_y < y_target+1]
print(transform(num=target[0]))

new_x = np.append(x, future_data_num)  # 补充的后面的线条的横坐标
fig = plt.figure()
plt.plot(x, y, 'r.', markersize=12)
plt.plot(new_x, lr.predict(new_x[:, np.newaxis]), 'b-')
axes = plt.gca()
axes.set_ylim([100, 150])  # 加入对横纵轴坐标区间的限制
ax = plt.axes()
ax.xaxis.set_major_locator(MultipleLocator(30))
plt.legend(('Data', 'Linear Fit'), loc='lower right')
plt.title('Isotonic regression')
plt.show()
