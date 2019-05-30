# Tensorflow: 实战Google深度学习框架（第二版） 10.2.2 Keras高级用法 第二段代码
# 先是探索了怎样批量预处理，发现预处理时可以顺便产生batch，
# 然后查看inception原论文获知得到filter concat之后怎么操作
# 最后仍然报错Axis must be specified when shapes of a and weights differ.
# 放弃了，直接把源数据放入，不手动分batch
# Python 3
# coding: UTF-8
import keras
import numpy as np
import os
from keras.layers import Conv1D, MaxPool1D, Input, concatenate, Dense, Flatten
from keras.models import Model
from computer_vision.hi_keras.dataset import resize
from keras.utils import np_utils
from keras import backend as bke

os.environ["CUDA_VISIBLE_DEVICES"] = "7"

num_classes = 10
epochs = 5
batch_size = 128
image_size = (256, 256)

# 书上的结构
# from keras.layers import Conv2D, MaxPool2D
# # 定义输入图像尺寸
# input_img = Input(shape=(256, 256, 3))
#
# # 紧接着的是不按照代码顺序排列的网络结构。看这个样子，好像是基于inception结构的改版
# tower_1 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_img)
# tower_1 = Conv2D(64, (3, 3), padding='same', activation='relu')(tower_1)
#
# tower_2 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_img)
# tower_2 = Conv2D(64, (5, 5), padding='same', activation='relu')(tower_2)
#
# tower_3 = MaxPool2D((3, 3), strides=(1, 1), padding='same')(input_img)
# tower_3 = Conv2D(64, (1, 1), padding='same', activation='relu')(tower_3)

# inception的mnist改版
input_img = Input(shape=image_size)
tower_1 = Conv1D(64, 1, padding='same', activation='relu')(input_img)
tower_1 = Conv1D(64, 3, padding='same', activation='relu')(tower_1)

tower_2 = Conv1D(64, 1, padding='same', activation='relu')(input_img)
tower_2 = Conv1D(64, 5, padding='same', activation='relu')(tower_2)

tower_3 = MaxPool1D(3, 1, 'same')(input_img)
tower_3 = Conv1D(64, 1, padding='same', activation='relu')(tower_3)
feature = concatenate([tower_1, tower_2, tower_3], axis=1)

# 最后是分类器结构
feature = Flatten()(feature)
predict = Dense(10, activation='softmax')(feature)

# 接下来就和sklearn似的
model = Model(inputs=input_img, outputs=predict)

loss = keras.losses.categorical_crossentropy
optimizer = keras.optimizers.SGD()
model.compile(optimizer, loss, metrics=['accuracy'])

# 加载数据。下载地址 https://s3.amazonaws.com/img-datasets/mnist.npz
f = np.load('mnist.npz')
train_x, train_y = f['x_train'], f['y_train']
test_x, test_y = f['x_test'], f['y_test']
f.close()

# model.fit(train_x, train_y, batch_size=128, epochs=20, validation_data=(test_x, test_y))

# 预处理
train_x = np.array([resize(x, image_size) for x in train_x])
test_x = np.array([resize(x, image_size) for x in test_x])
print('-'*20, 'Resize completed.', '-'*20)
# 把类标改一下以放入loss
train_y = np_utils.to_categorical(train_y)
test_y = np_utils.to_categorical(test_y)

model.fit(train_x, train_y,
          batch_size,
          epochs,
          verbose=0,
          validation_data=(test_x, test_y))
bke.clear_session()  # 报错。手动清理一下。我也不清楚无法自动清除的原因，反正垃圾Keras
