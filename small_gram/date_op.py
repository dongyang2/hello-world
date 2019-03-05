#! python3
# coding: utf-8
# 因为text_op简称to，这个time_op文件就叫date_op吧，就是不太严谨

import datetime
import time

if __name__ == '__main__':
    time_stamp = datetime.datetime.now()
    print(time_stamp.strftime('%Y.%m.%d %H:%M:%S'))
    print(time.ctime())
    print('\n', '-'*16, 'End', time.ctime(), '-'*16)
    print('{}{} {} {} {}'.format('\n', '-'*16, 'End', time.ctime(), '-'*16))
    print('-'*15, 'Start', time.ctime(), '-'*15, '\n')

    print('%s%s %s %s %s' % ('\n', '-'*16, 'End', time.ctime(), '-'*16))
