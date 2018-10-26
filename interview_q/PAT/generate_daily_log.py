# 并不是PAT里面的题，是我的小脚本


def get_work_day(days=100):
    import datetime
    date = datetime.datetime.now()
    # week_today = date.weekday()  # 3 周四
    # date_now = date.ctime()
    # weekday = date_now.split(' ')[0]

    date_li = []
    for i in range(days):
        add_day = datetime.timedelta(days=i)
        da_days = date + add_day
        # print(da_days.ctime())
        date_li.append(da_days.strftime('%a %y%m%d'))  # 自定义的日期格式，简化了后面很多步骤
    return date_li


def switch(var):  # 用于充当python中的switch,不过这是自定义的
    return {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thu': 4,
        'Fri': 5,
        'Sat': 6,
        'Sun': 7
    }.get(var, 'error')  # 'error'为默认返回值，可自设置


def switch2(var):
    return {
        'Mon': 1,
        'Tue': 2,
        'Wed': 3,
        'Thu': 4,
        'Fri': 5,
        'Sat': 0,
        'Sun': 0
    }.get(var, 'error')  # 'error'为默认返回值，可自设置


def write_daily_log(path, days=100):
    data_li = get_work_day(days)
    # k = 0
    for day in data_li:
        # if k == 3:
        #     break
        # k += 1
        if switch2(day.split(' ')[0]) == 0:
            continue
        else:
            file_name = path + '/' + day.split(' ')[1] + '.txt'
            # print(day, ' ------ ', file_name)
            with open(file_name, mode='w', encoding='utf-8') as f:
                f.write('\n')


def get_file_name(s, suffix='txt'):
    """适用于使用ctime()获得的日期格式化"""
    elem_of_date = s.split(' ')
    file_name = '_'.join([elem_of_date[1], elem_of_date[2], elem_of_date[4]])
    return '.'.join([file_name, suffix])


if __name__ == "__main__":
    # print(get_work_day())

    path1 = 'E:/常用文档/日志'
    write_daily_log(path1, 70)
