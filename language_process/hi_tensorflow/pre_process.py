# Tensorflow: 实战Google 深度学习框架（第二版） 9.2.1
# Python 3
# coding: UTF-8
import codecs
import collections
from operator import itemgetter


def make_mapping_table(path, to_path):
    # 按照词频顺序将单词映射为数字，并将该映射表保存为文件
    counter = collections.Counter()
    with codecs.open(path, 'r', 'utf-8') as f:
        for line in f:
            for word in line.strip().split():
                counter[word] += 1

    # 按词频对单词进行排序
    sort_word_to_cnt = sorted(counter.items(), key=itemgetter(1), reverse=True)
    sorted_word = [x[0] for x in sort_word_to_cnt]

    # 将句子结束符加入词汇映射表
    sorted_word = ['<eos>'] + sorted_word
    with codecs.open(to_path, 'w', 'utf-8') as fo:
        for word in sorted_word:
            fo.write(word + '\n')


def get_id(word, dic):
    return dic[word] if word in dic else dic['<unk>']


def mapping_save(vocab_path, raw_data_path, to_path):
    with codecs.open(vocab_path, 'r', 'utf-8') as f:
        vocab = [w.strip() for w in f.readlines()]
    word_to_id = {k: v for (k, v) in zip(vocab, range(len(vocab)))}

    fin = codecs.open(raw_data_path, 'r', 'utf-8')
    fout = codecs.open(to_path, 'w', 'utf-8')
    for line in fin:
        words = line.strip().split() + ['<eos>']
        write_line = ' '.join([str(get_id(w, word_to_id)) for w in words])
        fout.write(write_line)
    fin.close()
    fout.close()


if __name__ == '__main__':
    import time
    from language_process.hi_tensorflow import config
    print('-' * 15, 'Start', time.ctime(), '-' * 15, '\n')

    RAW_DATA = config.data_path['train']
    VOCAB = config.vocab_output_path['vocab']

    make_mapping_table(RAW_DATA, VOCAB)

    VOCAB_OUTPUT_TRAIN = config.vocab_output_path['train_vocab']

    mapping_save(VOCAB, RAW_DATA, VOCAB_OUTPUT_TRAIN)
    RAW_TEST_DATA = config.data_path['test']
    RAW_VAL_DATA = config.data_path['valid']
    VOCAB_OUTPUT_TEST = config.vocab_output_path['test_vocab']
    VOCAB_OUTPUT_VAL = config.vocab_output_path['valid_vocab']

    mapping_save(VOCAB, RAW_TEST_DATA, VOCAB_OUTPUT_TEST)
    mapping_save(VOCAB, RAW_VAL_DATA, VOCAB_OUTPUT_VAL)
    print('%s%s %s %s %s' % ('\n', '-' * 16, 'End', time.ctime(), '-' * 16))
