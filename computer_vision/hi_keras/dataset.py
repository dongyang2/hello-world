import keras
from skimage import transform
import numpy as np
from keras.utils import np_utils


def resize(img, shape):
    return transform.resize(img, output_shape=shape)


class DataGenerator(keras.utils.Sequence):
    def __init__(self, data, labels, bs, shape=(224, 224)):
        """
        :param data:   数据
        :param labels: 数据对应的类标
        :param bs:     一个batch的大小
        :param shape:  指定修改后的图片尺寸
        """
        self.data = data
        self.batch_size = bs
        self.labels = labels
        self.shape = shape

    def __len__(self):
        """The number of batches in the Sequence"""
        return int(np.floor(len(self.labels) / self.batch_size))

    def __getitem__(self, index):
        """
        :param index:  当前batch的序号

        :return: 由index指定的一个batch的数据
        """
        batch_x = self.data[index * self.batch_size:(index + 1) * self.batch_size]
        batch_y = self.labels[index * self.batch_size:(index + 1) * self.batch_size]
        data = np.array([resize(x, self.shape) for x in batch_x])
        label = np.array(batch_y)

        return data, np_utils.to_categorical(label)

    def on_epoch_end(self):
        pass
