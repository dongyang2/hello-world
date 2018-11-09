# 数据预处理之 插入缺失值
import numpy as np

from sklearn.datasets import load_boston
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import Imputer
from sklearn.model_selection import cross_val_score

random = np.random.RandomState(0)

dataset = load_boston()
X_full, y_full = dataset.data, dataset.target
n_samples = X_full.shape[0]  # 行数
n_origin_data = X_full.shape[1]  # 列数

# Estimate the score on the entire dataset, with no missing values
estimator = RandomForestRegressor(random_state=0, n_estimators=100)
score = cross_val_score(estimator, X_full, y_full).mean()
print("Score with the entire dataset = %.2f" % score)  # 0.56

# Add missing values in 75% of the lines
missing_rate = 0.75
n_missing_samples = int(np.floor(n_samples * missing_rate))  # 缺失值的数量
missing_samples = np.hstack((np.zeros(n_samples - n_missing_samples,
                                      dtype=np.bool),
                             np.ones(n_missing_samples,
                                     dtype=np.bool)))  # 先水平堆叠按比例获得的True和False
random.shuffle(missing_samples)  # 再打乱，从而制造缺失值的选择
missing_features = random.randint(0, n_origin_data, n_missing_samples)  # 生成n_missing_samples个在[0,n_origin_data)区间的整数

# Estimate the score without the lines containing missing values
# 获得造出的有缺失值的数据，会丢弃很多行
X_filtered = X_full[~missing_samples, :]  # X_full[~missing_samples, :]这个用法很有意思，这用法只能用于numpy.array
y_filtered = y_full[~missing_samples]
estimator_RF = RandomForestRegressor(random_state=0, n_estimators=100)
# score = cross_val_score(estimator_RF, X_filtered, y_filtered).mean()
# print("Score without the samples containing missing values = %.2f" % score)  # 0.48

# Estimate the score after imputation of the missing values
X_missing = X_full.copy()
X_missing[np.where(missing_samples)[0], missing_features] = 0
y_missing = y_full.copy()
estimator_imp_rf = Pipeline([("imputer", Imputer(missing_values=0,
                                                 strategy="mean",
                                                 axis=0)),
                             ("forest", RandomForestRegressor(random_state=0,
                                                              n_estimators=100))])
score_imp = cross_val_score(estimator_imp_rf, X_missing, y_missing).mean()
print("Score after imputation of the missing values = %.2f" % score_imp)  # 0.57

# 整篇代码看下来，我觉得似乎写的不对，34，35行造出的有缺失值的数据，其实缺失的是样本数量（即去除了很多行），而不是在每一个样本中制造缺失值
# 所以我觉得代码应该这样写（此处先注释掉了37，38行）
score_missing = cross_val_score(estimator_RF, X_missing, y_missing).mean()
print("Score without the samples containing missing values = %.2f" % score_missing)  # 0.52
