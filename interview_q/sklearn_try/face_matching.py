# 下半脸填充，四个模型根据训练数据去预测给定上半脸的下半脸是什么样的
# This example shows the use of multi-output estimator to complete images. The goal is to predict the lower half of a
# face given its upper half.
# The first column of images shows true faces. The next columns illustrate how extremely randomized trees, k nearest
# neighbors, linear regression and ridge regression complete the lower half of those faces.
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces  # C:\Users\Username\scikit_learn_data\olivetti_py3.pkz
from sklearn.utils.validation import check_random_state

from sklearn.ensemble import ExtraTreesRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV

# 读到的是一个dict，四个键——DESCR,target,data,images.
# DESCR是describe的简写，可以print出来。target应该是类似于索引的东西，因为一共是40个图片，一个图片对应十个一模一样的索引。
# images就是那40张图片，data似乎是把images里的每张图片给展平了。
# target.shape (400,)  data.shape (400, 4096)  images.shape (400, 64, 64)
data = fetch_olivetti_faces()
# targets = data.target
# data = data.images.reshape((len(data.images), -1))  # 经我测试，这里得到的结果就是data.data
# 这里有2个numpy知识点，一是targets<30得到的是一个充满True和False的一维数组，二是把true和false的数组作用于其他数组可以起到挑选作用
# 那么问题来了，直接data.data[:300]岂不美滋滋，官方代码就是喜欢充狠
# train = data.data[targets < 30]  # shape (300, 4096)
# test = data.data[targets >= 30]  # Test on independent people  # shape (100, 4096)
train = data.data[:300]  # shape (300, 4096)
test = data.data[300:]  # shape (100, 4096)

# Test on a subset of people
n_faces = 5
rng = check_random_state(4)
# face_ids = rng.randint(test.shape[0], size=(n_faces, ))  # 这里randint函数如果只给一个数，则将其当上界，两个数则当成上下界
# test = test[face_ids, :]  # 随机选了5行，又装，强行加冒号，哎~sklearn官方货······
face_ids = rng.randint(test.shape[0], size=n_faces)
test_sub = test[face_ids]  # shape (5, 4096)

n_pixels = data.data.shape[1]  # 4096
# Upper half of the faces
X_train = train[:, :(n_pixels + 1) // 2]  # +1再除以2是为了保证鲁棒性，这样永远都是除以二向上取整
X_test = test[:, :(n_pixels + 1) // 2]

# Lower half of the faces
y_train = train[:, n_pixels // 2:]
y_test = test[:, n_pixels // 2:]

# Fit estimators
ESTIMATORS = {
    "Extra trees": ExtraTreesRegressor(n_estimators=10, max_features=32,
                                       random_state=0),  # 极端随机森林回归
    "K-nn": KNeighborsRegressor(),
    "Linear regression": LinearRegression(),
    "Ridge": RidgeCV(),  # 带有交叉验证的岭回归
}

y_test_predict = dict()
for name, estimator in ESTIMATORS.items():  # 训练好几个模型，得到好几个结果，存起来
    estimator.fit(X_train, y_train)
    y_test_predict[name] = estimator.predict(X_test)

# Plot the completed faces
image_shape = (64, 64)

n_cols = 1 + len(ESTIMATORS)
plt.figure(figsize=(2. * n_cols, 2.26 * n_faces))
plt.title("Face completion with multi-output estimators", size=16)
# plt.suptitle("Face completion with multi-output estimators", size=16)

for i in range(n_faces):
    true_face = np.hstack((X_test[i], y_test[i]))

    if i:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1)
    else:
        sub = plt.subplot(n_faces, n_cols, i * n_cols + 1,
                          title="true faces")

    sub.axis("off")
    sub.imshow(true_face.reshape(image_shape),
               cmap=plt.cm.gray,
               interpolation="nearest")

    for j, est in enumerate(sorted(ESTIMATORS)):
        completed_face = np.hstack((X_test[i], y_test_predict[est][i]))

        if i:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j)

        else:
            sub = plt.subplot(n_faces, n_cols, i * n_cols + 2 + j,
                              title=est)

        sub.axis("off")
        sub.imshow(completed_face.reshape(image_shape),
                   cmap=plt.cm.gray,
                   interpolation="nearest")

plt.show()
