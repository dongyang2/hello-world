# 使用基于slim的VGG16预训练模型得到图片特征
import tensorflow.contrib.slim as slim
import tensorflow as tf
import numpy as np
import os
os.environ["CUDA_VISIBLE_DEVICES"] = "4"
import sys
# sys.path.append('..')
# from pwa import vgg


def vgg_16(inputs,
           num_classes=1000,
           is_training=True,
           dropout_keep_prob=0.5,
           spatial_squeeze=True,
           scope='vgg_16',
           fc_conv_padding='VALID',
           global_pool=False):
    """Oxford Net VGG 16-Layers version D Example.
    Note: All the fully_connected layers have been transformed to conv2d layers.
          To use in classification mode, resize input to 224x224.
    Args:
      inputs: a tensor of size [batch_size, height, width, channels].
      num_classes: number of predicted classes. If 0 or None, the logits layer is
        omitted and the input features to the logits layer are returned instead.
      is_training: whether or not the out is being trained.
      dropout_keep_prob: the probability that activations are kept in the dropout
        layers during training.
      spatial_squeeze: whether or not should squeeze the spatial dimensions of the
        outputs. Useful to remove unnecessary dimensions for classification.
      scope: Optional scope for the variables.
      fc_conv_padding: the type of padding to use for the fully connected layer
        that is implemented as a convolutional layer. Use 'SAME' padding if you
        are applying the network in a fully convolutional manner and want to
        get a prediction map downsampled by a factor of 32 as an output.
        Otherwise, the output prediction map will be (input / 32) - 6 in case of
        'VALID' padding.
      global_pool: Optional boolean flag. If True, the input to the classification
        layer is avgpooled to size 1x1, for any input size. (This is not part
        of the original VGG architecture.)
    Returns:
      net: the output of the logits layer (if num_classes is a non-zero integer),
        or the input to the logits layer (if num_classes is 0 or None).
      end_points: a dict of tensors with intermediate activations.
    """
    with tf.variable_scope(scope, 'vgg_16', [inputs]) as sc:
        end_points_collection = sc.original_name_scope + '_end_points'
        # Collect outputs for conv2d, fully_connected and max_pool2d.
        with slim.arg_scope([slim.conv2d, slim.fully_connected, slim.max_pool2d],
                            outputs_collections=end_points_collection):
            net = slim.repeat(inputs, 2, slim.conv2d, 64, [3, 3], scope='conv1')
            net = slim.max_pool2d(net, [2, 2], scope='pool1')
            net = slim.repeat(net, 2, slim.conv2d, 128, [3, 3], scope='conv2')
            net = slim.max_pool2d(net, [2, 2], scope='pool2')
            net = slim.repeat(net, 3, slim.conv2d, 256, [3, 3], scope='conv3')
            net = slim.max_pool2d(net, [2, 2], scope='pool3')
            net = slim.repeat(net, 3, slim.conv2d, 512, [3, 3], scope='conv4')
            net = slim.max_pool2d(net, [2, 2], scope='pool4')
            net = slim.repeat(net, 3, slim.conv2d, 512, [3, 3], scope='conv5')
            net = slim.max_pool2d(net, [2, 2], scope='pool5')

            # if num_classes == 0:
            #     return net

            # Use conv2d instead of fully_connected layers.
            net = slim.conv2d(net, 4096, [7, 7], padding=fc_conv_padding, scope='fc6')
            net = slim.dropout(net, dropout_keep_prob, is_training=is_training,
                               scope='dropout6')
            net = slim.conv2d(net, 4096, [1, 1], scope='fc7')
            # Convert end_points_collection into a end_point dict.
            end_points = slim.utils.convert_collection_to_dict(end_points_collection)
            if global_pool:
                net = tf.reduce_mean(net, [1, 2], keep_dims=True, name='global_pool')
                end_points['global_pool'] = net
            if num_classes:
                net = slim.dropout(net, dropout_keep_prob, is_training=is_training,
                                   scope='dropout7')
                net = slim.conv2d(net, num_classes, [1, 1],
                                  activation_fn=None,
                                  normalizer_fn=None,
                                  scope='fc8')
                if spatial_squeeze:
                    net = tf.squeeze(net, [1, 2], name='fc8/squeezed')
                end_points[sc.name + '/fc8'] = net
            return net, end_points


