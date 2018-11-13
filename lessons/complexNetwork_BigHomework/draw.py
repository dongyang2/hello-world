import matplotlib.pyplot as plt
import matplotlib.pylab as py_lab
import numpy as np
# import matplotlib.ticker as m_tick


def line_picture(x, y, xl, yl):
    param = {
        'axes.labelsize': '20',
        'figure.figsize': '12, 9'
    }
    py_lab.rcParams.update(param)
    # y2 = [0, 0.014, 0.03, 0.16, 0.37, 0.78, 0.81, 0.83, 0.86, 0.92]

    plt.plot(x, y)
    # plt.plot(x1, y2)

    ps = plt.subplot(111)
    # axes.set_yticks([0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0])
    ps.grid(True)

    plt.legend(loc="lower right")  # set legend location
    plt.ylabel(yl)
    plt.xlabel(xl)

    plt.show()


def histogram_picture(y, xl, yl):
    params = {
        'axes.labelsize': '20',
        'lines.linewidth': 2,
        'figure.figsize': '24, 9'
    }
    py_lab.rcParams.update(params)

    # y1 = [9.79,7.25,7.24,4.78,4.20]
    # y2 = [5.88,4.55,4.25,3.78,3.92]
    # ind = np.arange(5)              # x轴的数字
    # width = 0.20
    # plt.bar(ind, y)
    # plt.bar(ind+width,y2,width,color = 'g',label = 'm=4')

    x = np.arange(len(y))
    plt.bar(x, y)
    plt.xlabel(xl)
    plt.ylabel(yl)

    # pg = plt.gca()
    # pg.grid(True)
    plt.legend(loc="upper right")

    plt.show()
