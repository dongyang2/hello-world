#! python3
# coding: utf-8
# 因为text_op简称to，这个time_op文件就叫date_op吧，就是不太严谨

import datetime
import time


def get_now_time(pat=None, cd=' ', ct=':', c=' ', num_mon=False, abb=True):
    """返回指定格式和连接符的当前时间。

    :param pat       时间格式，以空格分开，无视大小写。但注意这里month，minute不能简写成m。
    :type pat        str
    :param cd        日期连接符
    :type cd         str
    :param ct        时分秒的连接符
    :type ct         str
    :param num_mon   是否返回数字月
    :type num_mon    bool
    :param c         日期与时分秒的连接符
    :type c          str
    :param abb       是否对 月和日 缩写
    :type abb        bool
    """
    now = time.ctime()
    mon_dic = {
        'Jan': '01',
        'Feb': '02',
        'Mar': '03',
        'Apr': '04',
        'May': '05',
        'Jun': '06',
        'Jul': '07',
        'Aug': '08',
        'Sep': '09',
        'Oct': '10',
        'Nov': '11',
        'Dec': '12'
    }
    week, month, _, day, t, year = now.split(' ')  # 周几，月，空格，日，时分秒，年
    if num_mon is True:
        month = mon_dic[month]
        if abb is True and int(month) < 10:
            month = month[1]
    if abb is not True and int(day) < 10:
        day = '0'+day

    if pat is None:
        d_new = cd.join([year, month, day])
        return c.join([d_new, t, week])
    else:
        hour, minute, sec = t.split(':')
        pat_li = pat.split(' ')
        pat_time = []
        pat_day = []
        for p in pat_li:
            p = p.lower()
            if p == 'year' or p == 'y':
                pat_day.append(year)
            elif p == 'month' or p == 'mon':
                pat_day.append(month)
            elif p == 'day' or p == 'd':
                pat_day.append(day)
            elif p == 'hour' or p == 'h':
                pat_time.append(hour)
            elif p == 'minute' or p == 'min':
                pat_time.append(minute)
            elif p == 'sec' or p == 'second' or p == 's':
                pat_time.append(sec)
        t_new = ct.join(pat_time)
        d_new = cd.join(pat_day)
        return c.join([d_new, t_new])


if __name__ == '__main__':
    time_stamp = datetime.datetime.now()
    print(time_stamp.strftime('%Y.%m.%d %H:%M:%S'))
    print(time.ctime())
    print('\n', '-'*16, 'End', time.ctime(), '-'*16)
    print('{}{} {} {} {}'.format('\n', '-'*16, 'End', time.ctime(), '-'*16))
    print('-'*15, 'Start', time.ctime(), '-'*15, '\n')

    print(get_now_time('mon day h min', cd='-', num_mon=True, abb=False))

    print('%s%s %s %s %s' % ('\n', '-'*16, 'End', time.ctime(), '-'*16))
