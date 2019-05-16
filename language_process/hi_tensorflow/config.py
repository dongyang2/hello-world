data_path = {
    # 这三个文件都是经过了预处理的
    'train': 'H:\PennTreebankDateset/simple-examples/data/ptb.train.txt',
    'test': 'H:\PennTreebankDateset/simple-examples/data/ptb.test.txt',
    'valid': 'H:\PennTreebankDateset/simple-examples/data/ptb.valid.txt'
}

vocab_output_path = {
    'vocab': 'output/ptb.vocab',  # 词汇到数字的映射表
    'train_vocab': 'output/ptb.train',   # 通过映射表转换得到的train文件
    'test_vocab': 'output/ptb.test',
    'valid_vocab': 'output/ptb.val'
}
