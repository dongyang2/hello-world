# Tensorflow: 实战Google 深度学习框架（第二版） 9.2.3
# Python 3
# coding: UTF-8
import numpy as np
import tensorflow as tf


class PTBModel(object):

    def __init__(self, is_training, batch_size, num_step) -> None:
        super().__init__()
        self.batch_size = batch_size
        self.num_step = num_step

        # 定义输入和输出的形状和格式
        self.input_data = tf.placeholder(tf.int32, [batch_size, num_step])
        self.target = tf.placeholder(tf.int32, [batch_size, num_step])

        dropout_keep_prob = self.LSTM_KEEP_PROB if is_training else 1.0
        # 造两个一样的层，这种利用 for _ in range(self.NUM_LAYER) 的方法我也是服了
        lstm_cells = [
            tf.nn.rnn_cell.DropoutWrapper(
                tf.nn.rnn_cell.BasicLSTMCell(self.HIDDEN_SIZE),
                output_keep_prob=dropout_keep_prob
            )
            for _ in range(self.NUM_LAYER)
        ]
        cell = tf.nn.rnn_cell.MultiRNNCell(lstm_cells)

        self.initial_state = cell.zero_state(batch_size, tf.float32)

        embedding = tf.get_variable(name='embedding', shape=[self.VOCAB_SIZE, self.HIDDEN_SIZE])

        # 制作embedding —— 将输入单词转为词向量
        inputs = tf.nn.embedding_lookup(embedding, self.input_data)
        if is_training:
            inputs = tf.nn.dropout(inputs, self.EMBEDDING_KEEP_PROB)

    HIDDEN_SIZE = 300
    NUM_LAYER = 2
    VOCAB_SIZE = 10000
    # TRAIN_BATCH_SIZE = 20
    # TRAIN_NUM_STEP = 35
    EVAL_BATCH_SIZE = 1
    EVAL_NUM_STEP = 1
    NUM_EPOCH = 5
    LSTM_KEEP_PROB = 0.9
    EMBEDDING_KEEP_PROB = 0.9
    MAX_GRAD_NORM = 5
    SHARE_EMB_AND_SOFTMAX = True
