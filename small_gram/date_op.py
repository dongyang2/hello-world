#! python3
# coding: utf-8
# 因为text_op简称to，这个time_op文件就叫date_op吧，就是不太严谨

import datetime

if __name__ == '__main__':
    time_stamp = datetime.datetime.now()
    print(time_stamp.strftime('%Y.%m.%d %H:%M:%S'))