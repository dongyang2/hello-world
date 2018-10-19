import time


def train(train_data_path, val_data_path):
    # di = train_data_path.split('/')[:-1][0]
    # di_mod = di + '/fastText.model'

    import fastText
    # 训练模型
    classifier = fastText.train_supervised(train_data_path, label="__label__")

    # load训练好的模型
    # classifier = fastText.load_model(mod_path)

    result = classifier.test(val_data_path)
    print(result)
    # print(result.recall)
    # return classifier


if __name__ == '__main__':
    t_path1 = 'H:\DF_emotion/train.txt'
    v_path1 = 'H:\DF_emotion/test.txt'
    train(t_path1, v_path1)

    print('df_train', time.ctime())