def vgg_arg_scope(weight_decay=0.0005):
    """Defines the VGG arg scope.
    Args:
      weight_decay: The l2 regularization coefficient.
    Returns:
      An arg_scope.
    """
    with slim.arg_scope([slim.conv2d, slim.fully_connected],
                        activation_fn=tf.nn.relu,
                        weights_regularizer=slim.l2_regularizer(weight_decay),
                        biases_initializer=tf.zeros_initializer()):
        with slim.arg_scope([slim.conv2d], padding='SAME') as arg_sc:
            return arg_sc


if __name__ == '__main__':
    import scipy.misc as misc

    batch_size = 1
    image_size = 224
    num_channel = 3

    this_path = sys.path[0]
    pic_path = this_path+'/'+'1523.jpg'
    m_img = misc.imread(pic_path)
    resize_img = tf.image.resize_images(m_img, [image_size, image_size])

    with slim.arg_scope(vgg_arg_scope()):  # 开始创建网络，使用VGG作者已经固定的一些网络参数

        x = tf.placeholder(tf.float32,  # 指定输入格式
                           shape=(
                               batch_size,
                               image_size,
                               image_size,
                               num_channel
                           ), name='x-input')

        out, _ = vgg_16(x,
                        num_classes=0,  # 置0则输出特征
                        is_training=False
                        )

        res = tf.arg_max(out, 1)  # 指定一个可以让session run的东西

        # model_path = "../pwa/vgg_16.ckpt"  # 绝对路径用来以防万一  # dl2
        model_path = "../pwa/vgg_16.ckpt"  # dl5

        # exclude参数可以选择除去哪几层的变量名
        variables_to_restore = slim.get_variables_to_restore(exclude=['fc6', 'fc7', 'fc8'])
        # print(variables_to_restore)

        # 各张量的名字，比下面两个好用
        # from tensorflow.python import pywrap_tensorflow
        # reader = pywrap_tensorflow.NewCheckpointReader(model_path)
        # var_to_shape_map = reader.get_variable_to_shape_map()
        # for key in var_to_shape_map:
        #     print(key)

        saver = tf.train.Saver(variables_to_restore)
        with tf.Session() as sess:
            saver.restore(sess, model_path)  # 把保存的模型读到会话里

            graph = tf.get_default_graph()

            # 为了打印各变量和各层的名字
            for key in graph.get_all_collection_keys():
                print(key, graph.get_collection(key))

            img_np = sess.run(resize_img)  # 把tensor转化为numpy格式
            # print(np.array([img_np]).shape)

            # 获得图中各张量名字
            # li1 = [n.name for n in tf.get_default_graph().as_graph_def().node]
            # for i1 in li1:
            #     print(i1)

            c = sess.run(out, feed_dict={'x-input:0': [img_np]})  # 这里必须写x-input:0,不能写x-input
            fe = sess.run([graph.get_tensor_by_name("vgg_16/conv2/conv2_1/weights:0"),
                           # graph.get_tensor_by_name("vgg_16/conv3/conv3_1/weights:0"),
                           # graph.get_tensor_by_name("vgg_16/conv1/conv1_1/weights:0"),
                           # graph.get_tensor_by_name("vgg_16/conv4/conv4_1/weights:0"),
                           # graph.get_tensor_by_name("vgg_16/conv5/conv5_3/weights:0"),
                           graph.get_tensor_by_name("vgg_16/pool5/MaxPool:0"),
                           graph.get_tensor_by_name('vgg_16/conv5/conv5_2/weights:0')],
                          feed_dict={'x-input:0': [img_np]})
            for i2 in fe:
                print(i2.shape, end=' ')
            np.save(this_path+'/1523_fe', fe[1])
            # print(c.shape)
