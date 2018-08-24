import tensorflow as tf
import os
import sys
import numpy as np
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D, MaxPooling2D, ZeroPadding2D, Reshape
from keras.layers import Activation, Dropout, Flatten, Dense
from keras import backend as bk
import h5py


def test():
    hello = tf.constant('Hello, TensorFlow!')
    sess = tf.Session()
    print(sess.run(hello))

    a = tf.constant(10)
    b = tf.constant(32)
    print(sess.run(a+b))


def generate_input():
    train_data_gen = ImageDataGenerator(
        # rotation_range=40,
        # width_shift_range=0.2,
        # height_shift_range=0.2,
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
    path_train = 'H:/infosec/train_image'
    path_validate = 'H:/infosec/validate_image'
    mod = Sequential()
    generator = train_data_gen.flow_from_directory(path_train, class_mode=None, shuffle=False)
    np_arr_train = mod.predict_generator(generator, 2000, use_multiprocessing=True)  # 取2千图片
    f_t = open('H:/infosec/train.npy', 'w')
    np.save(f_t, np_arr_train)
    f_t.close()

    validate_gen = ImageDataGenerator(rescale=1. / 255)
    generator = validate_gen.flow_from_directory(path_validate, class_mode=None)
    np_arr_val = mod.predict_generator(generator, 800)
    f_v = open('H:/infosec/validate.npy', 'w')
    np.save(f_v, np_arr_val)
    f_v.close()


if __name__ == '__main__':
    # test()
    # generate_input()

    img_width, img_height = 384, 384

    train_data_dir = 'H:/infosec/train_image'
    validation_data_dir = 'H:/infosec/validate_image'

    input_shape = (img_width, img_height, 1)

    model = Sequential()
    model.add(Convolution2D(32, (3, 3), input_shape=input_shape))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    # print(model.output_shape)

    model.add(Convolution2D(32, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))

    model.add(Convolution2D(64, (3, 3)))
    model.add(Activation('relu'))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    # model.add(Dropout(0.25))

    model.add(Flatten())
    # model.add(Dense(64, activation='relu'))
    # model.add(Dense(256, activation='relu'))
    model.add(Dense(512, activation='relu'))
    model.add(Dropout(0.5))

    # model.add(Dense(64, activation='relu'))
    # model.add(Dropout(0.5))

    # model.add(Reshape((9, )))
    model.add(Dense(9, activation='softmax'))
    # model.add(Activation('sigmoid'))

    model.compile(loss='binary_crossentropy',
                  # optimizer='rmsprop',
                 optimizer='adam',
                  metrics=['accuracy'])

    # this is the augmentation configuration we will use for training
    train_data_gen = ImageDataGenerator(
        rescale=1. / 255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

    # this is the augmentation configuration we will use for testing:
    # only rescaling
    val_data_gen = ImageDataGenerator(rescale=1. / 255)

    train_generator = train_data_gen.flow_from_directory(
        train_data_dir,
        target_size=(img_width, img_height),
        color_mode='grayscale',
        # class_mode='sparse'
        class_mode='categorical'
    )

    validation_generator = val_data_gen.flow_from_directory(
        validation_data_dir,
        target_size=(img_width, img_height),
        color_mode='grayscale',
        # class_mode='sparse'
        class_mode='categorical')

    model.fit_generator(
        train_generator,
        steps_per_epoch=20,
        epochs=50,
        validation_data=validation_generator,
        validation_steps=50
    )

    model.save_weights('fifth_try.h5')
    # score = model.evaluate(x_test, y_test, batch_size=128)
