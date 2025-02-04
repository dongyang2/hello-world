# Tensorflow: 实战Google 深度学习框架（第二版） 9.2.2
# Python 3
# coding: UTF-8
import numpy as np


def read_data(path):
    with open(path, 'r', encoding='utf-8') as f:
        id_string = ' '.join([line.strip() for line in f.readlines()])
    id_list = [int(word) for word in id_string.split()]
    return id_list


def make_batches(id_list, batch_size, num_step):
    num_batches = (len(id_list) - 1)//(batch_size*num_step)
    data = np.array(id_list[:num_batches*batch_size*num_step])
    data = np.reshape(data, [batch_size, num_batches*num_step])
    data_batches = np.split(data, num_batches, axis=1)

    # 这里得到的是RNN每一步输出所需要预测的下一个单词
    label = np.array(id_list[1:num_batches*batch_size*num_step+1])
    label = np.reshape(label, [batch_size, num_batches*num_step])
    label_batches = np.split(label, num_batches, axis=1)

    return list(zip(data_batches, label_batches))


if __name__ == '__main__':
    import time
    from language_process.hi_tensorflow import config

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    train_data = config.vocab_output_path['train_vocab']
    train_batch_size = 20
    train_num_step = 35

    train_batches = make_batches(read_data(train_data), train_batch_size, train_num_step)

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
