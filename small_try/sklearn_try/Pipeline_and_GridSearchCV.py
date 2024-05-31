# 一个pipeline和gridSearch结合的示例，用于给PCA和卡方校验寻参。
# This example constructs a pipeline that does dimensionality reduction followed by prediction with
# a support vector classifier. It demonstrates the use of GridSearchCV and Pipeline to optimize over
# different classes of estimators in a single CV run – unsupervised PCA and NMF dimensionality reductions
# are compared to univariate feature selection during the grid search.

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits  # 也是一个手写数字数据集
from sklearn.model_selection import GridSearchCV
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.decomposition import PCA, NMF
from sklearn.feature_selection import SelectKBest, chi2
from matplotlib.ticker import MultipleLocator


pipe = Pipeline([
    ('reduce_dim', PCA()),
    ('classify', LinearSVC())
])

N_FEATURES_OPTIONS = [2, 4, 8]
C_OPTIONS = [1, 10, 100, 1000]
param_grid = [
    {
        'reduce_dim': [PCA(iterated_power=7), NMF()],
        'reduce_dim__n_components': N_FEATURES_OPTIONS,
        'classify__C': C_OPTIONS
    },
    {
        'reduce_dim': [SelectKBest(chi2)],
        'reduce_dim__k': N_FEATURES_OPTIONS,
        'classify__C': C_OPTIONS
    },
]
reducer_labels = ['PCA', 'NMF', 'KBest(chi2)']

grid = GridSearchCV(pipe, cv=3, n_jobs=1, param_grid=param_grid)
digits = load_digits()  # DESCR, images (1797,8,8), data (1797,64), target (1797,), target_names (10,)
# 使用gridSearchCV这个函数返回的变量就能直接fit
grid.fit(digits.data, digits.target)

mean_scores = np.array(grid.cv_results_['mean_test_score'])  # 这里cv_result_返回的是list类型
# scores are in the order of param_grid iteration, which is alphabetical
mean_scores = mean_scores.reshape(len(C_OPTIONS), -1, len(N_FEATURES_OPTIONS))  # 这里把每九个分为一个3*3二维数组 shape 3*3*4
# select score for best C
mean_scores = mean_scores.max(axis=0)  # 取每个3*3二维数组里对应位置最大的那个数值，一共取9个数字。比如shape 3*3*100的执行这句脚本也是输出3*3的
bar_offsets = (np.arange(len(N_FEATURES_OPTIONS)) * (len(reducer_labels) + 1) + .5)  # 每个柱状图的开始X坐标

plt.figure()
COLORS = 'bgrcmyk'
for i, (label, reducer_scores) in enumerate(zip(reducer_labels, mean_scores)):
    plt.bar(bar_offsets + i, reducer_scores, label=label, color=COLORS[i])

ax = plt.axes()
plt.title("Comparing feature reduction techniques")
plt.xlabel('Reduced number of features')
ax.xaxis.set_major_locator(MultipleLocator(1))
# plt.xticks(bar_offsets + len(reducer_labels) / 2, N_FEATURES_OPTIONS)
plt.ylabel('Digit classification accuracy')
plt.ylim((0, 1))
plt.legend(loc='upper left')
plt.show()
