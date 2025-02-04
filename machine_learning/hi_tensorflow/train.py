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
        # 造两个一样的层，这种利用 for _ in range(self.NUM_LAYER) 的方法我也是服了，真厉害
        lstm_cells = [
            tf.nn.rnn_cell.DropoutWrapper(
                tf.nn.rnn_cell.BasicLSTMCell(self.HIDDEN_SIZE),
                output_keep_prob=dropout_keep_prob
            )
            for _ in range(self.NUM_LAYER)
        ]
        cell = tf.nn.rnn_cell.MultiRNNCell(lstm_cells)  # 将LSTM用作RNN的中间结构

        self.initial_state = cell.zero_state(batch_size, tf.float32)

        embedding = tf.get_variable(name='embedding', shape=[self.VOCAB_SIZE, self.HIDDEN_SIZE])

        # 制作embedding —— 将输入单词转为词向量
        inputs = tf.nn.embedding_lookup(embedding, self.input_data)
        if is_training:
            inputs = tf.nn.dropout(inputs, self.EMBEDDING_KEEP_PROB)

        outputs = []
        state = self.initial_state
        with tf.variable_scope('RNN'):
            for time_step in range(num_step):
                if time_step > 0:
                    tf.get_variable_scope().reuse_variables()
                cell_output, state = cell(inputs[:, time_step, :], state)
                outputs.append(cell_output)
        output = tf.reshape(tf.concat(outputs, 1), [-1, self.HIDDEN_SIZE])

        # softmax层，将RNN在每个位置上的输出转为各个单词的logits
        if self.SHARE_EMB_AND_SOFTMAX:
            weight = tf.transpose(embedding)
        else:
            weight = tf.get_variable('weight', [self.HIDDEN_SIZE, self.VOCAB_SIZE])
        bias = tf.get_variable('bias', [self.VOCAB_SIZE])
        logits = tf.matmul(output, weight) + bias

        # 定义交叉熵损失和其平均损失
        loss = tf.nn.sparse_softmax_cross_entropy_with_logits(
            labels=tf.reshape(self.target, [-1]),
            logits=logits
        )
        self.cost = tf.reduce_sum(loss) / batch_size
        self.final_state = state

        # 不是训练时就不做反向传播
        if not is_training:
            return

        trainable_variables = tf.trainable_variables()
        grads, _ = tf.clip_by_global_norm(tf.gradients(self.cost, trainable_variables), self.MAX_GRAD_NORM)
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=1.0)
        self.train_op = optimizer.apply_gradients(zip(grads, trainable_variables))

    HIDDEN_SIZE = 300
    NUM_LAYER = 2
    VOCAB_SIZE = 10000
    LSTM_KEEP_PROB = 0.9
    EMBEDDING_KEEP_PROB = 0.9
    MAX_GRAD_NORM = 5
    SHARE_EMB_AND_SOFTMAX = True


def run_epoch(session, model, batches, train_op, output_log, step):
    total_cost = 0.0
    iters = 0
    # perplexity = 0.0
    state = session.run(model.initial_state)
    for x, y in batches:
        cost, state, _ = session.run(
            [model.cost, model.initial_state, train_op],
            {model.input_data: x, model.target: y, model.initial_state: state}
        )
        total_cost += cost
        iters += model.num_step

        if output_log and step % 100 == 0:
            perplexity = np.exp(total_cost / iters)
            print('After %d steps, perplexity is %.3f' % (step, perplexity))
        step += 1
    perplexity = np.exp(total_cost / iters)

    return step, perplexity


if __name__ == '__main__':
    import time
    import os
    from language_process.hi_tensorflow import config
    from language_process.hi_tensorflow.batching import read_data, make_batches

    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')
    # # tensorflow使用CPU. i5-5300U 一个epoch需要超过1h10min，总的算来需要超过6小时
    # os.environ["CUDA_DEVICE_ORDER"] = "PCI_BUS_ID"
    # os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

    # 1080 Ti 12G  16min
    os.environ["CUDA_VISIBLE_DEVICES"] = "7"

    train_data = config.vocab_output_path['train_vocab']
    val_data = config.vocab_output_path['valid_vocab']
    test_data = config.vocab_output_path['test_vocab']

    TRAIN_BATCH_SIZE = 20
    TRAIN_NUM_STEP = 35
    EVAL_BATCH_SIZE = 1
    EVAL_NUM_STEP = 1
    NUM_EPOCH = 5

    initializer = tf.random_uniform_initializer(-0.05, 0.05)  # 生成均匀分布的随机数

    with tf.variable_scope('language_model', reuse=None, initializer=initializer):
        train_model = PTBModel(True, TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)

    with tf.variable_scope('language_model', reuse=True, initializer=initializer):
        eval_model = PTBModel(False, EVAL_BATCH_SIZE, EVAL_NUM_STEP)

    with tf.Session() as sess:
        tf.global_variables_initializer().run()
        train_batches = make_batches(read_data(train_data), TRAIN_BATCH_SIZE, TRAIN_NUM_STEP)
        eval_batches = make_batches(read_data(val_data), EVAL_BATCH_SIZE, EVAL_NUM_STEP)
        test_batches = make_batches(read_data(test_data), EVAL_BATCH_SIZE, EVAL_NUM_STEP)

        step_train = 0
        for epoch in range(NUM_EPOCH):
            print('In epoch %d' % (epoch+1))
            step_train, train_pplx = run_epoch(sess, train_model, train_batches, train_model.train_op, True, step_train)
            print('Train perplexity: %.3f' % train_pplx)

            # 居然还有tf.no_op()这种操作
            _, eval_pplx = run_epoch(sess, eval_model, eval_batches, tf.no_op(), False, 0)
            print('Evaluation perplexity: %.3f' % eval_pplx)

    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
