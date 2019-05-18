# Tensorflow: 实战Google 深度学习框架（第二版） 10.2.2 Keras高级用法 第二段代码
# Python 3
# coding: UTF-8
import keras
import numpy as np
import os
from keras.layers import Conv2D, MaxPool2D, Input, concatenate, Dense
from keras.models import Model

os.environ["CUDA_VISIBLE_DEVICES"] = "7"

# 定义输入图像尺寸
input_img = Input(shape=(256, 256, 3))

# 紧接着的是不按照代码顺序排列的网络结构。看这个样子，好像是基于inception结构的改版
tower_1 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_img)
tower_1 = Conv2D(64, (3, 3), padding='same', activation='relu')(tower_1)

tower_2 = Conv2D(64, (1, 1), padding='same', activation='relu')(input_img)
tower_2 = Conv2D(64, (5, 5), padding='same', activation='relu')(tower_2)

tower_3 = MaxPool2D((3, 3), strides=(1, 1), padding='same')(input_img)
tower_3 = Conv2D(64, (1, 1), padding='same', activation='relu')(tower_3)

output = concatenate([tower_1, tower_2, tower_3], axis=1)

# TODO: debug
# 最后是万年不变的结尾，和sklearn似的
predict = Dense(10, activation='softmax')(output)

f = np.load('mnist.npz')
train_x, train_y = f['x_train'], f['y_train']
test_x, test_y = f['x_test'], f['y_test']
f.close()
inputs = Input(shape=(784, ))
model = Model(inputs=inputs, ouputs=predict)
loss = keras.losses.categorical_crossentropy
optimizer = keras.optimizers.SGD()
model.compile(optimizer, loss, metrics=['accuracy'])
model.fit(train_x, train_y, batch_size=128, epochs=20, validation_data=(test_x, test_y))
