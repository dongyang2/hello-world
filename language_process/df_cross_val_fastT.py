import numpy as np
from sklearn.model_selection import train_test_split


def read_csv(path):
    import csv
    csv_reader = csv.reader(open(path, encoding='utf-8'))
    li = []
    i = 0
    for row in csv_reader:
        i += 1
        if i != 1:
            # print(row)
            li.append(row)
    arr = np.array(li)
    return arr


def write_ft_file(train_path):  # 写可以放入fastText的交叉验证文件
    source_data = read_csv(train_path)















if __name__ == '__main__':
    import time
    print('-----------START------cross_val_fastText', time.ctime(), '\n')

    print('\n----------END-----cross_val_fastText', time.ctime())